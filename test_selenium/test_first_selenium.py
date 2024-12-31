import pytest


@pytest.mark.usefixtures('setup_and_teardown_browser')
class TestDemo:
    def test_first_demo(self):
        print(self.driver.title)
