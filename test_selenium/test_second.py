import time

from driver.drivermanager import DriverManager


def test_second_selenium(setup_and_teardown_browser):
    print(DriverManager.get_driver().title)
    time.sleep(3)
