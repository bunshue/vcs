from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.e-happy.com.tw')
driver.maximize_window()
print('目前網址：', driver.current_url)
print('瀏覽器尺寸：', driver.get_window_size())
print('網頁原始碼：\n', driver.page_source)

sleep(5)
driver.quit()