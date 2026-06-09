from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
actions = ActionChains(driver)
iframe = driver.find_element(By.ID,"iframe1")
actions.scroll_to_element(iframe).perform()
time.sleep(3)
driver.switch_to.frame(iframe)
question = driver.find_element(By.XPATH,"//a[normalize-space()='What is Selenium?']").text
assert question == "What is Selenium?"
time.sleep(5)
driver.quit()
print("Success")