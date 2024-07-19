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



""" NG
from selenium import webdriver

# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome("./chromedriver", options=opt)

# 建立瀏覽器物件
#driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()   #使用Firefox

url = "google.com"
driver.get(url)

"""

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.get("爬取的網址")
# 從載入後的動態網頁裡，找到指定的元素
imgCount = driver.find_element(By.CSS_SELECTOR, "CSS 選擇器")

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
actions = ActionChains(driver)
# 滑鼠先移到 submitBtn 上，然後再點擊 submitBtn
actions.move_to_element(submitBtn).click(submitBtn)
actions.perform()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
time.sleep(1)  # 等待一秒
submitBtn.click()
time.sleep(0.5)  # 等待 0.5 秒
submitBtn.click()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")  # 指向 chromedriver 的位置
url = "https://www.google.com"
driver.get(url)  # 打開瀏覽器，開啟網頁

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select  # 使用 Select 對應下拉選單

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)  # 開啟範例網址
a = driver.find_element(By.ID, "a")  # 取得 id 為 a 的網頁元素 ( 按鈕 A )
b = driver.find_element(By.CLASS_NAME, "btn")  # 取得 class 為 btn 的網頁元素 ( 按鈕 B )
c = driver.find_element(By.CSS_SELECTOR, ".test")  # 取得 class 為 test 的網頁元素 ( 按鈕 C )
d = driver.find_element(By.NAME, "dog")  # 取得屬性 name 為 dog 的網頁元素 ( 按鈕 D )
h1 = driver.find_element(By.TAG_NAME, "h1")  # 取得 tag h1 的網頁元素
link1 = driver.find_element(By.LINK_TEXT, "我是超連結，點擊會開啟 Google 網站")  # 取得指定超連結文字的網頁元素
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")  # 取得超連結文字包含 Google 的網頁元素
select = Select(
    driver.find_element(By.XPATH, "/html/body/select")
)  # 取得 html > body > select 這個網頁元素

a.click()  # 點擊 a
print(a.text)  # 印出 a 元素的內容
time.sleep(0.5)
b.click()  # 點擊 b
print(b.text)  # 印出 b 元素的內容
time.sleep(0.5)
c.click()  # 點擊 c
print(c.text)  # 印出 c 元素的內容
time.sleep(0.5)
d.click()  # 點擊 d
print(d.text)  # 印出 d 元素的內容
time.sleep(0.5)
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
time.sleep(0.5)
h1.click()  # 點擊 h1
time.sleep(0.5)
link1.click()  # 點擊 link1
time.sleep(0.5)
link2.click()  # 點擊 link2
print(link2.get_attribute("href"))  # 印出 link2 元素的 href 屬性

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
a.click()  # 點擊按鈕 A，出現 a 文字
time.sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 1
add.click()  # 點擊 add 按鈕，出現 數字 2
time.sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 3
time.sleep(1)
add.click()  # 點擊 add 按鈕，出現 數字 4

print("------------------------------------------------------------")  # 60個

# 下方的程式使用「ActionChains」的方式，結果與上述的執行結果相同。
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
actions = ActionChains(driver)  # 使用 ActionChains 的方式
actions.click(a).pause(1)  # 點擊按鈕 A，出現 a 文字後，暫停一秒
actions.double_click(add).pause(1).click(add).pause(1).click(add)
# 連點 add 按鈕，等待一秒後再次點擊，等待一秒後再次點擊
actions.perform()  # 執行儲存的動作

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
a = driver.find_element(By.ID, "a")
show = driver.find_element(By.ID, "show")
actions = ActionChains(driver)
actions.click(show).send_keys(["1", "2", "3", "4", "5"])  # 輸入 1～5 的鍵盤值 ( 必須是字串 )
actions.pause(1)  # 等待一秒
actions.click(a)  # 點擊按鈕 A
actions.pause(1)  # 等待一秒
actions.send_keys_to_element(show, ["A", "B", "C", "D", "E"])  # # 輸入 A～E 的鍵盤值
actions.perform()  # 送出動作

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("./chromedriver")
url = "https://example.oxxostudio.tw/python/selenium/demo.html"
driver.get(url)
body = driver.find_element(By.TAG_NAME, "body")
a = driver.find_element(By.ID, "a")
b = driver.find_element(By.CLASS_NAME, "btn")
c = driver.find_element(By.CSS_SELECTOR, ".test")
d = driver.find_element(By.NAME, "dog")
link1 = driver.find_element(By.LINK_TEXT, "我是超連結，點擊會開啟 Google 網站")
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")

print(a.id)
print(b.text)
print(c.tag_name)
print(d.size)
print(link1.get_attribute("href"))
print(link2.get_attribute("target"))
body.screenshot("./test.png")

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome("./chromedriver")
url = "https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html"
driver.get(url)

time.sleep(1)
driver.execute_script("window.scrollTo(0, 500)")  # 捲動到 500px 位置
time.sleep(1)
driver.execute_script("window.scrollTo(0, 2500)")  # 捲動到 2500px 位置
time.sleep(1)
driver.execute_script("window.scrollTo(0, 0)")  # 捲動到 0px 位置

h1 = driver.find_element(By.TAG_NAME, "h1")
h3 = driver.find_element(By.TAG_NAME, "h3")
script = """
  let h1 = arguments[0];
  let h3 = arguments[1];
  alert(h1, h3)
"""
driver.execute_script(script, h1, h3)  # 執行 JavaScript，印出元素
time.sleep(2)
Alert(driver).accept()  # 點擊提示視窗的確認按鈕，關閉提示視窗

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
driver = webdriver.Chrome("./chromedriver", options=opt)
# 清空 window.navigator
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)

print("------------------------------------------------------------")  # 60個

url = "https://twitter.com"
driver.get(url)
time.sleep(2)
driver.execute_script(f"window.scrollTo(0, 200)")  # 自動往下捲動 200px
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')  # 取得登入按鈕
login.click()  # 點擊登入按鈕

print("------------------------------------------------------------")  # 60個

time.sleep(2)  # 等待兩秒，讓網頁載入完成
# 取得輸入 email 的輸入框
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("你的 email")  # 輸入 email
print("輸入 email 完成")
# 取得畫面上所有按鈕 ( 使用 elements )
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "下一步" or i.text == "Next":
        i.click()  # 如果按鈕是「下一步」或「Next」就點擊
        print("點擊下一步")
        break

print("------------------------------------------------------------")  # 60個

time.sleep(2)  # 等待兩秒頁面載入後繼續
try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")  # 輸入帳號
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()  # 如果按鈕是「下一步」或「Next」就點擊
            print("驗證使用者帳號，點擊下一步")
            break
    time.sleep(2)  # 等待兩秒頁面載入後繼續
except:
    print("ok")
    time.sleep(2)  # 如果沒有出現安全性畫面，等待兩秒頁面載入後繼續

print("------------------------------------------------------------")  # 60個

pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys("你的密碼")
print("輸入密碼")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "登入" or i.text == "Log in":
        i.click()
        print("點擊登入")
        break

print("------------------------------------------------------------")  # 60個

time.sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")  # 在輸入框輸入文字
print("輸入文字")
time.sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")  # 提供圖片絕對路徑，上傳圖片
print("上傳圖片")
time.sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()  # 點擊推文按鈕
        print("推文完成")
        break
time.sleep(1)
driver.close()  # 關閉瀏覽器視窗

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.common.by import By

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome("./chromedriver", options=opt)
driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
    Object.defineProperty(navigator, 'webdriver', {
      get: () => undefined
    })
  """
    },
)

url = "https://twitter.com"
driver.get(url)
time.sleep(2)
driver.execute_script(f"window.scrollTo(0, 200)")
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
login.click()
time.sleep(2)
username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("你的 email")
print("輸入 email 完成")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "下一步" or i.text == "Next":
        i.click()
        print("點擊下一步")
        break
time.sleep(2)

try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()
            print("驗證使用者帳號，點擊下一步")
            break
    time.sleep(2)
except:
    print("ok")
    time.sleep(2)

pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys("你的密碼")
print("輸入密碼")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')

for i in buttons:
    if i.text == "登入" or i.text == "Log in":
        i.click()
        print("點擊登入")
        break

time.sleep(2)
textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")
print("輸入文字")
time.sleep(1)
imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")
print("上傳圖片")
time.sleep(1)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()
        print("推文完成")
        break
time.sleep(1)
driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver 子套件

browser = webdriver.Chrome()  # 建立 Chrome 瀏覽器物件
url = "http://www.flag.com.tw"
browser.get(url)  # 開啟 Chrome 並連到旗標網站
time.sleep(5)  # 暫停 5 秒
browser.close()  # 關閉網頁(目前分頁)A

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

browser = webdriver.Chrome()  # 建立 Chrome 瀏覽器物件
url = "http://www.google.com"
browser.get(url)  # 開啟 Chrome 並連到 Google 網站
print("標題：" + browser.title)  # 輸出網頁標題
print("網址：" + browser.current_url)  # 輸出網頁網址
print("內容：" + browser.page_source[0:50])  # 輸出網頁原始碼的前 50 個字
print("視窗：", browser.get_window_rect())  # 輸出視窗的位置及寬高
browser.save_screenshot("d:/scrcap.png")  # 截取網頁畫面
time.sleep(3)  # 暫停 3 秒
browser.set_window_rect(200, 100, 500, 250)  # 改變視窗位置及大小
time.sleep(3)
browser.fullscreen_window()  # 將視窗設為全螢幕
time.sleep(3)
browser.quit()  # 關閉視窗結束驅動

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

browser = webdriver.Chrome()  # 建立 Chrome 瀏覽器物件
url = "http://www.google.com"
browser.get(url)  # 開啟 Chrome 並連到旗標網站
e1 = browser.find_element_by_tag_name("head")  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name("title")  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到
browser.quit()  # 關閉視窗結束驅動

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

opt = webdriver.ChromeOptions()  # ←建立選項物件
opt.add_experimental_option(
    "prefs",  # ←在選項物件中加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
browser = webdriver.Chrome(options=opt)  # ←以 options 指名參數來建立瀏覽器物件
url = "http://www.facebook.com"
browser.get(url)  # ←開啟 Chrome 並連到 fb 網站
browser.find_element_by_id("email").send_keys("您的帳號")  # }
browser.find_element_by_id("pass").send_keys("您的密碼")  # }輸入帳密並按登入鈕
browser.find_element_by_name("login").click()  # }

print("------------------------------------------------------------")  # 60個

from selenium import webdriver  # 匯入 selenium 的 webdriver

opt = webdriver.ChromeOptions()  # 建立選項物件
opt.add_experimental_option(
    "prefs",  # 加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
browser = webdriver.Chrome(options=opt)  # 以 options 參數來建立瀏覽器物件

url = "http://www.google.com"
browser.get(url)  # ←開啟 Chrome 並連到 Google 網站
browser.maximize_window()  # ←將視窗最大化以避免最右邊的登入鈕沒顯示出來

browser.find_element_by_id("gb_70").click()  # ←按登入鈕
time.sleep(3)  # ←暫停 3 秒等待進入下一頁
browser.find_element_by_id("identifierId").send_keys("您的帳號")  # }←輸入帳號
browser.find_element_by_id("identifierNext").click()  # ←按繼續鈕
time.sleep(3)  # ←暫停 3 秒等待進入下一頁
browser.find_element_by_name("password").send_keys("您的密碼")  # ←輸入帳密
browser.find_element_by_id("passwordNext").click()  # ←按繼續鈕

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driverPath = "D:\geckodriver\geckodriver.exe"
browser = webdriver.Firefox(executable_path=driverPath)
url = "https://www.wikipedia.org/"
browser.get(url)  # 網頁下載至瀏覽器

txtBox = browser.find_element_by_id("searchInput")
txtBox.send_keys("Artificial Intelligence")  # 輸入表單資料
time.sleep(5)  # 暫停5秒
txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

# pip3 install selenium
# 下載 chromedriver ( 注意要對應自己 chrome 版本 )
# https://chromedriver.chromium.org/downloads

driver = webdriver.Chrome(
    "/Users/oxxo/Documents/oxxo/practice/python/chromedriver"
)  # 設定 chromedriver 路徑

url = "http://oxxo.studio"
driver.get(url)  # 前往這個網址
print(driver.title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 捲動到最下方
time.sleep(1)
for i in range(1, 7):
    img = driver.find_element_by_xpath(
        '//*[@id="content-grid"]/ul/li[' + str(i) + "]/a[1]/div/img"
    )
    response = requests.get(img.get_attribute("src"))
    with open("demo/test" + str(i) + ".jpg", "wb") as f:
        f.write(response.content)  # 將response.content二進位內容寫入檔案
driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("headless")  # 不會開啟瀏覽器

driver = webdriver.Chrome(
    "/Users/oxxo/Documents/oxxo/practice/python/chromedriver", chrome_options=options
)  # 設定 chromedriver 路徑

url = "https://www.dinbendon.net/do/login"
driver.get(url)  # 前往這個網址

# 輸入使用者 id
user = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input'
)
user.send_keys("XXX")

# 輸入使用者密碼
pwd = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input'
)
pwd.send_keys("XXX")

# 取得驗證碼訊息
checkquestion = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]'
)
check = driver.find_element_by_xpath(
    '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input'
)

# 計算驗證碼
checktext = checkquestion.text
print(checktext)
a = int(re.findall(r"\d+", checktext)[0])  # 使用正則表達式提取數字
b = int(re.findall(r"\d+", checktext)[1])
result = a + b
print(result)
check.send_keys(result)  # 輸入驗證碼

# 點擊按鈕
btn = driver.find_element_by_xpath(
    ' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]'
)
btn.click()

time.sleep(1)

# 抓取第一筆便當名稱，加入例外處理
try:
    menu = driver.find_element_by_xpath(
        '//*[@id="inProgressBox_inProgressOrders_0"]/td[2]/div[1]/a/span[2]'
    )

    print(menu.text)
except:
    print("找不到便當名稱")

driver.close()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver

driver = webdriver.Chrome(
    "/Users/oxxo/Documents/oxxo/practice/python/chromedriver"
)  # 設定 chromedriver 路徑

url = "https://www.google.com.tw/imghp?hl=zh-TW&tab=wi&ogbl"
driver.get(url)  # 前往這個網址

search = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
search.send_keys("林志玲")

btn = driver.find_element_by_xpath('//*[@id="sbtc"]/button')
btn.click()

for i in range(1, 6):
    time.sleep(0.5)
    div = driver.find_element_by_xpath(
        "/html/body/div[6]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div["
        + str(i)
        + "]"
    )
    div.click()

    time.sleep(0.5)
    img = driver.find_element_by_xpath(
        '//*[@id="irc-ss"]/div[' + str(i) + "]/div[1]/div[4]/div[1]/a/div/img"
    )
    src = img.get_attribute("src")
    print(src)
    if str(src) != "None":
        if ".jpg" in src:
            filename = src.split("/")[-1]
            response = requests.get(src)
            with open("demo/" + str(filename), "wb") as f:
                f.write(response.content)  # 將response.content二進位內容寫入檔案
                closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
                closeBtn.click()
        else:
            closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]')
            closeBtn.click()

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


