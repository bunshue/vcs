from selenium import webdriver  # 匯入 selenium 的 webdriver

opt = webdriver.ChromeOptions()  # ←建立選項物件
opt.add_experimental_option('prefs',  # ←在選項物件中加入「禁止顯示訊息框」的選項
                            {'profile.default_content_setting_values': {'notifications': 2}})
browser = webdriver.Chrome(options=opt)  # ←以 options 指名參數來建立瀏覽器物件

browser.get('http://www.facebook.com')  # ←開啟 Chrome 並連到 fb 網站
browser.find_element_by_id('email').send_keys('您的帳號')  # }
browser.find_element_by_id('pass').send_keys('您的密碼')  # }輸入帳密並按登入鈕
browser.find_element_by_name('login').click()  # }
