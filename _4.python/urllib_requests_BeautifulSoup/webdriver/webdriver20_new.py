'''
新進測試

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
#driver.maximize_window()    #全螢幕顯示

url = 'https://www.google.com/'
driver.get(url)  #開啟網址












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



