from selenium import webdriver
from time import sleep

urls = ['http://www.google.com',
        'http://www.e-happy.com.tw',
        'https://www.ruten.com.tw/',
        'https://tw.yahoo.com/']

driver = webdriver.Chrome()
driver.maximize_window()

for url in urls:
    driver.get(url) 
    sleep(3)

driver.close()
