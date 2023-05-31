url = 'http://www.google.com'
#url = 'https://www.gmail.com'
mail_address = 'XXXXXXX'
password = 'XXXXXXX'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 建立瀏覽器物件
#driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
#driver.maximize_window()    #全螢幕顯示

driver.get(url)

driver.find_element(By.CLASS_NAME, 'gb_Md').click()  # 按右上角的 登入 鈕


driver.find_element(By.NAME, 'identifier').send_keys(mail_address) # 輸入 帳號

time.sleep(2)  # 必須加入等待，否則會有誤動作

driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()  # 按 下一步 鈕

time.sleep(2)  # 必須加入等待，否則會有誤動作  

'''
driver.find_element_by_xpath("//input[@type='password']").send_keys(password)  # 輸入 密碼
time.sleep(2)  # 必須加入等待，否則會有誤動作

driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()  # 按 繼續 鈕  
time.sleep(3)  # 必須加入等待，否則會有誤動作
'''

