import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui.selects
driver=webdriver.Chrome()

driver.get("https://www.greenstechnologys.com/")

element=driver.find_element(By.XPATH,"//a[@href='contact.php']")
element.click()

form=driver.find_element(By.XPATH,"/html/body/div[1]/section[2]/div/div/h3")

name=driver.find_element(By.XPATH,"//input[@id='InputName']")
name.send_keys("Raghavi")

email=driver.find_element(By.XPATH,"//input[@id='InputEmail1']")
email.send_keys("rag@gmail.com")

number=driver.find_element(By.XPATH,"//input[@id='InputSubject']")
number.send_keys("8754532220")

course=driver.find_element(By.XPATH,"//select[@class='form-control']")
course.is_selected()

branch=driver.find_element(By.XPATH,"//select[@class='form-control'][2]")
branch.is_selected()

plan=driver.find_element(By.XPATH,"//select[@class='form-control'][3]")
plan.is_selected()

message=driver.find_element(By.XPATH,"//textarea[@class='form-control input-message']")
message.send_keys("interested")

button=driver.find_element(By.XPATH,"//button[@id='submit']")
button.click()

time.sleep(100)