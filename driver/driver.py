from driver.drivermanager import DriverManager
from enums.browser import Browser
from factory.driverfactory import DriverFactory


class Driver:
    @staticmethod
    def init_driver(browser_name: Browser):
        if not DriverManager.get_driver():
            DriverManager.set_driver(DriverFactory.get_driver(browser_name))
            DriverManager.get_driver().maximize_window()
            DriverManager.get_driver().get("https://tutorialsninja.com/demo/index.php")

    @staticmethod
    def close_driver():
        if driver := DriverManager.get_driver():
            driver.quit()
            DriverManager.unload()
