from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# 你的資訊
url = "https://www.facebook.com/"
email = "YOUR EMAIL"
password = "YOUR PASSWORD"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    ChromeDriverManager().install())

driver.maximize_window()    #全螢幕顯示

# 進入Facebook登入畫面
driver.get(url)

# 填入帳號密碼，並送出
driver.find_element_by_id("email").send_keys(email)
driver.find_element_by_id("pass").send_keys(password)
driver.find_element_by_name("login").click()

# 等待10秒
time.sleep(10)

driver.quit()   #關閉瀏覽器並且退出驅動程序
