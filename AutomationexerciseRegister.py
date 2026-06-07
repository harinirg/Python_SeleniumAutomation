import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads')   ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')       ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")
driver=webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
driver.get("http://automationexercise.com")
wait=WebDriverWait(driver,15)
signin = driver.find_element(By.XPATH,value="//a[@href='/login']")
if signin.is_displayed():
    print("HomePage is displayed")
else:
    print("HomePage is not displayed")
signin.click()
new_user=driver.find_element(By.XPATH,value="//h2[text()='New User Signup!']")
if new_user.is_displayed():
    print("New user page is displayed")
else:
    print("New user page is not displayed")
new_name=driver.find_element(By.XPATH,value="//input[@name='name']")
new_name.send_keys("harini")
new_email=driver.find_element(By.XPATH,value="(//input[@name='email'])[2]")
new_email.send_keys("rgharini30@gmail.com")
driver.find_element(By.XPATH,value="//button[text()='Signup']").click()
driver.find_element(By.XPATH,value="//input[@id='id_gender2']").click()
driver.find_element(By.ID,value="password").send_keys("Harni61@26")
Select(driver.find_element(By.ID,"days")).select_by_visible_text("10")
Select(driver.find_element(By.ID,"months")).select_by_visible_text("January")
Select(driver.find_element(By.ID,"years")).select_by_visible_text("2004")
driver.find_element(By.XPATH,value="//input[@name='newsletter']").click()
driver.find_element(By.ID,value="optin").click()
driver.find_element(By.ID,value="first_name").send_keys("Halini")
driver.find_element(By.ID,value="last_name").send_keys("Raja")
driver.find_element(By.XPATH,value="//input[@id='company']").send_keys("Expleo")
driver.find_element(By.XPATH,value="//input[@data-qa='address']").send_keys("6/181(1),Anna nagar,Salem")
driver.find_element(By.XPATH,value="//input[@name='address2']").send_keys("1/121(1),Attayampatti")
driver.find_element(By.XPATH,value="//input[@data-qa='state']").send_keys("Tamil Nadu")
driver.find_element(By.XPATH,value="//input[@data-qa='city']").send_keys("Salem")
driver.find_element(By.ID,value="zipcode").send_keys("637505")
driver.find_element(By.XPATH,value="//input[@data-qa='mobile_number']").send_keys("7897345091")
driver.find_element(By.XPATH,value="//button[text()='Create Account']").click()
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH,"//a[@data-qa='continue-button']"))).click()
dismiss_ads(driver)
logged_in = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Logged in as')]")))
print(logged_in.text)
if logged_in:
    print("Logged in successfully")
else:
    print("Failed")
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/delete_account']"))).click()
dismiss_ads(driver)

continue_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@data-qa='continue-button']")
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView(true);",
    continue_btn
)

continue_btn.click()