from selenium.webdriver.common.by import By

class MenuPage:

    menu = (By.ID,"react-burger-menu-btn")
    logout = (By.ID,"logout_sidebar_link")

    def __init__(self,driver):
        self.driver = driver

    def logout_user(self):
        self.driver.find_element(*self.menu).click()
        self.driver.find_element(*self.logout).click()
