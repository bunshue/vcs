import time
from selenium import webdriver

url = 'https://irs.thsrc.com.tw/IMINT'		#台灣高鐵訂票系統

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

driver.get(url)
driver.find_element_by_id("btn-confirm").click()
time.sleep(0.3)
driver.save_screenshot("wholepage.png")

#driver.close()  #關閉瀏覽器


