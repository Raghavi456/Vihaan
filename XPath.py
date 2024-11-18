import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")

account=driver.find_element(By.XPATH,"//*[@id='u_0_0_0n']")
account.click()

name=driver.find_element(By.XPATH,"//input[@id='u_0_8_9u']")
name.send_keys("Raghavi")



time.sleep(10)