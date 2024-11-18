import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.greenstechnologys.com/")

print(driver.title) #1ST URL

time.sleep(5)

driver.get("https://www.greenstechnologys.com/courses.html")

print(driver.title) #2ND URL
time.sleep(5)
driver.back()

time.sleep(5)

print(driver.title) #1ST URL

driver.forward()

time.sleep(5)

print(driver.title) #2nd URL

time.sleep(5)

