from selenium import webdriver
import time
url = "https://hophd.wordpress.com"
web = webdriver.Chrome("chromedriver.exe")
web.implicitly_wait(60)
web.get(url)
web.set_window_position(0, 0)
time.sleep(10)
web.quit()


