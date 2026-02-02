# ch7_7_6.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'd:\Web_Crawler\ch7\h7_3.html'
browser.get(url)                # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//h1/em")
print('em          : ', n1.text)
n2 = browser.find_element_by_xpath("//h1")
print('h1          : ', n2.text)
n3 = browser.find_element_by_xpath("//h1")
print('textContent : ', n3.get_attribute('textContent'))
n4 = browser.find_element_by_xpath("//h1")
print('innerHTML : ', n4.get_attribute('innerHTML'))
n5 = browser.find_element_by_xpath("//h1")
print('outerHTML : ', n5.get_attribute('outerHTML'))
