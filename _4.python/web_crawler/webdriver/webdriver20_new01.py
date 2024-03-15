#url = 'https://example.oxxostudio.tw/python/selenium/demo.html'
url = 'C:/_git/vcs/_1.data/______test_files1/webdriver_data.html'

'''
新進測試

'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立瀏覽器物件
driver = webdriver.Chrome()    #使用Chrome
#driver = webdriver.Firefox()   #使用Firefox
driver.set_window_position(0, 0)	#設定視窗位置
driver.set_window_size(800, 600)	#設定視窗大小
driver.maximize_window()    #全螢幕顯示

print('------------------------------------------------------------')	#60個

#PyAutoGUI，自動控制滑鼠與鍵盤
import pyautogui as auto

'''
url = 'https://www.google.com/'
driver.get(url)  #開啟網址
time.sleep(3)


txt = driver.find_element(By.NAME, 'q')             # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys('this is a lion-mouse')
time.sleep(2)

print(txt.tag_name)
print(txt.get_attribute("type"))
print(txt.get_attribute("id"))


txt.submit()    #就是按了enter
'''

#url = 'https://tw.yahoo.com/'
driver.get(url)  #開啟網址
time.sleep(1)

auto.PAUSE = 1

x_st = 60
y_st = 140
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
auto.typewrite("獅子")
auto.click()

x_st = 60
y_st = 200
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)


y_st += 22
time.sleep(2)
print('move to (', x_st, ', ', y_st,')')
auto.moveTo(x_st, y_st, 2)
time.sleep(2)
auto.click()
time.sleep(2)

print('------------------------------------------------------------')	#60個
print('完成')

'''
print('準備關閉瀏覽器')
for i in range(0, 10):
    print(i, '秒')	# 0~9
    time.sleep(1)

#print('關閉瀏覽器')
#driver.close()  #關閉瀏覽器

print('關閉瀏覽器並且退出驅動程序')
driver.quit()   #關閉瀏覽器並且退出驅動程序
'''

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
print(type(browser))

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

dirverPath = 'D:\geckodriver\chromedriver.exe'
browser = webdriver.Chrome(dirverPath)
print(type(browser))

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

print(f"網頁標題內容是 = {browser.title}")

tag1 = browser.find_element_by_id('author')             # 傳回<h1>
print(f"\n標籤名稱 = {tag1.tag_name}, 內容是 = {tag1.text}")

print()
tag2 = browser.find_elements_by_id('content')           # 傳回<h1>
for i in range(len(tag2)):
    print(f"標籤名稱 = {tag2[i].tag_name}, 內容是 = {tag2[i].text}")

print()
tag3 = browser.find_elements_by_tag_name('p')           # 傳回<p>
for i in range(len(tag3)):
    print(f"標籤名稱 = {tag3[i].tag_name}, 內容是 = {tag3[i].text}")

print()
tag4 = browser.find_elements_by_tag_name('img')         # 傳回<img>
for i in range(len(tag4)):
    print(f"標籤名稱 = {tag4[i].tag_name}, 內容是 = {tag4[i].get_attribute('src')}")

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'https://deepwisdom.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

eleLink = browser.find_element_by_link_text('深智數位緣起')
print(type(eleLink))            # 列印eleLink資料類別
time.sleep(5)                   # 暫停5秒
eleLink.click()                 

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.google.com'
browser.get(url)                        # 網頁下載至瀏覽器

txtBox = browser.find_element_by_name('q')
txtBox.send_keys('明志科技大學')        # 輸入表單資料
time.sleep(5)                           # 暫停5秒
txtBox.submit()                         # 送出表單

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://www.mcut.edu.tw'
browser.get(url)                    # 網頁下載至瀏覽器

ele = browser.find_element_by_tag_name('body')
time.sleep(3)
ele.send_keys(Keys.PAGE_DOWN)       # 網頁捲動到下一頁
time.sleep(3)
ele.send_keys(Keys.END)             # 網頁捲動到最底端
time.sleep(3)
ele.send_keys(Keys.PAGE_UP)         # 網頁捲動到上一頁
time.sleep(3)
ele.send_keys(Keys.HOME)            # 網頁捲動到最上端

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'https://deepwisdom.com.tw'
browser.get(url)                    # 網頁下載至瀏覽器

time.sleep(3)
browser.refresh()                   # 更新網頁
time.sleep(3)
browser.quit()                      # 關閉網頁

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
import time
url = "https://hophd.wordpress.com"
web = webdriver.Chrome("chromedriver.exe")
web.implicitly_wait(60)
web.get(url)
web.set_window_position(0, 0)
time.sleep(10)
web.quit()




print("------------------------------------------------------------")  # 60個


from selenium import webdriver
import time
url = "https://hophd.wordpress.com"
web = webdriver.Chrome("chromedriver.exe")
web.implicitly_wait(60)
web.get(url)
web.set_window_position(0, 0)
time.sleep(10)
web.quit()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


