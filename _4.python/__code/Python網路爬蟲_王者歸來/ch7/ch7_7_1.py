# ch7_7_1.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'd:\Web_Crawler\ch7\h7_1.html'
browser.get(url)                # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath('//h4')
print(n1.text)
n2 = browser.find_element_by_xpath('//body/section/h4')
print(n2.text)
n3 = browser.find_element_by_xpath('//section/h4')
print(n3.text)
n4 = browser.find_element_by_xpath('//body/*/h4')
print(n4.text)            

