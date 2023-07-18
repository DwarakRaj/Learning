from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(5)
get_title = driver.title
print(get_title)
driver.find_element("xpath", f"//input[@type='search']").send_keys("ber")
sleep(5)
static_berries = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg']
dy_berries = []

dynamic_berries = driver.find_elements(By.XPATH,"//h4[@class='product-name']")
for berry in dynamic_berries:
    print(berry.text)
    dy_berries.append(berry.text)
print(static_berries)
print(dy_berries)
assert static_berries == dy_berries
print("Berries are Verified")
sleep(5)
driver.find_element("xpath",f"//button[@type='submit']").click()
sleep(5)
addtocart = driver.find_elements("xpath",f"//div[@class='product']/descendant::button[contains(text(),'ADD TO CART')]")
print(len(addtocart))

for add in addtocart:
    add.click()
    print(add.text)
print("Items added to cart")
sleep(5)
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element("xpath",f"//div[@class='action-block']/button[contains(text(),'PROCEED TO CHECKOUT')]").click()
sleep(5)
driver.find_element("xpath",f"//input[@type='text']").send_keys("rahulshettyacademy")
driver.find_element("xpath",f"//button[@class='promoBtn']").click()
#sleep(10)
#<!--- Explicit wait --!>
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promocode = driver.find_element("xpath","//span[@class='promoInfo']")
print(promocode.text)
assert driver.find_element("xpath","//span[@class='promoInfo']").is_displayed()
print("Code applied successfully")

#assertion
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == totalAmount
print("The total amount is verified")

#assignment - compare - discount should always be lesser than the actual amount if discount applied
discountamount = float(driver.find_element(By.XPATH, "//span[@class='discountAmt']").text)

while promocode.is_displayed():
    if discountamount < totalAmount:
        break
print("Discount is applied")
print("Discount is verified")

#### Assignment get list of berries and compare it whith dynamically loaded list





