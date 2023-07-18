from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.pepperfry.com/")
driver.maximize_window()
get_title = driver.title
print(get_title)
sleep(10)
#switch to frame
driver.switch_to.frame("webklipper-publisher-widget-container-notification-frame")
sleep(5)
driver.find_element("xpath",f"//div[@class='container']/descendant::i[@class='wewidgeticon we_close']").click()
sleep(2)

############################################# 1. Print menu, sub-menu & categories ################################################################################
# mainmenuprint = driver.find_elements("xpath", f"//ul[@class='hd-menu-main-list-container']/descendant::a")
# for menu in mainmenuprint:
#     mousehoverMainmenu = driver.find_element("xpath", f"//ul[@class='hd-menu-main-list-container']/descendant::a[contains(text(),'{menu.text}')]")
#     sleep(2)
#     print(menu.text)
#     #mouseover
#     a = ActionChains(driver)
#     a.move_to_element(mousehoverMainmenu).perform()
#     sleep(2)
#
#     submenu = driver.find_elements("xpath", f"//a[@class='hd-menu-category-link ng-star-inserted']")
#     for menunames in submenu:
#         print(menunames.text)
#         subcategories = driver.find_elements("xpath", f"//a[text()='{menunames.text} ']/parent::li/following-sibling::li/a")
#         for subitems in subcategories:
#             print(subitems.text)
############################################## 2. Print the title and price of 1st item, 3 seater sofa - 40 elements #############################################################################
# titlebar = driver.find_elements("xpath", f"//div[@class='product-card']/descendant::div/h3")
# for title in titlebar:
#     prices=driver.find_element("xpath", f"//div[@class='product-card']/descendant::div/h3[contains(text(),'{title.text}')]/parent::div[@class='marginBottom-4']/following-sibling::div[@class='product-price']/span")
#     print("Cost of ", title.text, "is Rs.", prices.text)

############################################ 3. Click particular element, Compare PLP and PDP title and cost ###################################################################

#click on first menu
driver.find_element("xpath", f"//ul[@class='hd-menu-main-list-container']/descendant::a").click()
sleep(2)
driver.find_element("xpath", f"(//div[@class='hd-menu-main-category hd-hover-col ng-star-inserted']/ul/li)[2]").click()
sleep(2)

plppage = driver.current_window_handle
#plpaddress = str(plppage)
elementname = driver.find_element("xpath", f"(//div[@class='marginBottom-4']/h3)[1]")
elementprice = driver.find_element("xpath", f"//div[@class='product-card']/descendant::div/h3[contains(text(),'{elementname.text}')]/parent::div[@class='marginBottom-4']/following-sibling::div[@class='product-price']/span")
var_elementtext = elementname.text
print(elementname.text)
print(elementprice.text)
print(var_elementtext)
print(plppage)
driver.execute_script("arguments[0].click();", elementname)
#elementname.click()
sleep(5)

pdppage = driver.window_handles
for handles in pdppage:
    if handles != plppage:
        driver.switch_to.window(handles)
pdpelement = driver.find_element("xpath",f"//div[@class='vip-product-name text-lg font-medium marginBottom-4']/h1")
arrangedpdp = pdpelement.text
newValue=arrangedpdp.replace(',','')
pdpelementprice = driver.find_element("xpath","//span[@class='text-xxl font-bold ng-tns-c155-1']")
print(newValue)
print(pdpelementprice.text)
#print(elementname.text)
print(type(pdpelementprice))
print(var_elementtext)
print(elementprice == pdpelementprice)
print(var_elementtext == newValue)
if  (var_elementtext == newValue) or (elementprice == pdpelementprice):
    print("Elements are  same")
else:
    print("The elements are not same")

#############################################################################################################################################

