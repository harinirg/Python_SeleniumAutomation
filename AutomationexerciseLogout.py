import time
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.implicitly_wait(15)
driver.maximize_window()
if driver.title == "Automation Exercise":
    print("Home page was launched")
else:
    print("Home page was not launched")
driver.find_element(By.XPATH,value="//a[text()=' Signup / Login']").click()
login_page = driver.find_element(By.XPATH,value="//div[@class='login-form']/child::h2").text
if login_page.__eq__("Login to your account"):
    print("Login section was displayed")
else:
    print("Login section was not displayed")
driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[2]").send_keys("harinigokulraja@gmail.com")
driver.find_element(By.XPATH,value="//form[@action='/login']/child::input[3]").send_keys("harini@26")
driver.find_element(By.XPATH,value="//form[@action='/login']/child::button").click()
logged_in = driver.find_element(By.XPATH,value="//ul[@class='nav navbar-nav']/child::*[10]").is_displayed()
if logged_in:
    print("Logged in successfully")
else:
    print("Unsuccessfull login")
driver.find_element(By.XPATH,value="//a[text()=' Logout']").click()
url = driver.current_url

if url.__eq__("https://automationexercise.com/login"):
    print("Logout successfull")
else:
    print("Unsuccessfull logout")

driver.close()