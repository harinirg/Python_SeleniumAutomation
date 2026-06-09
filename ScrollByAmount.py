from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
actions = ActionChains(driver)
# Scroll down by 800 pixels
actions.scroll_by_amount(0, 800).perform()
time.sleep(3)
iframe = driver.find_element(By.ID, "iframe1")
driver.switch_to.frame(iframe)
question = driver.find_element(
    By.XPATH,"//a[normalize-space()='What is Selenium?']").text
assert question == "What is Selenium?"
print("Success")
time.sleep(5)
driver.quit()