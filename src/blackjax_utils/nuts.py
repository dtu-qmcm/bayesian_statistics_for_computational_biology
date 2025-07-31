import os
from functools import partial

import blackjax
import jax
from jax import numpy as jnp


def get_init_params(key, base, sd):
    def jitter_leaf(key, base_leaf, sd_leaf):
        return sd_leaf + jax.random.normal(key, shape=base_leaf.shape) * sd_leaf

    flat_means, treedef = jax.tree.flatten(base)
    keys = jax.random.split(key, num=len(flat_means))
    keytree = jax.tree.unflatten(treedef, keys)
    if sd is None:
        sd = jax.tree.map(jnp.zeros_like, base)
    return jax.tree.map(jitter_leaf, keytree, base, sd)


def run_warmup(key, params, target_density, draws, warmup_kwargs):
    warmup = blackjax.window_adaptation(
        blackjax.nuts,
        target_density,
        **warmup_kwargs,
    )
    (initial_states, tuned_params), _ = warmup.run(key, params, draws)  # type: ignore
    return initial_states, tuned_params


def inference_loop(key, initial_state, params, target_logdensity, num_samples):
    kernel = blackjax.nuts(target_logdensity, **params).step

    @jax.jit
    def one_step(state, rng_key):
        state, info = kernel(rng_key, state)
        return state, (state, info)

    keys = jax.random.split(key, num_samples)
    _, (states, info) = jax.lax.scan(one_step, initial_state, keys)

    return states, info


def get_kernel(tuned_params, target_density):
    return blackjax.nuts(target_density, **tuned_params).step


inference_loop_pmap = jax.pmap(
    inference_loop,
    in_axes=(0, 0, 0, None, None),
    static_broadcasted_argnums=(3, 4),
)
get_kernel_pmap = jax.pmap(
    get_kernel,
    in_axes=(0,),
    static_broadcasted_argnums=(1,),
)


def run_nuts(
    key,
    log_posterior,
    init_params,
    init_sd=None,
    n_chain=4,
    n_warmup=500,
    n_sample=500,
    **warmup_kwargs,
):
    if jax.local_device_count() >= n_chain:
        warmup_func = jax.pmap(
            partial(run_warmup, warmup_kwargs=warmup_kwargs),
            in_axes=(0, 0, None, None),
            static_broadcasted_argnums=(2, 3),
        )
        sample_func = inference_loop_pmap
    else:
        warmup_func = jax.vmap(
            partial(run_warmup, warmup_kwargs=warmup_kwargs),
            in_axes=(0, 0, None, None),
        )
        sample_func = jax.vmap(
            inference_loop,
            in_axes=(0, 0, 0, None, None),
        )

    sample_key, warmup_key, init_key = jax.random.split(key, 3)
    warmup_keys = jax.random.split(warmup_key, n_chain)
    sample_keys = jax.random.split(sample_key, n_chain)
    init_keys = jax.random.split(init_key, n_chain)
    get_init_params_vmap = jax.vmap(get_init_params, in_axes=(0, None, None))
    init_params = get_init_params_vmap(init_keys, init_params, init_sd)
    initial_states, tuned_params = warmup_func(
        warmup_keys,
        init_params,
        log_posterior,
        n_warmup,
    )
    states, info = sample_func(
        sample_keys,
        initial_states,
        tuned_params,
        log_posterior,
        n_sample,
    )
    return states, info
