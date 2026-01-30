from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
options = webdriver.EdgeOptions()
options.add_experimental_option("excludeSwitches",["enable-logging"])

driver = webdriver.Edge(options=options)

def test_login():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    assert driver.find_element(By.CSS_SELECTOR, value=".login_logo") 
    driver.find_element(By.ID, value="user-name").send_keys("standard_user")
    driver.find_element(By.ID, value="password").send_keys("secret_sauce")
    driver.find_element(By.ID, value="login-button").click()
    title = driver.find_element(By.XPATH, value="//span[@class='title']").text
    assert "PRODUCTS" == title
    time.sleep(3)
    
def test_wrongLogin():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    assert driver.find_element(By.CSS_SELECTOR, value=".login_logo") 
    driver.find_element(By.ID, value="user-name").send_keys("standard_user")
    driver.find_element(By.ID, value="password").send_keys("secret_auce")
    driver.find_element(By.ID, value="login-button").click()
    title = driver.find_element(By.CSS_SELECTOR, value="h3[data-test='error']").text
    assert "Epic sadface" in title
    time.sleep(3)