#把自己偽裝成一個瀏覽器

import time
from selenium import webdriver

from bs4 import BeautifulSoup

url = 'https://www.google.com.tw/'

web = webdriver.Chrome()    #使用Chrome
#web = webdriver.Firefox()   #使用Firefox
web.set_window_position(0,0)
web.set_window_size(800,600)

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
html = web.page_source
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


'''
from selenium import webdriver

# 設定facebook登入資訊
url = 'https://www.facebook.com/'
email='你的faceook電子郵件'
password='你的faceook密碼'
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()  #視窗最大化
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id('email').send_keys(email) #輸入郵件
driver.find_element_by_id('pass').send_keys(password)#輸入密碼
driver.find_element_by_id('loginbutton').click()    # 按登入鈕
'''



