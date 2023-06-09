#抓中央氣象局資料

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

url = 'https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID=menu'

driver.get(url)
time.sleep(1)

html = driver.page_source	#讀取網頁的原始碼
#print(html)
#driver.quit()   #關閉瀏覽器並且退出驅動程序

soup = BeautifulSoup(html, 'html.parser')
target = soup.select('#County option')
counties = list()
for item in target:
    counties.append((item.text,item['value']))
    
print(counties)

for c in counties:
    print(c)


print('----------------------------------------------------------------------')	#70個
print('完成')

'''
print('準備關閉瀏覽器')
for i in range(0, 10):
    print(i, '秒')	# 0~9
    time.sleep(1)

#print('關閉瀏覽器')
#driver.close()  #關閉瀏覽器

print('關閉瀏覽器並且退出驅動程序')
driver.quit()   #關閉瀏覽器並且退出驅動程序
'''




