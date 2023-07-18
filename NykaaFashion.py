from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.chrome()
driver.get("https://www.nykaafashion.com/")
driver.maximize_window()
sleep(5)

#######################hoverover over main maenu and print items ########################################

mainmenu = driver.find_elements("xpath", f"//span[@class='css-11uh70c']")
for menu in mainmenu:
    mousehoverMainmenu = driver.find_element("xpath", f"//div[@class='css-x63yaz']")
    sleep(2)
    print(menu.text)
    #mouseover
    a = ActionChains(driver)
    a.move_to_element(mousehoverMainmenu).perform()
    sleep(2)