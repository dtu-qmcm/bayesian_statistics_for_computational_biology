"""Functions for calibrating an optical density meter.

The functions describe a Bayesian model of a meter whose readings depend
linearly on a sample's concentration, with normally distributed measurement
error.
"""

import jax.numpy as jnp
from jax import Array
from jax.scipy.stats import norm
from jax.typing import ArrayLike


def predict_od(
    concentration: ArrayLike,
    intercept: ArrayLike,
    slope: ArrayLike,
) -> Array:
    """Predict the optical density of some samples from their concentrations.

    Args:
        concentration: Concentration of each sample.
        intercept: Optical density the meter reports for a blank sample.
        slope: Change in optical density per unit of concentration.

    Returns:
        The predicted optical density of each sample, with the same shape as
        concentration.
    """
    return intercept + slope * jnp.asarray(concentration)


def get_log_likelihood(
    od: ArrayLike,
    concentration: ArrayLike,
    intercept: ArrayLike,
    slope: ArrayLike,
    sigma: ArrayLike,
) -> Array:
    """Get the log likelihood of some optical density measurements.

    Each measurement follows a normal distribution centred on the optical
    density that predict_od gives for its sample's concentration.

    Args:
        od: Measured optical density of each sample.
        concentration: Known concentration of each sample.
        intercept: Optical density the meter reports for a blank sample.
        slope: Change in optical density per unit of concentration.
        sigma: Standard deviation of the measurement error.

    Returns:
        The sum of the log densities of all the measurements.
    """
    expected_od = predict_od(concentration, intercept, slope)
    return norm.logpdf(od, expected_od, sigma).sum()


def get_log_prior(
    intercept: ArrayLike,
    slope: ArrayLike,
    sigma: ArrayLike,
) -> Array:
    """Get the log prior density of the calibration parameters.

    The parameters have these prior distributions:

        intercept ~ Normal(0, 0.1)
        slope ~ Normal(1, 1)
        sigma ~ HalfNormal(0.1)

    Args:
        intercept: Optical density the meter reports for a blank sample.
        slope: Change in optical density per unit of concentration.
        sigma: Standard deviation of the measurement error.

    Returns:
        The sum of the three parameters' log prior densities, or negative
        infinity if sigma is not positive.
    """
    log_density = (
        norm.logpdf(intercept, 0.0, 0.1)
        + norm.logpdf(slope, 1.0, 1.0)
        + jnp.log(2.0)
        + norm.logpdf(sigma, 0.0, 0.1)
    )
    return jnp.where(sigma > 0, log_density, -jnp.inf)


def get_log_posterior(
    od: ArrayLike,
    concentration: ArrayLike,
    intercept: ArrayLike,
    slope: ArrayLike,
    sigma: ArrayLike,
) -> Array:
    """Get the unnormalised log posterior density of the calibration parameters.

    Args:
        od: Measured optical density of each sample.
        concentration: Known concentration of each sample.
        intercept: Optical density the meter reports for a blank sample.
        slope: Change in optical density per unit of concentration.
        sigma: Standard deviation of the measurement error.

    Returns:
        The sum of the log prior density and the log likelihood.
    """
    return get_log_prior(intercept, slope, sigma) + get_log_likelihood(
        od, concentration, intercept, slope, sigma
    )
