import pytest

from pages.home_page import HomePage


@pytest.mark.usefixtures('setup_and_teardown_browser')
class TestDemo:

    def test_first_demo(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account()
        home_page.click_on_login()
