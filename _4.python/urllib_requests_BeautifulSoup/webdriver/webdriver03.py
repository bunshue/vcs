#登入 facebook

import time
from selenium import webdriver

# 會出現 Alert 視窗
url = 'https://www.facebook.com/'
email = '您的 Email 帳號'
password = '您的密碼'

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

# 取消 Alert 視窗
#url = 'https://www.facebook.com/'
#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(url)

# 執行自動登入動作
driver.find_element_by_id('email').clear()
driver.find_element_by_id('email').send_keys(email)

time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_id('pass').clear()
driver.find_element_by_id('pass').send_keys(password)

driver.find_element_by_id('loginbutton').click()  # 按 登入 鈕

#driver.quit()   #關閉瀏覽器並且退出驅動程序

# 設定facebook登入資訊
url = 'https://www.facebook.com/'
email = '你的faceook電子郵件'
password = '你的faceook密碼'

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

driver.get(url)

# 執行自動登入動作
driver.find_element_by_id('email').clear()
driver.find_element_by_id('email').send_keys(email) #輸入郵件

time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_id('pass').clear()
driver.find_element_by_id('pass').send_keys(password)#輸入密碼

driver.find_element_by_id('loginbutton').click()    # 按登入鈕




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



