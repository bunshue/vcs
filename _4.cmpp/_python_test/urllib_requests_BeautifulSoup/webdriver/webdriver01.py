#把自己偽裝成一個瀏覽器

import time
from selenium import webdriver
from bs4 import BeautifulSoup

url = 'https://www.google.com.tw/'

web = webdriver.Chrome()    #使用Chrome
#web = webdriver.Firefox()   #使用Firefox
web.set_window_position(0,0)	#設定視窗位置
web.set_window_size(800,600)	#設定視窗大小

web.get(url)
web.save_screenshot('screenshot.png')  #存圖

time.sleep(10)

web.quit()

'''
web.find_element_by_id('topbar__user__login').click()
web.find_element_by_name('username').clear()
web.find_element_by_name('username').send_keys('your account')
web.find_element_by_name('password').clear()
web.find_element_by_name('password').send_keys('your password')
web.find_element_by_id('login-send').click()
'''
'''
for i in range(1,9):
    result = web.find_element_by_id('btn{}'.format(i)).click()
    print(result)
    time.sleep(5)
web.quit()
'''

'''
url = 'https://www.cwb.gov.tw/V8/C/W/OBS_County.html?ID=menu'

web = webdriver.Chrome('chromedriver.exe')
web.implicitly_wait(60)
web.get(url)
html = web.page_source	#讀取網頁的原始碼
#web.quit()
#print(html)
web.quit()

soup = BeautifulSoup(html, 'html.parser')
target = soup.select('#County option')
counties = list()
for item in target:
    counties.append((item.text,item['value']))
    
print(counties)

for c in counties:
    print(c)

'''




