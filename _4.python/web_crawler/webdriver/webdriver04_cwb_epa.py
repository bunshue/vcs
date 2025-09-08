print("抓 中央氣象局/環保署 資料")
print("------------------------------------------------------------")  # 60個
print("準備工作")

import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 建立瀏覽器物件
# driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()  # 使用Firefox
driver.set_window_position(0, 0)  # 設定視窗位置
driver.set_window_size(800, 600)  # 設定視窗大小
driver.maximize_window()  # 全螢幕顯示

print("------------------------------------------------------------")  # 60個
print("抓中央氣象局資料")
"""
url = 'https://www.cwa.gov.tw/V8/C/W/OBS_County.html?ID=menu'

driver.get(url)
time.sleep(1)

html = driver.page_source	#讀取網頁的原始碼
#print(html)


soup = BeautifulSoup(html, 'html.parser')
target = soup.select('#County option')
counties = list()
for item in target:
    counties.append((item.text,item['value']))
    
print(counties)

target = ""
for c in counties:
    #print(type(c))
    #print(c)
    #print(c[0], c[1])
    if c[0] == '新竹市':
        target = c[1]

if target != "":
    url = url.replace('menu', target)
    print(url)
    driver.get(url)
    time.sleep(1)

    html = driver.page_source	#讀取網頁的原始碼
    #print(html)
    #driver.quit()   #關閉瀏覽器並且退出驅動程序

    soup = BeautifulSoup(html, 'html.parser')
    

#print(counties)
#('新竹市', '10018')

driver.quit()   #關閉瀏覽器並且退出驅動程序

sys.exit()
"""
print("------------------------------------------------------------")  # 60個

print("抓環保署資料")

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://data.epa.gov.tw/"

# driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()  # 使用Firefox

driver.maximize_window()  # 全螢幕顯示

driver.get(url)

txt = driver.find_element(By.ID, "searchbar-input")  # 取得 id 為 xxxx 的網頁元素 ( TextArea )
txt.send_keys("aqi" + Keys.RETURN)  # 輸入 aqi 後按 Enter

time.sleep(1)  # 必須加入等待，否則會有誤動作

btn = driver.find_element_by_link_text("空氣品質指標(AQI)")
btn.click()  # 點選 空氣品質指標(AQI) 鈕
time.sleep(3)  # 必須加入等待，否則會有誤動作

btn = driver.find_element_by_link_text("JSON")
btn.click()  # 下載 JSON
time.sleep(3)  # 必須加入等待，否則會有誤動作

btn = driver.find_element_by_link_text("XML")
btn.click()  # 下載 XML
time.sleep(3)  # 必須加入等待，否則會有誤動作

btn = driver.find_element_by_link_text("CSV")
btn.click()  # 下載 CSV


driver.close()  # 關閉瀏覽器


"""
<input id="searchbar-input" accesskey="S" type="text" name="text"
placeholder="請輸入關鍵字搜尋，例如:環境或&quot;縣市(臺北市)小時值-每小時&quot;"
aria-label="請輸入關鍵字搜尋，例如:環境或&quot;縣市(臺北市)小時值-每小時&quot;"
value="" class="bpa-input" data-v-5e8e3ca1="">
"""


print("------------------------------------------------------------")  # 60個
print("完成")


sys.exit()


"""
print('準備關閉瀏覽器')
for i in range(0, 10):
    print(i, '秒')	# 0~9
    time.sleep(1)

#print('關閉瀏覽器')
#driver.close()  #關閉瀏覽器

print('關閉瀏覽器並且退出驅動程序')
driver.quit()   #關閉瀏覽器並且退出驅動程序
"""
