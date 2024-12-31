from selenium import webdriver

from driver.drivermanager import DriverManager


class Driver:
    @staticmethod
    def init_driver():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("")
        DriverManager.set_driver(driver)

    @staticmethod
    def close_driver():
        pass
