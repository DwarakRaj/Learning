from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market")
sleep(10)

niftycom = []

names = driver.find_elements("xpath", f"//table[@id='livePreTable']/descendant::tr/td/a[@class='symbol-word-break']")

    

for name in names:
    print(name.text,end='-')
    niftycom.append(name.text)
    comp_share_price = driver.find_element("xpath", f"//a[text()='{name.text}']/../..//td[7]")
    print(comp_share_price.text)

print("------------------------------")
print((niftycom))
print("------------------Boss DwarakBoss------------")
# for niftyname in niftycom:
#     comp_share_price = driver.find_element("xpath", f"//a[text()='{niftyname}']/../..//td[7]")
#     print(comp_share_price.text)



################################# end of 1st example #######################################











