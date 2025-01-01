from driver.drivermanager import DriverManager
from factory.driverfactory import DriverFactory


class Driver:
    @staticmethod
    def init_driver(browser_name):
        DriverManager.set_driver(DriverFactory.get_driver(browser_name))
        DriverManager.get_driver().get("https://tutorialsninja.com/demo/index.php")

    @staticmethod
    def close_driver():
        DriverManager.get_driver().quit()
        DriverManager.unload()
