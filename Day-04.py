import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start the WebDriver (Chrome)
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://www.greenstechnologys.com/")

# Wait until the 'Contact' link is clickable
contact_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='contact.php']"))
)
contact_link.click()

# Wait until the form heading is visible
form_heading = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div/div/h3"))
)

# Fill the form fields
name = driver.find_element(By.XPATH, "//input[@id='InputName']")
name.send_keys("Raghavi")

email = driver.find_element(By.XPATH, "//input[@id='InputEmail1']")
email.send_keys("rag@gmail.com")

number = driver.find_element(By.XPATH, "//input[@id='InputSubject']")
number.send_keys("8754532220")

# Select course from the dropdown
course_dropdown = driver.find_element(By.XPATH, "//select[@class='form-control']")
course_select = Select(course_dropdown)
course_select.select_by_visible_text("Selenium")  # Example option, replace with actual text

# Select branch from the second dropdown
branch_dropdown = driver.find_element(By.XPATH, "//select[@class='form-control'][2]")
branch_select = Select(branch_dropdown)
branch_select.select_by_visible_text("Software Testing")  # Example option, replace with actual text

# Select plan from the third dropdown
plan_dropdown = driver.find_element(By.XPATH, "//select[@class='form-control'][3]")
plan_select = Select(plan_dropdown)
plan_select.select_by_visible_text("Basic")  # Example option, replace with actual text

# Enter message
message = driver.find_element(By.XPATH, "//textarea[@class='form-control input-message']")
message.send_keys("Interested in your training programs.")

# Submit the form
submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
submit_button.click()

# Wait for confirmation or completion (you can modify this based on the website response)
WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

# Optional: pause to review results
time.sleep(5)

# Close the driver
driver.quit()
