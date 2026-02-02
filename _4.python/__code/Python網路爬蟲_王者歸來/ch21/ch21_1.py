# ch21_1.py
from selenium import webdriver

# 網址處理
url_yahoo = 'https://tw.bid.yahoo.com/search/auction/product?'
url_product = 'kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime'
url = url_yahoo + url_product
# 擷取網頁
driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
browser.implicitly_wait(5)          # 等待網頁載入
browser.get(url)                    # 網頁下載至瀏覽器
# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
product_links = browser.find_elements_by_xpath(linkPath)
product_link = product_links[0].get_attribute('href')
print('商品連結 : ', product_link)
# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = browser.find_elements_by_xpath(titlePath)
product_title = product_titles[0].get_attribute('textContent')
print('商品名稱 : ', product_title)
# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = browser.find_elements_by_xpath(pricePath)
product_price = product_prices[0].text
print('商品價格 : ', product_price)





