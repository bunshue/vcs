import time
from selenium import webdriver

#url lost
url = 'http://drho.tw/news'

web = webdriver.Firefox()
web.get(url)
for i in range(1,9):
    web.find_element_by_id('btn{}'.format(i)).click()
    time.sleep(5)
web.quit()
