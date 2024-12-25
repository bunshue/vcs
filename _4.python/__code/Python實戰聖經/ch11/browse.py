from selenium import webdriver
import time

# 建立瀏覽器物件
#driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()   #使用Firefox

url = 'http://www.e-happy.com.tw'
url = 'https://www.google.com/'

driver.get(url)
driver.maximize_window()
print('目前網址：', driver.current_url)
print('瀏覽器尺寸：', driver.get_window_size())
print('網頁原始碼：\n', driver.page_source)

time.sleep(2)
driver.quit()

print('完成')
