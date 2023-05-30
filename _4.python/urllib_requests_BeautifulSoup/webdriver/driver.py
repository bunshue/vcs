from selenium import webdriver
import time

# 開啟下載的chromedriver
driver = webdriver.Chrome("./chromedriver")

# 等待10秒
time.sleep(10)

driver.quit()   #關閉瀏覽器並且退出驅動程序
