from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup WebDriver (using Chrome here)
driver = webdriver.Chrome()

# Open Amazon website
driver.get("https://www.amazon.com/ap/signin")

# Wait for the page to load (implicit wait)
driver.implicitly_wait(5)

# Enter the username (email or phone number)
email_field = driver.find_element(By.ID, "ap_email")
email_field.send_keys("your-email@example.com")

# Click on "Continue" to proceed to the password page
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()

# Wait for the password field to load
driver.implicitly_wait(5)

# Enter the password
password_field = driver.find_element(By.ID, "ap_password")
password_field.send_keys("your-password")

# Click on the Sign-In button
sign_in_button = driver.find_element(By.ID, "signInSubmit")
sign_in_button.click()

# Wait for a while to see if login was successful
time.sleep(5)

# Close the browser
driver.quit()
