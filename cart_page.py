from selenium.webdriver.common.by import By

class CartPage:

    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    remove_btn = (By.ID, "remove-sauce-labs-onesie")
    checkout_btn = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def remove_item(self):
        self.driver.find_element(*self.remove_btn).click()

    def checkout(self):
        self.driver.find_element(*self.checkout_btn).click()



