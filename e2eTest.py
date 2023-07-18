from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver.get("https://rahulshettyacademy.com/angularpractice/shop")
driver.maximize_window()
driver.implicitly_wait(5)
get_title = driver.title
print(get_title)
driver.implicitly_wait(4)
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")

for product in products:
    #productName = product.find_element(By.XPATH, "/div/h4/a").text
    productName = driver.find_element(By.XPATH,"//div[@class='card h-100']/div/h4/a").text
    if productName == "Blackberry":
        driver.find_element(By.CLASS_NAME, "btn-info").click()
print("Clicked on Blackberry and adding to Cart")

#driver.find_element(By.XPATH, "//a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CLASS_NAME, "btn-success").click()
driver.find_element(By.ID, "country").send_keys("ind")
#sleep(10)
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,"India").click()
sleep(5)
checkbox2 = driver.find_element(By.XPATH,"//input[@id='checkbox2']")
driver.execute_script("arguments[0].click();", checkbox2)
driver.find_element(By.XPATH,"//input[@type='submit']").click()
successMessage = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text

#assert successMessage == "Success! Thank you! Your order will be delivered in next few weeks :-)."
assert "Success! Thank you!" in successMessage
print("Order is placed Successfully")
