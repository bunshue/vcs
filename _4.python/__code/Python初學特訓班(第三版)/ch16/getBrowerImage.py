import time
from selenium import webdriver

url = "http://irs.thsrc.com.tw/IMINT"
driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()    #���ù����

driver.find_element_by_id("btn-confirm").click()

time.sleep(0.3)

driver.save_screenshot("wholepage.png")
