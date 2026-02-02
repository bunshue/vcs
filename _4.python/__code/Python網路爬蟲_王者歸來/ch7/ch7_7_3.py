# ch7_7_3.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'd:\Web_Crawler\ch7\h7_1.html'
browser.get(url)                # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath("//section/p[1]")
print(n1.text)
n2 = browser.find_element_by_xpath("//section/p[2]")
print(n1.text)
