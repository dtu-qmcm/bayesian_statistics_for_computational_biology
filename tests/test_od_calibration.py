import numpy as np
import pytest
from scipy.stats import halfnorm, norm

from course_exercises import od_calibration

CONCENTRATION = np.array([0.0, 0.5, 1.0, 2.0, 4.0])
OD = np.array([0.02, 0.27, 0.49, 1.03, 1.98])


def test_predict_od_scalar():
    assert od_calibration.predict_od(2.0, 0.1, 0.5) == pytest.approx(1.1)


def test_predict_od_vectorised():
    np.testing.assert_allclose(
        od_calibration.predict_od(CONCENTRATION, 0.1, 0.5),
        0.1 + 0.5 * CONCENTRATION,
    )


def test_get_log_likelihood_matches_scipy():
    expected = norm.logpdf(OD, 0.01 + 0.5 * CONCENTRATION, 0.05).sum()
    assert od_calibration.get_log_likelihood(OD, CONCENTRATION, 0.01, 0.5, 0.05) == (
        pytest.approx(expected, rel=1e-5)
    )


def test_get_log_likelihood_prefers_good_fit():
    good = od_calibration.get_log_likelihood(OD, CONCENTRATION, 0.01, 0.5, 0.05)
    bad = od_calibration.get_log_likelihood(OD, CONCENTRATION, 0.01, 1.0, 0.05)
    assert good > bad


def test_get_log_prior_matches_scipy():
    expected = (
        norm.logpdf(0.01, 0.0, 0.1)
        + norm.logpdf(0.5, 1.0, 1.0)
        + halfnorm.logpdf(0.05, scale=0.1)
    )
    assert od_calibration.get_log_prior(0.01, 0.5, 0.05) == pytest.approx(
        expected, rel=1e-5
    )


@pytest.mark.parametrize("sigma", [0.0, -0.1])
def test_get_log_prior_rejects_non_positive_sigma(sigma):
    assert od_calibration.get_log_prior(0.01, 0.5, sigma) == -np.inf


def test_get_log_posterior_matches_scipy():
    expected = (
        norm.logpdf(0.01, 0.0, 0.1)
        + norm.logpdf(0.5, 1.0, 1.0)
        + halfnorm.logpdf(0.05, scale=0.1)
        + norm.logpdf(OD, 0.01 + 0.5 * CONCENTRATION, 0.05).sum()
    )
    assert od_calibration.get_log_posterior(OD, CONCENTRATION, 0.01, 0.5, 0.05) == (
        pytest.approx(expected, rel=1e-5)
    )
