from selenium import webdriver

# 會出現 Alert 視窗
url = 'https://www.facebook.com/'
email='您的 Email 帳號'
password='您的密碼'
driver = webdriver.Chrome()

# 取消 Alert 視窗
#url = 'https://www.facebook.com/'
#chrome_options = webdriver.ChromeOptions()
#prefs = {"profile.default_content_setting_values.notifications" : 2}
#chrome_options.add_experimental_option("prefs",prefs)
#driver = webdriver.Chrome(chrome_options=chrome_options)

driver.maximize_window()
driver.get(url)

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()  # 按 登入 鈕

#driver.quit()