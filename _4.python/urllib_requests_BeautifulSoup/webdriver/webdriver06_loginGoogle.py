url = 'http://www.google.com'
#url = 'https://www.gmail.com'
mail_address = 'XXXXXXX'
password = 'XXXXXXX'

import time
from selenium import webdriver

#driver = webdriver.Firefox();
driver = webdriver.Chrome()

driver.maximize_window()    #全螢幕顯示

driver.get(url)

driver.find_element('name', 'gb_70').click()  # 按右上角的 登入 鈕

driver.find_element('name', 'identifierId').send_keys(mail_address) # 輸入 帳號

time.sleep(2)  # 必須加入等待，否則會有誤動作

driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()  # 按 繼續 鈕
time.sleep(2)  # 必須加入等待，否則會有誤動作  

driver.find_element_by_xpath("//input[@type='password']").send_keys(password)  # 輸入 密碼
time.sleep(2)  # 必須加入等待，否則會有誤動作

driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()  # 按 繼續 鈕  
time.sleep(3)  # 必須加入等待，否則會有誤動作

