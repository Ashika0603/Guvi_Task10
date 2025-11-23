
from HomePageValidation import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def teardown(driver):
    driver.quit()

def test_homePage():

    if "Swag Labs" == page_title:
        print("Title of the web page is validated test passed")
    else:
        print("Title mismatch test failed")
    teardown(driver)


def test_current_url():

    if "https://www.saucedemo.com/inventory.html" == current_url:
            print("URL of the homepage validation is Successful")
    else:
            print("URL mismatch test failed")
    teardown(driver)


def test_invalid_login():
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)
        driver.find_element(By.NAME, "user-name").send_keys("standard_user1")
        driver.find_element(By.NAME, "password").send_keys("secret_sauce2")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(5)
        error_message = driver.find_element(By.CLASS_NAME, "error-message-container.error")

        if error_message.is_displayed():
            print(f"Login failed: Error message displayed: {error_message.text}")
    except NoSuchElementException:
        print("Login successful: No error message found.")

        teardown(driver)











