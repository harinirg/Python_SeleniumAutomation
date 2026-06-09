from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
body = driver.find_element(By.TAG_NAME, "body")
origin = ScrollOrigin.from_element(body)
ActionChains(driver).scroll_from_origin(origin,0,800).perform()
time.sleep(3)
iframe = driver.find_element(By.ID, "iframe1")
driver.switch_to.frame(iframe)
question = driver.find_element(
    By.XPATH, "//a[normalize-space()='What is Selenium?']").text
assert question == "What is Selenium?"
print("Success")
time.sleep(5)
driver.quit()