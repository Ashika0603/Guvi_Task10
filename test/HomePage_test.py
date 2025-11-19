import time
from sys import flags

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_homePage():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    user_name = "standard_user"
    password = "secret_sauce"
    driver.find_element(By.NAME, "user-name").send_keys(user_name)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    time.sleep(5)
    page_title = driver.title
    print(f"The title of the webpage is: {page_title}")

    if "Swag Labs" == page_title:
        print("Title of the web page is validated test passed")
    else:
        print("Title mismatch test failed")

    current_url = driver.current_url
    print(f"The current URL is: {current_url}")

    if "https://www.saucedemo.com/inventory.html" == current_url:
        print("URL of the homepage validation Successful")
    else:
        print("URL mismatch test failed")

    if user_name == "standard_user" and password == "secret_sauce":
         print("Logged in with given credentials test passed")
         print(f"URL of the dashboard is: {current_url}")
    else:
        print("invalid credentials test failed")



