from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver = driver

    def click_on_login(self):
        self.driver.find_element(By.LINK_TEXT, "Login").click()

    def click_on_my_account(self):
        self.driver.find_element(By.LINK_TEXT, "My Account").click()
