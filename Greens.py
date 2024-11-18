# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# #from webdriver_manager.chrome import ChromeDriverManager
# import time
#
# # Setup WebDriver (using Chrome here)
# driver = webdriver.Chrome()
#
# driver.get("https://www.greenstechnologys.com/python-training.html")
#
# training=driver.find_element(By.XPATH,"/html/body/header[2]/div[1]/div/div/div[3]/ul/li[1]/a")
# training.click()
#
# home=driver.find_element(By.XPATH,"/html/body/nav/div/div/ul/li[1]/a")
# home.click()
#
# course=driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/ul/li[4]/a")
# course.click()
#
# selenium=driver.find_element(By.XPATH,"/html/body/section[1]/div[2]/div/div[1]/a/img")
# selenium.click()
#
# time.sleep(100)





from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from webdriver_manager.chrome import ChromeDriverManager  # Use this to handle the driver automatically
import time

# Setup WebDriver (using Chrome here)
driver = webdriver.Chrome()

# Open the Python Training page
driver.get("https://www.greenstechnologys.com/python-training.html")

# Use WebDriverWait to wait for the 'Training' link to be clickable
training = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//header//div[1]//a[text()='Training']"))
)
training.click()

# Wait for the 'Home' link to be clickable and click it
home = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//nav//a[text()='Home']"))
)
home.click()

# Wait for the 'Course' link to be clickable and click it
course = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-item']//a[text()='Courses']"))
)
course.click()

# Wait for the Selenium course image to be clickable and click it
selenium = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//section//a[@href='selenium-training.html']//img"))
)
selenium.click()

# Wait for a few seconds before closing (for visual confirmation)
time.sleep(5)

# Close the browser
driver.quit()


