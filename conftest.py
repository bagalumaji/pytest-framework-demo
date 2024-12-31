import pytest
from selenium import webdriver


@pytest.fixture()
def setup_and_teardown_browser(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()
