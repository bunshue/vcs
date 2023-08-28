from selenium import webdriver
from time import sleep

url = 'https://www.books.com.tw/web/books'

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
sleep(2)  #加入等待
driver.find_element_by_id('key').send_keys('文淵閣工作室') #輸入搜尋文字
sleep(2)
driver.find_element_by_xpath('//*[@id="search"]/button').click()  #按 搜尋 鈕
