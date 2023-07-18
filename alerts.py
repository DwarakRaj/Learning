from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element("xpath", f"//input[@name='enter-name']").click()
sleep(5)
driver.find_element("xpath", f"//input[@name='enter-name']").send_keys("Dwarak")
sleep(5)
driver.find_element(By.ID,"alertbtn").click()
sleep(5)
alertsofjava = driver.switch_to.alert
print(alertsofjava)
sleep(2)
alertsofjava.accept()
print("Alert handled successfully")




