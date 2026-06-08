from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://automationexercise.com/")
# Verify Home Page
if driver.title == "Automation Exercise":
    print("Home page was launched")
else:
    print("Home page was not launched")
# Hide advertisement iframes
iframes = driver.find_elements(By.TAG_NAME, "iframe")
for iframe in iframes:
    driver.execute_script("arguments[0].style.display='none';",iframe)
# Click Products
products = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/products']")))
driver.execute_script("arguments[0].click();",products)
actions = ActionChains(driver)
blue_top = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//p[text()='Blue Top']/ancestor::div[@class='product-image-wrapper']")))
actions.move_to_element(blue_top).perform()
blue_add_cart = driver.find_element(By.XPATH,"(//a[contains(@data-product-id,'1') and contains(text(),'Add to cart')])[1]")
driver.execute_script("arguments[0].click();",blue_add_cart)
continue_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Continue Shopping')]")))
continue_btn.click()
men_tshirt = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//p[text()='Men Tshirt']/ancestor::div[@class='product-image-wrapper']")))
actions.move_to_element(men_tshirt).perform()
men_add_cart = driver.find_element(By.XPATH,"(//a[contains(@data-product-id,'2') and contains(text(),'Add to cart')])[1]")
driver.execute_script("arguments[0].click();",men_add_cart)
view_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']")))
view_cart.click()
assert driver.find_element(By.XPATH,"//a[text()='Blue Top']").is_displayed()
assert driver.find_element(By.XPATH,"//a[text()='Men Tshirt']").is_displayed()
print("Both products are added to cart")
print("Blue Top Price:",driver.find_element(By.XPATH,"//a[text()='Blue Top']/ancestor::tr//td[@class='cart_price']/p").text)
print("Blue Top Quantity:",driver.find_element(By.XPATH,"//a[text()='Blue Top']/ancestor::tr//button").text)
print("Blue Top Total:",driver.find_element(By.XPATH,"//a[text()='Blue Top']/ancestor::tr//td[@class='cart_total']/p").text)
print("Men Tshirt Price:",driver.find_element(By.XPATH,"//a[text()='Men Tshirt']/ancestor::tr//td[@class='cart_price']/p").text)
print("Men Tshirt Quantity:",driver.find_element( By.XPATH,"//a[text()='Men Tshirt']/ancestor::tr//button").text)
print("Men Tshirt Total:",driver.find_element(By.XPATH,"//a[text()='Men Tshirt']/ancestor::tr//td[@class='cart_total']/p").text)
driver.quit()