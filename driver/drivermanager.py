import threading

from selenium.webdriver.remote.webdriver import WebDriver


class DriverManager:
    _thread_local_driver: WebDriver = threading.local()

    @staticmethod
    def get_driver() -> WebDriver:
        return getattr(DriverManager._thread_local_driver, "driver", None)

    @staticmethod
    def set_driver(driver: WebDriver):
        DriverManager._thread_local_driver.driver = driver

    @staticmethod
    def unload():
        if hasattr(DriverManager._thread_local_driver, "driver"):
            del DriverManager._thread_local_driver.driver
