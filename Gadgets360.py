from selenium import webdriver


from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.gadgets360.com/")
driver.maximize_window()
get_title = driver.title
print(get_title)
sleep(10)

driver.find_element("xpath", f"//div[@class='web_dialog web_dialognotify web_dialogproduct animated bounceInRight']").click()
driver.find_element("xpath",f"//button[@id='btnClosenotify']").click()

