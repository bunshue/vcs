#把自己偽裝成一個瀏覽器

import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.google.com.tw/'

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

driver.get(url)

driver.save_screenshot('screenshot.png')  #存圖

for i in range(0, 10):
    print(i)	# 0~9
    time.sleep(1)

driver.quit()   #關閉瀏覽器並且退出驅動程序

'''
driver.find_element_by_id('topbar__user__login').click()
driver.find_element_by_name('username').clear()
driver.find_element_by_name('username').send_keys('your account')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('your password')
driver.find_element_by_id('login-send').click()
'''
'''
for i in range(1,9):
    result = driver.find_element_by_id('btn{}'.format(i)).click()
    print(result)
    time.sleep(5)
driver.quit()   #關閉瀏覽器並且退出驅動程序
'''

'''
url = 'https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID=menu'

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(60)
driver.get(url)

html = driver.page_source	#讀取網頁的原始碼
#print(html)
driver.quit()   #關閉瀏覽器並且退出驅動程序

soup = BeautifulSoup(html, 'html.parser')
target = soup.select('#County option')
counties = list()
for item in target:
    counties.append((item.text,item['value']))
    
print(counties)

for c in counties:
    print(c)

'''




