import sys
import requests

print('------------------------------------------------------------')	#60個

r = requests.get('http://www.flag.com.tw') # 向旗標網站發出 GET 請求,並將回應物件儲存到 r

if r.status_code == 200:   # 回應的狀態碼若為 200 表示 OK
    print(r.text)          # 將回應的文字(網頁原始碼)印出來
else:
    print(r.status_code, r.reason) # 若發生錯誤(狀態碼不是 200), 則印出狀態碼及錯誤原因
    
print('------------------------------------------------------------')	#60個

url = 'https://httpbin.org/get'
hd = {'user-key': '7ADGS9S'}  # 標頭參數(以字典儲存)
pm = {'id': 1023, 'neme': 'joe'}   # 網址參數(以字典儲存)
r = requests.get(url, headers = hd, params = pm)   # 加入 headers 及 params 參數
print(r.text)   # 將回應的文字印出來

print('------------------------------------------------------------')	#60個

url = 'http://httpbin.org/post' # 使用測試服務網站, POST 方法網址要加 /post
r = requests.post(url, data = 'Hello')  # 送出字串資料
print(r.text)
r = requests.post(url, data = {'id':'123', 'name':'Joe'})
print(r.text)

print('------------------------------------------------------------')	#60個

r = requests.put('https://httpbin.org/put', data = {'key':'abc'})
print(r.text)
r = requests.patch('https://httpbin.org/patch', data = {'key':'xyz'})
print(r.text)
r = requests.delete('https://httpbin.org/delete')
print(r.text)

print('------------------------------------------------------------')	#60個

page = """
<html>
  <head><title>旗標科技</title></head>
  <body>
    <div class="section" id="main">
      <img alt="旗標圖示" src="https://zh.wikipedia.org/static/images/icons/wikdddipedia.png">
      <p>產品類別</p>
      <button id="books"><h4 class="bk">圖書</h4></button>
      <button id="maker"><h4 class="pk">創客</h4></button>
      <button id="teach"><h4 class="pk">教具</h4></button>
    </div>
    <div class="section" id="footer">
      <p>杭州南路一段15-1號19樓</p>
      <a href="http://flag.tw/contact">聯絡我們</a>
    </div>
  </body>
</html>
"""

from bs4 import BeautifulSoup
bs = BeautifulSoup(page, 'lxml')

print(bs.title)
print(bs.a)

print(bs.a.text)
print(bs.a.get('href'))
print(bs.a['href'])

print(bs.find('h4'))
print(bs.find('h4', {'class': 'pk'}))
print(bs.find('h4').text)

print(bs.find_all('h4'))
print(bs.find_all('h4', {'class': 'pk'}))

print(bs.find_all(['title', 'p']))
print(bs.find_all(['title', 'p'])[1].text)  #← 傳回第 1 個 (由 0 算起) 符合標籤中的文字

print('h4:', bs.select('h4'))         #←查詢所有 h4 標籤
print('#book:', bs.select('#books'))  #←查詢所有 id 為 'books' 的標籤
print('.pk:', bs.select('.pk'))       #←查詢所有 class 為 'pk' 的標籤
print('h4.bk', bs.select('h4.bk'))    #←查詢所有 class 為 'bk' 的 h4 標籤

print(bs.select('#main button .pk'))

print(bs.select('#main button .pk')[1].text)
print(bs.select('#footer a')[0]['href'])




print('------------------------------------------------------------')	#60個


import re # 使用前要先匯入 re 模組
print(re.match (r'pyt', 'python')) # pyt 由開頭即符合, 因此成功
print(re.match (r'yth', 'python')) # yth 與開頭不符合, 因此失敗
print(re.search(r'yth', 'python')) # seach( ) 不限開頭, 因此成功


print('------------------------------------------------------------')	#60個


import re

m = re.search(r'p[a-z]+e', 'apples')
print(m)   # 輸出 <_sre.SRE_Match object; span=(1, 5), match='pple'>
print(m.group())    # 輸出 pple
print(m.start())    # 輸出 1
print(m.end())    # 輸出 5 注意！pple 的位置是 1~4
print(m.span())    # 輸出 (1, 5)

print('------------------------------------------------------------')	#60個

print('1111 fail')
from selenium import webdriver    # 匯入 selenium 的 webdriver 子套件
from time import sleep         # 匯入內建 time 模組的 sleep() 函式 (計時用)
browser = webdriver.Chrome()   # 建立 Chrome 瀏覽器物件
browser.get('http://www.flag.com.tw')  # 開啟 Chrome 並連到旗標網站
sleep(5)                       # 暫停 5 秒
browser.close()                # 關閉網頁(目前分頁)A

print('------------------------------------------------------------')	#60個

print('2222')

from selenium import webdriver # 匯入 selenium 的 webdriver
from time import sleep         # 匯入內建 time 模組的 sleep() 函式

browser = webdriver.Chrome()            # 建立 Chrome 瀏覽器物件
browser.get('http://www.google.com')    # 開啟 Chrome 並連到 Google 網站
print('標題：' + browser.title)         # 輸出網頁標題
print('網址：' + browser.current_url)   # 輸出網頁網址
print('內容：' + browser.page_source[0:50]) # 輸出網頁原始碼的前 50 個字
print('視窗：', browser.get_window_rect())  # 輸出視窗的位置及寬高
browser.save_screenshot('d:/scrcap.png')   # 截取網頁畫面
sleep(3) # 暫停 3 秒
browser.set_window_rect(200, 100, 500, 250)   # 改變視窗位置及大小
sleep(3)
browser.fullscreen_window()     # 將視窗設為全螢幕
sleep(3)
browser.quit() # 關閉視窗結束驅動

print('------------------------------------------------------------')	#60個

print('333')

from selenium import webdriver # 匯入 selenium 的 webdriver

browser = webdriver.Chrome() # 建立 Chrome 瀏覽器物件
browser.get('http://www.google.com') # 開啟 Chrome 並連到旗標網站
e1 = browser.find_element_by_tag_name('head')  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name('title')  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到
browser.quit()     # 關閉視窗結束驅動

print('------------------------------------------------------------')	#60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

opt = webdriver.ChromeOptions()  # ←建立選項物件
opt.add_experimental_option('prefs',  # ←在選項物件中加入「禁止顯示訊息框」的選項
                            {'profile.default_content_setting_values': {'notifications': 2}})
browser = webdriver.Chrome(options=opt)  # ←以 options 指名參數來建立瀏覽器物件

browser.get('http://www.facebook.com')  # ←開啟 Chrome 並連到 fb 網站
browser.find_element_by_id('email').send_keys('您的帳號')  # }
browser.find_element_by_id('pass').send_keys('您的密碼')  # }輸入帳密並按登入鈕
browser.find_element_by_name('login').click()  # }

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

