from selenium import webdriver
from time import sleep

url = 'https://www.books.com.tw/web/books'
#url = 'https://www.google.com/

# 建立瀏覽器物件
#driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()   #使用Firefox

driver.maximize_window()
driver.get(url)
sleep(2)  #加入等待
driver.find_element_by_id('key').send_keys('文淵閣工作室') #輸入搜尋文字
sleep(2)
driver.find_element_by_xpath('//*[@id="search"]/button').click()  #按 搜尋 鈕

print('完成')

