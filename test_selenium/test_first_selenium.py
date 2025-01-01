import time

import pytest

from driver.drivermanager import DriverManager


@pytest.mark.usefixtures('setup_and_teardown_browser')
class TestDemo:

    def test_first_demo(self):
        print(DriverManager.get_driver().title)
        time.sleep(3)
