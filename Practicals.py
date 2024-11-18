import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://demo.automationtesting.in/Windows.html")

# actual_title=driver.title
# expected_title="DEMOAUT.COM"
#
# if actual_title==expected_title:
#     print(driver.title)
# else:
#     print("not matching")

print(driver.title)
print(driver.current_url)


driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()

time.sleep(10)

driver.close()