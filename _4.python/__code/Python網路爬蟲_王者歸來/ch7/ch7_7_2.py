# ch7_7_2.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'd:\Web_Crawler\ch7\h7_1.html'
browser.get(url)                # 網頁下載至瀏覽器

n1 = browser.find_element_by_xpath('//p')
print(n1.text)

