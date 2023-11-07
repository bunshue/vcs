from selenium import webdriver  # 匯入 selenium 的 webdriver
from time import sleep          # 匯入內建的 time 模組的 sleep() 函式

opt =  webdriver.ChromeOptions()      #建立選項物件
opt.add_experimental_option('prefs',  #加入「禁止顯示訊息框」的選項
    {'profile.default_content_setting_values': {'notifications' : 2}})
browser = webdriver.Chrome(options = opt) #以 options 參數來建立瀏覽器物件

browser.get('http://www.google.com')    #←開啟 Chrome 並連到 Google 網站
browser.maximize_window()  #←將視窗最大化以避免最右邊的登入鈕沒顯示出來

browser.find_element_by_id('gb_70').click()   #←按登入鈕
sleep(3)       #←暫停 3 秒等待進入下一頁
browser.find_element_by_id('identifierId').send_keys('您的帳號') #}←輸入帳號
browser.find_element_by_id('identifierNext').click()   #←按繼續鈕
sleep(3)       #←暫停 3 秒等待進入下一頁
browser.find_element_by_name('password').send_keys('您的密碼')  #←輸入帳密
browser.find_element_by_id('passwordNext').click()   #←按繼續鈕

