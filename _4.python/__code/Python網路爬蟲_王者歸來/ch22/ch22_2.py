# ch22_2.py
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 搜尋條件
city = "台北市" 
checkin_time = "2019-11-24" 
checkout_time = "2019-11-25"       
# 網址處理
url = "https://tw.hotels.com/"
# 擷取網頁
driverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(executable_path=driverPath)
browser.implicitly_wait(10)                                 # 等待網頁載入
browser.get(url)                                            # 網頁下載至瀏覽器  
time.sleep(3)
searchNode = browser.find_elements_by_xpath("//input[contains(@id,'q-destination')]")
checkInNode = browser.find_elements_by_xpath("//input[contains(@id,'q-localised-check-in')]")
checkOutNode = browser.find_elements_by_xpath("//input[contains(@id,'q-localised-check-out')]")

# 輸入搜尋關鍵資料
searchNode[0].clear()                                       # 清除城市欄位
searchNode[0].send_keys(city)                               # 輸入搜尋城市
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)                           # 按Tab跳到check in欄位
checkInNode[0].clear()                                      # 清除check in欄位                                          
checkInNode[0].send_keys(checkin_time)                      # 輸入check in時間
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)                           # 按Tab跳至check out欄位
checkOutNode[0].clear()                                     # 清除check out欄位
checkOutNode[0].send_keys(checkout_time)                    # 輸入check out時間
time.sleep(3)
checkOutNode[0].send_keys(Keys.ENTER)                       # 表單按Enter表示輸入完成        
time.sleep(3)

# 旅館名稱
hotelPath = "//ol[@class='listings infinite-scroll-enabled']//h3/a"
names = browser.find_elements_by_xpath(hotelPath)
# 旅館地址
addressPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='address']"
addresses = browser.find_elements_by_xpath(addressPath)
# 旅館星級評價
starPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='star-rating-text']"
stars = browser.find_elements_by_xpath(starPath)
# 旅館定價
listingpricePath = "//ol[@class='listings infinite-scroll-enabled']//del[@data-reason='DRR-448']"
lprices = browser.find_elements_by_xpath(listingpricePath)
# 計算旅館數量
num = len(names)
print('旅館數量 : ', num)
print('-' * 70)
# 列出系列旅館資訊
for name,address,star,lprice in zip(names,addresses,stars,lprices):
    print('旅館名稱 : ', name.text) 
    print('旅館地址 : ', address.text)
    print('旅館星級 : ', star.text)
    print('旅館定價 : ', lprice.text)
    print('-' * 70)
    time.sleep(1)
    
