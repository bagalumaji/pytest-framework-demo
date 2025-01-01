from selenium import webdriver

from exceptions.browser_not_supported_exception import BrowserNotSupportedError


class DriverFactory:
    _browser_dict = {"chrome": lambda: webdriver.Chrome(), "firefox": lambda: webdriver.Firefox()}

    @staticmethod
    def get_driver(browser_name):
        if browser_name not in DriverFactory._browser_dict:
            raise BrowserNotSupportedError(browser_name)

        return DriverFactory._browser_dict.get(browser_name)()
