from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--incognito")
driver.get("https://www.flipkart.com/")
driver.maximize_window()
get_title = driver.title
print(get_title)
sleep(10)

try:
    driver.find_element("xpath", f"//button[@class='_2KpZ6l _2doB4z']").click()
except Exception as e:
    print ("No Such Element Exception")
    print('Reason: ', e)
sleep(5)

# mainmenu = driver.find_elements("xpath",f"//div[@class='xtXmba']")
# for menu in mainmenu:
#     print(menu.text)
#     sleep(1)

driver.find_element(By.XPATH,"//input[@name='q']").click()
sleep(5)
driver.find_element(By.XPATH,"//input[@name='q']" ).send_keys("Mobile")
sleep(5)
driver.find_element("xpath", f"//button[@type='submit']").click()
sleep(5)


mobiles = driver.find_elements("xpath",f"//div[@class='_4rR01T']")
for mobile in mobiles:
    prices = driver.find_element("xpath", f"//div[contains(text(),'{mobile.text}')]/parent::div[@class='col col-7-12']/following-sibling::div[@class='col col-5-12 nlI3QM']/descendant::div[@class='_30jeq3 _1_WHN1']")
    print(mobile.text, " available in Flipkart for ", prices.text)











