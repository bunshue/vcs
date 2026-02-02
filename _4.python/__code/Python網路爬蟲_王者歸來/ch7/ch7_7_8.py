# ch7_7_8.py
from selenium import webdriver

driverPath = 'D:\geckodriver\chromedriver.exe'
headless = webdriver.ChromeOptions()
headless.add_argument('headless')   # 隱藏參數
browser = webdriver.Chrome(executable_path=driverPath, options=headless)
url = 'd:\Web_Crawler\ch7\h7_4.html'
browser.implicitly_wait(5)          # 等待網頁載入
browser.get(url)                    # 網頁下載至瀏覽器

n = browser.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute('outerHTML'))
print(n.get_attribute('href'))






