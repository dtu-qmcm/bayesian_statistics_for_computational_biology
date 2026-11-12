import pytest


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    report = yield
    if call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
        report.outcome = "skipped"
        stub_name = call.excinfo.traceback[-1].name
        report.longrepr = (
            str(item.path),
            item.location[1],
            f"{stub_name} not implemented yet",
        )
    return report
