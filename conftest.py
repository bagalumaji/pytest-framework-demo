import pytest

from driver.driver import Driver
from enums.browser import Browser
from exceptions.browser_not_supported_exception import BrowserNotSupportedError


@pytest.fixture()
def setup_and_teardown_browser(request):
    browser_name = get_browser(request.config.getoption('browser'))
    Driver.init_driver(browser_name)
    yield
    Driver.close_driver()


def pytest_addoption(parser):
    browser_name = "chrome"
    parser.addoption("--browser", action="store", default=browser_name,
                     help="provide browser name as - chrome, firefox...")


def get_browser(browser_name) -> Browser:
    try:
        browser = Browser(browser_name)
        return browser
    except Exception:
        raise BrowserNotSupportedError(browser_name)
