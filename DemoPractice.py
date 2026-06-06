import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
search_box=driver.find_element(By.ID,value="APjFqb")
search_box.send_keys("Selenium")
search_button=driver.find_element(By.NAME,value="btnK")
if(search_button.is_enabled()):
    print("The button is enabled")
else:
    print("The button is disabled")
search_button.click()
driver.close()
