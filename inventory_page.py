from selenium.webdriver.common.by import By

class InventoryPage:

    sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    add_bike = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    onesie = (By.ID, "item_2_title_link")

    def __init__(self, driver):
        self.driver = driver

    def sort_low_to_high(self):
        self.driver.find_element(*self.sort_dropdown).send_keys("lohi")

    def add_two_items(self):
        self.driver.find_element(*self.add_backpack).click()
        self.driver.find_element(*self.add_bike).click()

    def open_onesie(self):
        self.driver.find_element(*self.onesie).click()

    def cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

