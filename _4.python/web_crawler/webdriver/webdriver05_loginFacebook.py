#登入 facebook

import time
from selenium import webdriver

# 會出現 Alert 視窗
url = 'https://www.facebook.com/'
email = '您的 Email 帳號'
password = '您的密碼'
driver = webdriver.Chrome()

# 取消 Alert
url = 'https://www.facebook.com/'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)

# 設定facebook登入資訊
url = 'https://www.facebook.com/'
email = '你的faceook電子郵件'
password = '你的faceook密碼'

# 建立瀏覽器物件
driver = webdriver.Chrome(chrome_options = chrome_options)
#driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

driver.get(url)

# 執行自動登入動作
driver.find_element_by_id('email').clear()
driver.find_element_by_id('email').send_keys(email)

time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_id('pass').clear()
driver.find_element_by_id('pass').send_keys(password)

driver.find_element_by_id('loginbutton').click()  # 按 登入 鈕

