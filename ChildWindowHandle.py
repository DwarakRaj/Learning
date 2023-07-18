from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.implicitly_wait(5)
get_title = driver.title
print(get_title)

driver.find_element(By.CLASS_NAME, "blinkingText").click()
mainWindow = driver.window_handles
#Handling Child window
driver.switch_to.window(mainWindow[1])
credentials = driver.find_element(By.XPATH, "//a[contains(text(),'mentor@rahulshettyacademy.com')]").text
print(credentials)
#Switch back to main window
driver.switch_to.window(mainWindow[0])
driver.find_element(By.XPATH,"//input[@id='username']").send_keys(credentials)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys(credentials)
sleep(2)
driver.find_element(By.ID,"signInBtn").click()
Wait = WebDriverWait(driver,10)
Wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)


