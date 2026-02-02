# ch21_2.py
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

# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = browser.find_elements_by_xpath(titlePath)

# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = browser.find_elements_by_xpath(pricePath)

# 計算商品數量
num = len(product_titles)
print('商品數量 : ', num)
print('-' * 50)

# 列出商品資訊
for title, link, price in zip(product_titles, product_links, product_prices):
    print('商品名稱 : ', title.get_attribute('textContent'))
    print('商品連結 : ', link.get_attribute('href'))
    print('商品價格 : ', price.text)
    print('-' * 70)



