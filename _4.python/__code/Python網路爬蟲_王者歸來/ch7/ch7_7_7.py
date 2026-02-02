# ch7_7_7.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'd:\Web_Crawler\ch7\h7_4.html'
browser.get(url)                # 網頁下載至瀏覽器

n = browser.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute('outerHTML'))
print(n.get_attribute('href'))






