from selenium import webdriver
# 設定facebook登入資訊
url = 'https://www.facebook.com/'
email='你的faceook電子郵件'
password='你的faceook密碼'

# 取消 Alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# 建立瀏覽器物件
driver = webdriver.Chrome(chrome_options=chrome_options)
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)

# 執行自動登入動作
driver.find_element_by_id('email').send_keys(email)  #輸入郵件
driver.find_element_by_id('pass').send_keys(password)#輸入密碼
driver.find_element_by_name('login').click()         # 按登入鈕