from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:

    first = (By.ID, "first-name")
    last = (By.ID, "last-name")
    zip = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")

    total = (By.CLASS_NAME, "summary_total_label")
    finish = (By.ID, "finish")
    success = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_details(self):
        self.wait.until(EC.visibility_of_element_located(self.first)).send_keys("Arti")
        self.driver.find_element(*self.last).send_keys("Yadav")
        self.driver.find_element(*self.zip).send_keys("110011")
        self.driver.find_element(*self.continue_btn).click()

    def get_total(self):
        self.wait.until(EC.visibility_of_element_located(self.total))
        return self.driver.find_element(*self.total).text

    def finish_checkout(self):
        self.driver.find_element(*self.finish).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success)
        ).text




