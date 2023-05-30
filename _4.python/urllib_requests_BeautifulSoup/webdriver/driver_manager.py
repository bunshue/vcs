from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(ChromeDriverManager().install())

# 等待10秒
time.sleep(10)

driver.quit()   #關閉瀏覽器並且退出驅動程序
