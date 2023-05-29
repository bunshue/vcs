import time
from selenium import webdriver

# 會出現 Alert 視窗
#url = 'https://www.facebook.com/'
#driver = webdriver.Chrome()

# 取消 Alert
url = 'https://www.facebook.com/'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options = chrome_options)

driver.maximize_window()    #全螢幕顯示

driver.get(url)

driver.find_element_by_id('email').clear()
driver.find_element_by_id('email').send_keys('您的 Email 帳號')
time.sleep(3)  # 必須加入等待，否則會有誤動作

driver.find_element_by_id('pass').clear()
driver.find_element_by_id('pass').send_keys('您的密碼')

driver.find_element_by_id('loginbutton').click()  # 按 登入 鈕
