# ch7_7_5.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
url = 'd:\Web_Crawler\ch7\h7_2.html'
browser.get(url)                # 網頁下載至瀏覽器

pict = browser.find_element_by_xpath("//section/img")
print(pict.get_attribute('src'))

