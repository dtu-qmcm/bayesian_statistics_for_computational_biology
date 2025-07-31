import arviz as az


def get_idata(states, info, coords=None, dims=None):
    idata = az.convert_to_inference_data(
        states.position,
        group="posterior",
        coords=coords,
        dims=dims,
    )
    idata.add_groups({"sample_stats": info._asdict()})
    return idata
