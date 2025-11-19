from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#initiating chrome
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
time.sleep(5)
#passing username and password
driver.find_element(By.NAME,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(5)

try:
      #getting tite value
      page_title = driver.title
      print(f"The title of the webpage is: {page_title}")
      #getting current URL value
      current_url = driver.current_url
      print(f"The current URL is: {current_url}")
      #getting the entire page content
      page_content = driver.page_source
      filename = "webpage_task_11.txt"
      #save the content to the text file
      with open(filename, "w", encoding="utf-8") as file:
          file.write(page_content)
      print(f"Webpage content successfully saved to {filename}")

      # Extract text values from the page
      page_content = driver.find_element(By.TAG_NAME, "html").text
      filename = "webpage_task_10.txt"
      # save the content to the text file
      with open(filename, "w", encoding="utf-8") as file:
          file.write(page_content)
      print(f"Webpage content successfully saved to {filename}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
