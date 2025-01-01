import pytest

from driver.driver import Driver


@pytest.fixture()
def setup_and_teardown_browser(request):
    browser_name = request.config.getoption('browser')
    Driver.init_driver(browser_name)
    yield
    Driver.close_driver()


def pytest_addoption(parser):
    browser_name = "chrome"
    parser.addoption("--browser", action="store", default=browser_name, help="provide browser name as - chrome, firefox...")
