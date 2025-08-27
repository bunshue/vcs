#url = 'https://example.oxxostudio.tw/python/selenium/demo.html'
url = 'D:/_git/vcs/_1.data/______test_files1/webdriver_data_old.html'

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
#driver.maximize_window()    #全螢幕顯示

driver.get(url)  # 開啟網址

txt = driver.find_element(By.ID, 'show')            # 取得 id 為 show 的網頁元素 ( TextArea )
a = driver.find_element(By.ID, 'aaa')               # 取得 id 為 aaa 的網頁元素 ( 按鈕 AAA )
b = driver.find_element(By.NAME, 'bbb')             # 取得屬性 name 為 bbb 的網頁元素 ( 按鈕 BBB )
c = driver.find_element(By.CLASS_NAME, 'ccc')       # 取得 class 為 ccc 的網頁元素 ( 按鈕 CCC )
d = driver.find_element(By.CSS_SELECTOR, '.ddd')    # 取得 class 為 ddd 的網頁元素 ( 按鈕 DDD ), 多一個.
h1 = driver.find_element(By.TAG_NAME, 'h1')         # 取得 tag h1 的網頁元素
link1 = driver.find_element(By.LINK_TEXT, '點擊開啟 Google 網站')  # 取得指定超連結文字的網頁元素
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Google') # 取得超連結文字包含 Google 的網頁元素
select = Select(driver.find_element(By.XPATH, '/html/body/select'))   # 取得 html > body > select 這個網頁元素
print('輸入文字')
txt.send_keys('在TextArea輸入一些文字');
print(txt.text)    # 印出 txt 元素的內容
time.sleep(5)

print('點擊 AAA')
a.click()        # 點擊 a
print(a.text)    # 印出 a 元素的內容
time.sleep(3)

print('點擊 BBB')
b.click()        # 點擊 b
print(b.text)    # 印出 b 元素的內容
time.sleep(3)

print('點擊 CCC')
c.click()        # 點擊 c
print(c.text)    # 印出 c 元素的內容
time.sleep(3)

print('點擊 DDD')
d.click()        # 點擊 d
print(d.text)    # 印出 d 元素的內容
time.sleep(3)

print('下拉式選單')
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
time.sleep(3)

print('點擊 h1')
h1.click()       # 點擊 h1
time.sleep(3)

print('點擊 link1')
link1.click()    # 點擊 link1
time.sleep(3)

print('點擊 link2')
link2.click()    # 點擊 link2
print(link2.get_attribute('href'))   # 印出 link2 元素的 href 屬性
time.sleep(3)

print('完成')
