#**********example01**********

# import time
#
# from selenium import webdriver
# driver=webdriver.Firefox()
#
# driver.get("https://www.google.com/")
#
# time.sleep(10)


# import time
#
# from selenium import webdriver
# driver=webdriver.Firefox()
# driver.get("https://www.facebook.com/")
# time.sleep(10)

# import time
#
# from selenium import webdriver
# driver=webdriver.Firefox()
# driver.get("https://www.amazon.in/")
# time.sleep(10)


import time

from selenium import webdriver
driver=webdriver.Firefox()
driver.get("http://greenstech.in/selenium-course-content.html")
title=driver.title
print(title)
time.sleep(10)

#*********example02***********

