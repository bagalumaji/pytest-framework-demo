import time

import pytest

from driver.drivermanager import DriverManager


@pytest.mark.usefixtures('setup_and_teardown_browser')
class TestSecond:
    def test_second_selenium(self):
        print(DriverManager.get_driver().title)
        time.sleep(3)

    def test_second_selenium_1(self):
        print(DriverManager.get_driver().title)
        time.sleep(3)
