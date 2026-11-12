# Exercise: calibrate an optical density meter

## The model

You have an optical density meter and some samples of known concentration. In this exercise you will write a Bayesian model that links the meter's readings to the samples' concentrations, so that later you can use the meter to measure samples of unknown concentration.

The model assumes that the meter's expected reading increases linearly with concentration, and that normally distributed noise moves each reading away from its expected value:

$$
\begin{align*}
od_i &\sim N(\alpha + \beta \cdot c_i, \sigma) \\
\alpha &\sim N(0, 0.1) \\
\beta &\sim N(1, 1) \\
\sigma &\sim HN(0.1)
\end{align*}
$$

## Getting started

The module `src/course_exercises/od_calibration.py` contains four unfinished functions, and `tests/test_od_calibration.py` contains tests that check them. Run the tests like this:

```sh
uv sync
uv run pytest -rs
```

At first pytest skips every test and lists the function each skipped test is waiting for. When you replace a function's `raise NotImplementedError` line with your own code, pytest starts running that function's tests and reports whether they pass or fail.

## Tasks

Fill in the functions in the order they appear in the module, running the tests after each one. Each function's docstring describes what it should return. You may find `jax.scipy.stats.norm.logpdf` useful.
