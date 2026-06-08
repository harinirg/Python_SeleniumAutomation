from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.leafground.com/")
if(driver.title=="Dashboard"):
    print("Home page is displayed successfully.")
else:
    print("Unsuccessful")
wait=WebDriverWait(driver,15)
wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Element']/parent::a"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,"//li[@id='menuform:m_dropdown']/child::a"))).click()
expected_url = "https://www.leafground.com/select.xhtml"
if expected_url in driver.current_url:
    print("URL Verified Successfully")
else:
    print("URL Verification Failed")
select_tool=driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']")
drop_down1=Select(select_tool)
tool1=drop_down1.select_by_visible_text("Playwright")

print("Playwright is selected")
tool2=drop_down1.select_by_index(3)
print("Puppeteer is selected")
print(drop_down1.first_selected_option.text)
drop_down2=driver.find_element(By.XPATH,"//li[@class='ui-autocomplete-input-token']//input")
drop_down2.send_keys("Python")
drop_down2.send_keys(Keys.ENTER)
drop_down2.send_keys("Selenium")
drop_down2.send_keys(Keys.ENTER)
drop_down2.send_keys("Java")
drop_down2.send_keys(Keys.ENTER)
print("Selected sucessfully")
driver.close()