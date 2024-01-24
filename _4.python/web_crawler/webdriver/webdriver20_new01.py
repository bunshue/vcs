#url = 'https://example.oxxostudio.tw/python/selenium/demo.html'
url = 'C:/_git/vcs/_1.data/______test_files1/webdriver_data.html'

'''
新進測試

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

print('------------------------------------------------------------')	#60個

#PyAutoGUI，自動控制滑鼠與鍵盤
import pyautogui as auto

'''
url = 'https://www.google.com/'
driver.get(url)  #開啟網址
time.sleep(3)


txt = driver.find_element(By.NAME, 'q')             # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys('this is a lion-mouse')
time.sleep(2)

print(txt.tag_name)
print(txt.get_attribute("type"))
print(txt.get_attribute("id"))


txt.submit()    #就是按了enter
'''

#url = 'https://tw.yahoo.com/'
driver.get(url)  #開啟網址
time.sleep(1)

auto.PAUSE = 1

x_st = 60
y_st = 140
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
auto.typewrite("獅子")
auto.click()

x_st = 60
y_st = 200
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)

print('------------------------------------------------------------')	#60個
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



