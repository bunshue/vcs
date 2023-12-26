# ch24_3.py
from selenium import webdriver

dirverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(dirverPath)
print(type(browser))


