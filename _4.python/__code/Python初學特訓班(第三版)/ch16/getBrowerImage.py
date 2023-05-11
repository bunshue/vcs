from selenium import webdriver
from time import sleep

url="http://irs.thsrc.com.tw/IMINT"
driver=webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.find_element_by_id("btn-confirm").click()
sleep(0.3)
driver.save_screenshot("wholepage.png")
