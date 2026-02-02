# ch7_7_4.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'd:\Web_Crawler\ch7\h7_1.html'
browser.get(url)                # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//section/p[@class='year']")
print(n1.text)
n1 = browser.find_element_by_xpath("//section/p[@class='price']")
print(n1.text)
