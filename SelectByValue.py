from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.leafground.com/select.xhtml")
dropdown = driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']")
select = Select(dropdown)
for option in select.options:
    print("Text:", option.text,"| Value:", option.get_attribute("value"))

time.sleep(5)
driver.quit()