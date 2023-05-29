import time
from selenium import webdriver

url = 'https://tw.yahoo.com/'

driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

driver.get(url)

for i in range(0, 10):
    print(i)	# 0~9
    time.sleep(1)

driver.close()  #關閉瀏覽器




