# url = "https://example.oxxostudio.tw/python/selenium/demo.html"
url = "D:/_git/vcs/_1.data/______test_files1/webdriver_data.html"

"""
# geckodriver 是讓自動化測試工具（如 Selenium）能夠控制 Firefox 瀏覽器 的橋樑程式（驅動程式）。
# Firefox 的網頁排版引擎叫做 Gecko，因此官方為它打造的驅動程式就命名為 geckodriver。

• 主要功能：它會接收來自 Selenium 的標準指令（例如：開啟網頁、點擊按鈕、輸入文字），並將這些指令翻譯成 Firefox 聽得懂的動作。
• 各瀏覽器的對應關係：每個主流瀏覽器都有專屬的驅動程式。

瀏覽器		對應的驅動程式
Firefox		geckodriver
Google Chrome	chromedriver
"""

import re
import os
import sys
import csv
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# 建立瀏覽器物件
# driver = webdriver.Chrome()  # 使用Chrome
driver = webdriver.Firefox()  # 使用Firefox
# driver = webdriver.Edge("./msedgedriver") # 還不能用  # 使用Edge
driver.set_window_position(0, 0)  # 設定視窗位置
driver.set_window_size(800, 600)  # 設定視窗大小
driver.maximize_window()  # 最大化視窗後開啟網站

url = "http://aaa.24ht.com.tw"

print(type(driver))

driver.get(url)  # 網頁下載至瀏覽器

print("標題       :", driver.title)
print("瀏覽器名稱 :", driver.name)  # 列印瀏覽器名稱
print("網址       :", driver.current_url)  # 網址
print("網頁連線id :", driver.session_id)  # 網頁連線id
print("視窗       :", driver.get_window_rect())  # 輸出視窗的位置及寬高
print("瀏覽器功能 :\n", driver.capabilities)  # 瀏覽器功能設定訊息

print("列印網頁原始碼")
print(driver.page_source)  # 列印網頁原始碼
print("內容：" + driver.page_source[0:50])  # 輸出網頁原始碼的前 50 個字

driver.get(url)
driver.maximize_window()
print("目前網址：", driver.current_url)
print("瀏覽器尺寸：", driver.get_window_size())
print("網頁原始碼：\n", driver.page_source)

time.sleep(1)  # 等1秒

driver.close()  # 關閉瀏覽器視窗

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序


# 以上為簡單使用 driver 的基本功能

print("------------------------------------------------------------")  # 60個
print("測試 OK ST")
print("------------------------------------------------------------")  # 60個

# 可以用得盡量搬到前面

url = "https://deepwisdom.com.tw"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒

driver.refresh()  # 更新網頁

time.sleep(1)  # 等1秒

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://hophd.wordpress.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(60)
driver.get(url)  # 打開瀏覽器，開啟網頁
driver.set_window_position(0, 0)

time.sleep(1)  # 等1秒

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

print("------------------------------------------------------------")  # 60個

from selenium.webdriver.support.select import Select  # 使用 Select 對應下拉選單

url = "https://example.oxxostudio.tw/python/selenium/demo.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

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
time.sleep(1)  # 等1秒
b.click()  # 點擊 b
print(b.text)  # 印出 b 元素的內容
time.sleep(1)  # 等1秒
c.click()  # 點擊 c
print(c.text)  # 印出 c 元素的內容
time.sleep(1)  # 等1秒
d.click()  # 點擊 d
print(d.text)  # 印出 d 元素的內容
time.sleep(1)  # 等1秒
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
time.sleep(1)  # 等1秒
h1.click()  # 點擊 h1
time.sleep(1)  # 等1秒
link1.click()  # 點擊 link1
time.sleep(1)  # 等1秒
link2.click()  # 點擊 link2
print(link2.get_attribute("href"))  # 印出 link2 元素的 href 屬性

print("------------------------------------------------------------")  # 60個

url = "https://example.oxxostudio.tw/python/selenium/demo.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
a.click()  # 點擊按鈕 A，出現 a 文字
time.sleep(1)  # 等1秒
add.click()  # 點擊 add 按鈕，出現 數字 1
add.click()  # 點擊 add 按鈕，出現 數字 2
time.sleep(1)  # 等1秒
add.click()  # 點擊 add 按鈕，出現 數字 3
time.sleep(1)  # 等1秒
add.click()  # 點擊 add 按鈕，出現 數字 4

print("------------------------------------------------------------")  # 60個

# 下方的程式使用「ActionChains」的方式，結果與上述的執行結果相同。
from selenium.webdriver.common.action_chains import ActionChains

url = "https://example.oxxostudio.tw/python/selenium/demo.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

a = driver.find_element(By.ID, "a")
add = driver.find_element(By.ID, "add")
actions = ActionChains(driver)  # 使用 ActionChains 的方式
actions.click(a).pause(1)  # 點擊按鈕 A，出現 a 文字後，暫停一秒
actions.double_click(add).pause(1).click(add).pause(1).click(add)
# 連點 add 按鈕，等待一秒後再次點擊，等待一秒後再次點擊
actions.perform()  # 執行儲存的動作

print("------------------------------------------------------------")  # 60個

from selenium.webdriver.common.action_chains import ActionChains

url = "https://example.oxxostudio.tw/python/selenium/demo.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

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

url = "https://example.oxxostudio.tw/python/selenium/demo.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

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
print("------------------------------------------------------------")  # 60個

url = "http://www.flag.com.tw"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒

driver.close()  # 關閉瀏覽器視窗  # 關閉網頁(目前分頁)A

print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

driver.save_screenshot("d:/scrcap.png")  # 截取網頁畫面

time.sleep(1)  # 等1秒

driver.set_window_rect(200, 100, 500, 250)  # 改變視窗位置及大小

time.sleep(1)  # 等1秒

driver.fullscreen_window()  # 將視窗設為全螢幕

time.sleep(1)  # 等1秒

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

urls = [
    "http://aaa.24ht.com.tw",
    # "http://www.mcut.edu.tw", NG
    "http://aaa.24ht.com.tw",
    "http://www.siliconstone.com",
]

driver = webdriver.Firefox()  # 使用Firefox

for url in urls:
    print('網址 :', url)
    driver.get(url)  # 網頁下載至瀏覽器
    time.sleep(1)  # 等1秒

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("標題 :", driver.title)

html = driver.page_source  # 網頁原始碼
print(html)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)

print("標題 :", driver.title)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("標題 :", driver.title)

html = driver.page_source  # 網頁原始碼
print(html)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&jobcatExpansionType=1&order=12&asc=0&page=6&mode=s&jobsource=2018indexpoc"
driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

print("標題 :", driver.title)
print(len(driver.page_source))

for x in range(5):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(1)  # 等1秒
    print(x + 1, len(driver.page_source))

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")

print("標題 :", driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id": "list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

keyword = "dog"
pathdir = "imgur2"
url = "http://imgur.com/search?q=" + keyword
os.makedirs(pathdir, exist_ok=True)

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

for x in range(3):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(1)  # 等1秒

soup = BeautifulSoup(driver.page_source, "lxml")
images = soup.find_all("a", class_="image-list-link")
print("圖檔數:", len(images))
for img in images:
    try:
        imgUrl = "http:" + img.find("img").get("src")
        print("下載:", imgUrl)
        res = requests.get(imgUrl)
    except requests.exceptions.MissingSchema:
        print("圖檔下載錯誤...")
        continue

    imgFile = os.path.join(pathdir, os.path.basename(imgUrl))
    fp = open(imgFile, "wb")
    for chunk in res.iter_content(100000):
        fp.write(chunk)
    fp.close()
print("結束 Imgur 網頁圖檔下載...")

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

keyword = "dog"
url = "http://imgur.com/search?q=" + keyword

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

for x in range(3):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(1)  # 等1秒

soup = BeautifulSoup(driver.page_source, "lxml")
images = soup.find_all("a", class_="image-list-link")
print("圖檔數:", len(images))
with open("imgur_dog.csv", "w+", newline="", encoding="big5") as fp:
    writer = csv.writer(fp)
    writer.writerow(["image-href"])
    for img in images:
        imgUrl = "http:" + img.find("img").get("src")
        writer.writerow([imgUrl])

print("成功建立 imgur_dog.csv 檔...")

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# url = "https://www.cwb.gov.tw/V8/C/W/County/County.html?CID=65" old
url = "https://www.cwa.gov.tw/V8/C/W/County/County.html?CID=65"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")
span = soup.select_one("span.tem-C.is-active")
print(span.text)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("測試 OK SP")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 以下測試中
print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_1.data/______test_files1/webdriver_data_old.html"
url = "D:/_git/vcs/_1.data/______test_files1/webdriver_data_old.html"
# url = "D:/_git/vcs/_1.data/______test_files1/webdriver_data.html"  # NG
# webdriver_data

url = "http://aaa.24ht.com.tw"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

print("標題 :", driver.title)

tag2 = driver.find_element(By.ID, "author")  # 傳回<h1>
print(tag2)
print(tag2.text)

print("\n標籤名稱 = %s, 內容是 = %s " % (tag2.tag_name, tag2.text))

print()

tag3 = driver.find_elements(By.ID, "content")  # 傳回<h1> 複數

for t3 in tag3:
    print("標籤名稱 = %s, 內容是 = %s " % (t3.tag_name, t3.text))

print()

tag4 = driver.find_elements(By.TAG_NAME, "p")  # 傳回<p> 複數

for t4 in tag4:
    print("標籤名稱 = %s, 內容是 = %s " % (t4.tag_name, t4.text))

print()

tag5 = driver.find_elements(By.TAG_NAME, "img")  # 傳回<img> 複數

for t5 in tag5:
    print("標籤名稱 = %s, 內容是 = %s " % (t5.tag_name, t5.get_attribute("src")))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://aaa.24ht.com.tw"

# driver = webdriver.Chrome()  # 使用Chrome
driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 打開瀏覽器，開啟網頁

print("標題 :", driver.title)

tag1 = driver.find_element(By.ID, "author")  # 傳回<h1>
print(f"\n標籤名稱 = {tag1.tag_name}, 內容是 = {tag1.text}")

print()

tag2 = driver.find_elements(By.ID, "content")  # 傳回<h1> 複數

for i in range(len(tag2)):
    print(f"標籤名稱 = {tag2[i].tag_name}, 內容是 = {tag2[i].text}")

print()

tag3 = driver.find_elements(By.TAG_NAME, "p")  # 傳回<p> 複數

for i in range(len(tag3)):
    print(f"標籤名稱 = {tag3[i].tag_name}, 內容是 = {tag3[i].text}")

print()

tag4 = driver.find_elements(By.TAG_NAME, "img")  # 傳回<img> 複數
for i in range(len(tag4)):
    print(f"標籤名稱 = {tag4[i].tag_name}, 內容是 = {tag4[i].get_attribute('src')}")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_1.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element(By.XPATH, "//h4")
print(n1.text)

n2 = driver.find_element(By.XPATH, "//body/section/h4")
print(n2.text)

n3 = driver.find_element(By.XPATH, "//section/h4")
print(n3.text)

n4 = driver.find_element(By.XPATH, "//body/*/h4")
print(n4.text)

print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_1.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element(By.XPATH, "//p")
print(n1.text)

print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_1.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element(By.XPATH, "//section/p[1]")
print(n1.text)

n2 = driver.find_element(By.XPATH, "//section/p[2]")
print(n2.text)

print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_1.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element(By.XPATH, "//section/p[@class='year']")
print(n1.text)

n1 = driver.find_element(By.XPATH, "//section/p[@class='price']")
print(n1.text)

print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_2.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 網頁下載至瀏覽器

pict = driver.find_element(By.XPATH, "//section/img")
print(pict.get_attribute("src"))

print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_3.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 網頁下載至瀏覽器

# n1 = driver.find_element_by_xpath("//h1/em") old
n1 = driver.find_element(By.XPATH, "//h1/em")
print("em          : ", n1.text)

# n2 = driver.find_element_by_xpath("//h1") old
n2 = driver.find_element(By.XPATH, "//h1")
print("h1          : ", n2.text)

# n3 = driver.find_element_by_xpath("//h1") old
n3 = driver.find_element(By.XPATH, "//h1")
print("textContent : ", n3.get_attribute("textContent"))

# n4 = driver.find_element_by_xpath("//h1") old
n4 = driver.find_element(By.XPATH, "//h1")
print("innerHTML : ", n4.get_attribute("innerHTML"))

# n5 = driver.find_element_by_xpath("//h1") old
n5 = driver.find_element(By.XPATH, "//h1")
print("outerHTML : ", n5.get_attribute("outerHTML"))

print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_4.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 網頁下載至瀏覽器

# n = driver.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]") old
n = driver.find_element(By.XPATH, "//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute("outerHTML"))
print(n.get_attribute("href"))

print("------------------------------------------------------------")  # 60個

url = "D:/_git/vcs/_4.python/web_crawler/webdriver/data/h7_4.html"

headless = webdriver.ChromeOptions()
headless.add_argument("headless")  # 隱藏參數
driver = webdriver.Chrome(options=headless)  # 使用Chrome
driver.implicitly_wait(5)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器

# n = driver.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]")
n = driver.find_element(By.XPATH, "//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute("outerHTML"))
print(n.get_attribute("href"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.deepmind.com.tw"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

time.sleep(1)  # 等1秒
driver.refresh()  # 更新網頁
time.sleep(1)  # 等1秒

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.deepmind.com.tw"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

# eleLink = driver.find_element_by_link_text("深智數位緣起")  # old
eleLink = driver.find_element(By.LINK_TEXT, "深智數位緣起")  # 取得指定超連結文字的網頁元素

print(type(eleLink))  # 列印eleLink資料類別

time.sleep(1)  # 等1秒

eleLink.click()

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox

url = "https://deepwisdom.com.tw"
driver.get(url)  # 打開瀏覽器，開啟網頁

# eleLink = driver.find_element_by_link_text("深智數位緣起") old
eleLink = driver.find_element(By.LINK_TEXT, "深智數位緣起")

print(type(eleLink))  # 列印eleLink資料類別
time.sleep(1)  # 等1秒
eleLink.click()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.mcut.edu.tw/?Lang=en"

driver = webdriver.Firefox()  # 使用Firefox
# NG driver.get(url)  # 網頁下載至瀏覽器

# txtBox = driver.find_element_by_id("hdSchKey")  # old
txtBox = driver.find_element(By.ID, "hdSchKey")
txtBox.send_keys("王永慶")  # 輸入表單資料

time.sleep(1)  # 等1秒

txtBox.submit()  # 送出表單

print("------------------------------")  # 30個

url = "http://www.mcut.edu.tw/?Lang=en"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

# txtBox = driver.find_element_by_name("SchKey") old
txtBox = driver.find_element(By.NAME, "SchKey")
txtBox.send_keys("王永慶")  # 輸入表單資料

time.sleep(1)  # 等1秒

txtBox.submit()  # 送出表單

print("------------------------------")  # 30個

url = "http://www.mcut.edu.tw"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

ele = driver.find_element_by_tag_name("body")
time.sleep(1)  # 等1秒
ele.send_keys(Keys.PAGE_DOWN)  # 網頁捲動到下一頁
time.sleep(1)  # 等1秒
ele.send_keys(Keys.END)  # 網頁捲動到最底端
time.sleep(1)  # 等1秒
ele.send_keys(Keys.PAGE_UP)  # 網頁捲動到上一頁
time.sleep(1)  # 等1秒
ele.send_keys(Keys.HOME)  # 網頁捲動到最上端

print("------------------------------")  # 30個

url = "http://www.mcut.edu.tw"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 打開瀏覽器，開啟網頁

ele = driver.find_element_by_tag_name("body")
time.sleep(1)  # 等1秒
ele.send_keys(Keys.PAGE_DOWN)  # 網頁捲動到下一頁
time.sleep(1)  # 等1秒
ele.send_keys(Keys.END)  # 網頁捲動到最底端
time.sleep(1)  # 等1秒
ele.send_keys(Keys.PAGE_UP)  # 網頁捲動到上一頁
time.sleep(1)  # 等1秒
ele.send_keys(Keys.HOME)  # 網頁捲動到最上端

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 登入帳號

url = "https://www.google.com"

email = "bunshue@gmail.com"
pwd = "aabbccdd12345"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

# driver.find_element_by_id("gb_70").click()  # old
driver.find_element(By.ID, "gb_70").click()

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"

email = "bunshue@gmail.com"
pwd = "aabbccdd12345"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

# driver.find_element_by_id("gb_70").click()  # 按登入鈕 # old
driver.find_element(By.ID, "gb_70").click()  # 按登入鈕

# driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號 # old
driver.find_element(By.ID, "identifierId").send_keys(email)  # 輸入帳號

time.sleep(1)  # 等1秒

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = "bunshue@gmail.com"
pwd = "aabbccdd12345"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

# driver.find_element_by_id("gb_70").click()  # 按登入鈕  # old
driver.find_element(By.ID, "gb_70").click()  # 按登入鈕

# driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號   old
driver.find_element(By.ID, "identifierId").send_keys(email)  # 輸入帳號

time.sleep(1)  # 等1秒

# 按繼續鈕
# driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()

time.sleep(1)  # 等1秒

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = "bunshue@gmail.com"
pwd = "aabbccdd12345"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

# driver.find_element_by_id("gb_70").click()  # 按登入鈕  # old
driver.find_element(By.ID, "gb_70").click()  # 按登入鈕

# driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號 # old
driver.find_element(By.ID, "identifierId").send_keys(email)  # 輸入帳號

time.sleep(1)  # 等1秒

# 按繼續鈕
# driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()

time.sleep(1)  # 等1秒

# 輸入密碼
# driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
driver.find_element(By.XPATH, "//input[@type='password']").send_keys(pwd)

time.sleep(1)  # 等1秒

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = "bunshue@gmail.com"
pwd = "aabbccdd12345"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 網頁下載至瀏覽器

# driver.find_element_by_id("gb_70").click()  # 按登入鈕 # old
driver.find_element(By.ID, "gb_70").click()  # 按登入鈕

# driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號 old
driver.find_element(By.ID, "identifierId").send_keys(email)  # 輸入帳號

time.sleep(1)  # 等1秒

# 按繼續鈕
# driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()

time.sleep(1)  # 等1秒

# 輸入密碼
# driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd) old
driver.find_element(By.XPATH, "//input[@type='password']").send_keys(pwd)

time.sleep(1)  # 等1秒

# 按繼續鈕
# driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click() old
driver.find_element(By.XPATH, "//span[@class='RveJvd snByac']").click()

time.sleep(1)  # 等1秒

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://opendata.epa.gov.tw/data/contents/aqi/"

driver = webdriver.Chrome()  # 使用Chrome
# NGdriver.get(url)  # 網頁下載至瀏覽器

# driver.find_element_by_link_text("JSON").click()  # 按JSON鈕 old
driver.find_element(By.LINK_TEXT, "JSON").click()  # 按JSON鈕

time.sleep(1)  # 等1秒

# driver.find_element_by_link_text("XML").click()  # 按XML鈕 old
driver.find_element(By.LINK_TEXT, "XML").click()  # 按XML鈕

time.sleep(1)  # 等1秒

# driver.find_element_by_link_text("CSV").click()  # 按CSV鈕 old
driver.find_element(By.LINK_TEXT, "CSV").click()  # 按CSV鈕

time.sleep(1)  # 等1秒

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://data.epa.gov.tw/"
url = "https://data.moenv.gov.tw/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

# driver.find_element_by_id("field-main-search").send_keys("aqi" + Keys.RETURN)  # 輸入 aqi 後按 Enter  old
driver.find_element(By.ID, "field-main-search").send_keys("aqi" + Keys.RETURN)  # 輸入 aqi 後按 Enter

time.sleep(1)  # 等1秒

# driver.find_element_by_link_text("空氣品質指標(AQI)").click()  # 點選 空氣品質指標(AQI) 鈕 old
driver.find_element(By.LINK_TEXT, "空氣品質指標(AQI)").click()  # 點選 空氣品質指標(AQI) 鈕

time.sleep(1)  # 等1秒

# driver.find_element_by_xpath('//*[@id="dataset-resources"]/div/table/tbody/tr/td[1]/a').click()  # 點選 空氣品質指標(AQI) 鈕 old
driver.find_element(By.XPATH, '//*[@id="dataset-resources"]/div/table/tbody/tr/td[1]/a').click()  # 點選 空氣品質指標(AQI) 鈕

time.sleep(1)  # 等1秒

# driver.find_element_by_link_text("JSON").click()  # 下載 JSON old
driver.find_element(By.LINK_TEXT, "JSON").click()  # 下載 JSON

time.sleep(1)  # 等1秒

# driver.find_element_by_link_text("XML").click()  # 下載 XML old
driver.find_element(By.LINK_TEXT, "XML").click()  # 下載 XML

time.sleep(1)  # 等1秒

# driver.find_element_by_link_text("CSV").click()  # 下載 CSV old
driver.find_element(By.LINK_TEXT, "CSV").click()  # 下載 CSV

time.sleep(1)  # 等1秒

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("標題 :", driver.title)

html = driver.page_source  # 網頁原始碼
print(html)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install())
)  # 使用Edge
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("標題 :", driver.title)

html = driver.page_source  # 網頁原始碼
print(html)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
cookies = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookies)

print("標題 :", driver.title)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install())
)  # 使用Edge
driver.implicitly_wait(10)
cookies = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookies)

print("標題 :", driver.title)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options
)  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("標題 :", driver.title)

html = driver.page_source  # 網頁原始碼
print(html)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

print("標題 :", driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")

tag_ol = soup.find("ol", {"id": "list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install())
)  # 使用Edge
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

print("標題 :", driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")

tag_ol = soup.find("ol", {"id": "list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")

# tag_ol = driver.find_element_by_xpath('//*[@id="list"]')  old
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')

print(tag_ol.tag_name)
# tags_li = tag_ol.find_elements_by_xpath("//li") old
tags_li = tag_ol.find_elements(By.XPATH, "//li")

for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome

driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")

# tag_ol = driver.find_element_by_xpath('//*[@id="list"]')  old
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute("innerHTML"))

soup = BeautifulSoup(tag_ol.get_attribute("innerHTML"), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install())
)  # 使用Edge
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, "/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, "//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, "/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, "//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute("innerHTML"))
soup = BeautifulSoup(tag_ol.get_attribute("innerHTML"), "lxml")

print("找全部的xx<li> + 條件")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(
    service=Service(EdgeChromiumDriverManager().install())
)  # 使用Edge
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute("innerHTML"))
soup = BeautifulSoup(tag_ol.get_attribute("innerHTML"), "lxml")

print("找全部的xx<li> + 條件")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.momoshop.com.tw/search/"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url + "searchShop.jsp?keyword=NBA")

print("標題 :", driver.title)

html = driver.page_source  # 網頁原始碼

fp = open("tmp_NBA.html", "w", encoding="utf8")
fp.write(html)
print("寫入檔案tmp_NBA.html...")
fp.close()

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://fchart.github.io/Ashion/"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")

sec = soup.find("section", class_="product spad")
items = sec.find_all("div", class_="product__item")
print(len(items))
products = []
for item in items:
    tag = item.find("h6").find("a")
    title = tag.text.strip() if tag else "N/A"
    tag = item.find("div", class_="product__item__pic")
    img = tag["data-setbg"].strip() if tag else "N/A"
    tag = item.find("div", class_="product__price")
    price = tag.text.strip() if tag else "N/A"
    print(title)
    products.append({"title": title, "image": url + img, "price": price})

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

with open("tmp_products.json", "w", encoding="utf-8") as fp:  # 寫入JSON檔案
    json.dump(products, fp, indent=2, sort_keys=True, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://fchart.github.io/ML/nba_items.html"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)
pages_remaining = True
page_num = 1
while pages_remaining:
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_table = soup.select_one("#our-table")
    rows = tag_table.find_all("tr")
    csvfile = "tmp_NBA_Products" + str(page_num) + ".csv"
    with open(csvfile, "w+", newline="", encoding="utf8") as fp:
        writer = csv.writer(fp)
        for row in rows:
            lst = []
            for cell in row.find_all(["td", "th"]):
                lst.append(cell.text.replace("\n", "").replace("\r", "").strip())
            writer.writerow(lst)
    print("儲存頁面:", page_num)
    try:
        next_link = driver.find_element(By.CLASS_NAME, "nextbtn")
        if next_link:
            next_link.click()
            time.sleep(1)  # 等1秒
            page_num = page_num + 1
        else:
            pages_remaining = False
    except Exception:
        pages_remaining = False

driver.close()  # 關閉瀏覽器視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome

driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
# tag_ol = driver.find_element_by_xpath("/html/body/ol")  old
tag_ol = driver.find_element(By.XPATH, "/html/body/ol")  # 單數

print(tag_ol.tag_name)
# tags_li = tag_ol.find_elements_by_xpath("//li") old
tags_li = tag_ol.find_elements(By.XPATH, "//li")

for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://rent.housefun.com.tw/region/�x�_��/?cid=0000"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")
div = soup.find("div", id="SearchContent")
items = div.find_all("article")
print(len(items))
for item in items:
    title = item.find("h3", class_="title").find("a")
    if title:
        print(title.text)
    address = item.find("address", class_="addr")
    if address:
        print(address.text.strip())
    price = item.find("span", class_="infos num")
    if price:
        print(price.text)
    print("-------------------")

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("在 google / youtube / yahoo / 維基百科 輸入搜尋字串, 並存圖")

driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox

search_word = "獅子"

print("在 google 輸入搜尋字串 NG")

url = "https://www.google.com/"
driver.get(url)  # 開啟網址

time.sleep(1)  # 等1秒

"""
Copy element 或 Copy outerHTML
<textarea class="gLFyf" jsaction="paste:puy29d;" id="APjFqb" maxlength="2048" name="q" rows="1"
aria-activedescendant="" aria-autocomplete="both" aria-controls="Alh6id" aria-expanded="false"
aria-haspopup="both" aria-owns="Alh6id" autocapitalize="off" autocomplete="off" autocorrect="off"
autofocus="" role="combobox" spellcheck="false" title="Google 搜尋" type="search" value="" aria-label="搜尋"
data-ved="0ahUKEwjBkLT1_7L_AhWhrVYBHSArAb0Q39UDCAY" style=""></textarea>
"""

# 使用 class, ok
# txt = driver.find_element(By.CLASS_NAME, "gLFyf") # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, ok
# txt = driver.find_element(By.ID, "APjFqb")        # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
txt = driver.find_element(By.NAME, "q")  # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)

time.sleep(1)  # 等1秒

txt.clear()
search_word = "老虎"
txt.send_keys(search_word)

time.sleep(1)  # 等1秒

txt.send_keys(Keys.RETURN)

time.sleep(1)  # 等1秒

driver.save_screenshot("screenshot_google.png")  # 存圖

time.sleep(1)  # 等1秒

print("------------------------------")  # 30個

print("在 youtube 輸入搜尋字串 OK")

url = "https://www.youtube.com/"
driver.get(url)  # 開啟網址

time.sleep(1)  # 等1秒

"""
Copy element 或 Copy outerHTML
<input id="search" autocapitalize="none" autocomplete="off" autocorrect="off"
name="search_query" tabindex="0" type="text" spellcheck="false" placeholder="搜尋"
aria-label="搜尋" role="combobox" aria-haspopup="false" aria-autocomplete="list"
dir="ltr" class="ytd-searchbox" style="outline: none;">
"""

# 使用 class, fail
# txt = driver.find_element(By.CLASS_NAME, "ytd-searchbox") # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, fail
# txt = driver.find_element(By.ID, "search")        # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
txt = driver.find_element(
    By.NAME, "search_query"
)  # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)

time.sleep(1)  # 等1秒

txt.send_keys(Keys.RETURN)

time.sleep(1)  # 等1秒

driver.save_screenshot("screenshot_youtube.png")  # 存圖

time.sleep(1)  # 等1秒

print("------------------------------")  # 30個

print("在 yahoo 輸入搜尋字串")

url = "https://tw.yahoo.com/?p=us"
driver.get(url)  # 開啟網址

time.sleep(1)  # 等1秒

"""
Copy element 或 Copy outerHTML
<input type="text" id="header-search-input" aria-autocomplete="both"
aria-label="" placeholder="基隆民宿" data-term-type="revenue" autocapitalize="off" autocomplete="off"
class="Bgc(#fff) Bd Bdrsbstart(4px) Bdc(#b0b0b0) Bdendw(0)  Bdrststart(4px) Bxsh(n) Bxz(bb) D(b) Fz(18px) H(inh) M(0) O(0)  W(100%) Bdc($c-fuji-blue-1-c):f Bdc(#949494):h Bdrsbend(4px) Bdrstend(4px) Pstart(10px) Pend(110px) Pos(r) Z(2)"
name="p" role="combobox" data-rapid_p="2" data-v9y="1">
"""

# 使用 class, fail
# txt = driver.find_element(By.CLASS_NAME, "ytd-searchbox") # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, ok
txt = driver.find_element(
    By.ID, "header-search-input"
)  # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
# txt = driver.find_element(By.NAME, "p")             # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)

time.sleep(1)  # 等1秒

txt.send_keys(Keys.RETURN)

time.sleep(1)  # 等1秒

driver.save_screenshot("screenshot_yahoo.png")  # 存圖

time.sleep(1)  # 等1秒

print("------------------------------")  # 30個

print("在 維基百科 輸入搜尋字串 NG")

url = "https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5"
driver.get(url)  # 開啟網址

time.sleep(1)  # 等1秒

"""
Copy element 或 Copy outerHTML
<input class="vector-search-box-input" type="search" name="search"
placeholder="搜尋維基百科" aria-label="搜尋維基百科" autocapitalize="sentences"
title="搜尋維基百科[alt-shift-f]" accesskey="f" id="searchInput" autocomplete="off">
"""

# 使用 class
txt = driver.find_element(
    By.CLASS_NAME, "vector-search-box-input"
)  # 取得 class 為 xxxx 的網頁元素 ( TextArea )
# 使用 id, ok
# txt = driver.find_element(By.ID, "searchInput")        # 取得 id 為 xxxx 的網頁元素 ( TextArea )
# 使用 name, ok
# txt = driver.find_element(By.NAME, "search")             # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys(search_word)

time.sleep(1)  # 等1秒

txt.send_keys(Keys.RETURN)

time.sleep(1)  # 等1秒

driver.save_screenshot("screenshot_wiki.png")  # 存圖

time.sleep(1)  # 等1秒

"""
print("準備關閉瀏覽器")
time.sleep(3)  # 等3秒
driver.close()  # 關閉瀏覽器視窗
driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import json

url = "https://www.momoshop.com.tw/search/searchShop.jsp?keyword=nike NBA&searchType=1&curPage=1&_isFuzzy=0&showType=chessboardType"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

items = []
count = 1
page = 1
while True:
    print("抓取: 第" + str(page) + "頁 網路資料中...")
    page = page + 1
    soup = BeautifulSoup(driver.page_source, "lxml")
    tag_ul = soup.select_one("div.listArea > ul")
    tag_lis = tag_ul.find_all("li")
    for tag_li in tag_lis:
        title = tag_li.find("h3", class_="prdName")
        price = tag_li.find("span", class_="price").find("b")
        items.append({"id": count, "title": title.text, "price": price.text})
        print("已經擷取:", count, "筆")
        count = count + 1

    btn_css = "div.pageArea.topPage > dl > dd > a"
    # button = driver.find_elements_by_css_selector(btn_css)
    button = driver.find_elements(By.CSS_SELECTOR, btn_css)
    print('取得button個數 :', len(button))
    if len(button)>0:
        if button[len(button) - 1].text == "下一頁":
            button[len(button) - 1].click()
        else:
            break
        time.sleep(1)  # 等1秒
    else:
        break

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

with open("momo_items.json", "w", encoding="utf-8") as fp:
    json.dump(items, fp, indent=2, sort_keys=True, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

print("標題 :", driver.title)

# tags = driver.find_elements_by_xpath('//*[@id="video-title"]') old
tags = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

links = []
for tag in tags:
    href = tag.get_attribute("href")
    if href:
        links.append(href)
        print(href)
print(len(links))

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

print("標題 :", driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")
tags = soup.select("#video-title")
links = []
for tag in tags:
    href = tag["href"]
    if href:
        links.append(href)
        print(href)
print(len(links))

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

print("標題 :", driver.title)

# tags = driver.find_elements_by_xpath('//*[@id="video-title"]') old
tags = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

links = []
for tag in tags:
    href = tag.get_attribute("href")
    links.append(href)
print(len(links))

wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip("https://www.youtube.com/watch?v=")
    title = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#container > h1"))
    ).text
    description = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#description"))
    ).text
    print("編號:", num)
    print("名稱:", title.strip())
    print("描述:", description.strip())
    print("---------------------------")

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://www.youtube.com/results?search_query=pytube3"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

print("標題 :", driver.title)

for x in range(5):
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)
    time.sleep(1)  # 等1秒

# tags = driver.find_elements_by_xpath('//*[@id="video-title"]') old
tags = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

links = []
for tag in tags:
    href = tag.get_attribute("href")
    if href:
        links.append(href)
print(len(links))

df = pd.DataFrame(columns=["id", "title", "description"])
wait = WebDriverWait(driver, 10)
for link in links:
    driver.get(link)
    num = link.strip("https://www.youtube.com/watch?v=")
    title = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#container > h1"))
    ).text
    description = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#description"))
    ).text
    df.loc[len(df)] = [num, title, description]

print(df.head())
df.to_csv("YouTube.csv", index=False, encoding="utf-8")

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.bloomberg.com/quote/SPX:IND"
url = "https://www.bloomberg.com/quote/CCMP:IND"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")

regex = re.compile("^companyName.*")
name_box = soup.find("h1", class_=regex)
name = name_box.text
print(name)
price_box = soup.find("span", attrs={"class": re.compile("^priceText.*")})
price = price_box.text
print(price)

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
url = "https://www.thsrc.com.tw/#index-tab-01"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)

# 輸入出發站
# driver.find_element_by_id("StartStation").send_keys(ss)  # old
driver.find_element(By.ID, "StartStation").send_keys(ss)

# 輸入到達站
# driver.find_element_by_id("EndStation").send_keys(es)  # old
driver.find_element(By.ID, "EndStation").send_keys(es)

# 輸入日期
# driver.find_element_by_id("DepartueSearchDate").click()  # old
driver.find_element(By.ID, "DepartueSearchDate").click()

# driver.find_element_by_id("DepartueSearchDate").send_keys(dd)  # old
driver.find_element(By.ID, "DepartueSearchDate").send_keys(dd)

# 輸入時間
# driver.find_element_by_id("DepartueSearchTime").click()  # old
driver.find_element(By.ID, "DepartueSearchTime").click()

# driver.find_element_by_id("DepartueSearchTime").send_keys(dt)  # old
driver.find_element(By.ID, "DepartueSearchTime").send_keys(dt)

# driver.find_element_by_id("SearchButton").click()  # 按查詢鈕  # old
driver.find_element(By.ID, "SearchButton").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)

# 按我同意
# driver.find_element_by_xpath("//button[@class='swal2-confirm swal2-styled']").click() old
driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()

# 輸入出發站
# driver.find_element_by_id("select_location01").send_keys(ss)  # old
driver.find_element(By.ID, "select_location01").send_keys(ss)

# #輸入到達站
# driver.find_element_by_id("select_location02").send_keys(es) # old
driver.find_element(By.ID, "select_location02").send_keys(es)

# 輸入日期
# driver.find_element_by_id("Departdate03").click() # old
driver.find_element(By.ID, "Departdate03").click()

# driver.find_element_by_xpath("//div[@id='tot-1']/div/div/ul/li/div/div/table/tbody/tr[2]/td[1]").click() old
driver.find_element(By.XPATH, "//div[@id='tot-1']/div/div/ul/li/div/div/table/tbody/tr[2]/td[1]").click()

# 輸入時間
# driver.find_element_by_id("outWardTime").click() # old
driver.find_element(By.ID, "outWardTime").click()

# driver.find_element_by_xpath("//div[@id='tot-1']/div[2]/div/ul/li[2]/div/div/table/tr[3]/td[3]/a/i").click() old
driver.find_element(By.XPATH, "//div[@id='tot-1']/div[2]/div/ul/li[2]/div/div/table/tr[3]/td[3]/a/i").click()

# driver.find_element_by_id("start-search").click()  # 按查詢鈕 old
driver.find_element(By.ID, "start-search").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)

# 執行自動登入動作
# driver.find_element_by_id("StartStation").send_keys(ss)  # 輸入郵件  # old
driver.find_element(By.ID, "StartStation").send_keys(ss)  # 輸入郵件
# driver.find_element_by_id("EndStation").send_keys(es)  # 輸入密碼密碼  # old
driver.find_element(By.ID, "EndStation").send_keys(es)  # 輸入密碼密碼
# driver.find_element_by_id("DepartueSearchDate").click()  # old
driver.find_element(By.ID, "DepartueSearchDate").click()
# driver.find_element_by_id("DepartueSearchDate").send_keys(dd)  # 輸入  # old
driver.find_element(By.ID, "DepartueSearchDate").send_keys(dd)  # 輸入
# driver.find_element_by_id("DepartueSearchTime").click()  # old
driver.find_element(By.ID, "DepartueSearchTime").click()
# driver.find_element_by_id("DepartueSearchTime").send_keys(dt)  # 輸入密碼  # old
driver.find_element(By.ID, "DepartueSearchTime").send_keys(dt)  # 輸入密碼
# driver.find_element_by_id("SearchButton").click()  # 按登入鈕  # old
driver.find_element(By.ID, "SearchButton").click()  # 按登入鈕

# 以下本來就沒用到
# driver.find_element_by_id("StartStation").click()
# Select(driver.find_element_by_id("StartStation")).select_by_visible_text(u"台中站")
# driver.find_element_by_id("StartStation").click()
# driver.find_element_by_id("EndStation").click()
# Select(driver.find_element_by_id("EndStation")).select_by_visible_text(u"台北站")
# driver.find_element_by_id("EndStation").click()
# driver.find_element_by_id("DepartueSearchDate").click()
# driver.find_element_by_link_text("26").click()
# driver.find_element_by_id("DepartueSearchTime").click()
# Select(driver.find_element_by_id("DepartueSearchTime")).select_by_visible_text("09:00")
# driver.find_element_by_id("DepartueSearchTime").click()
# driver.find_element_by_id("SearchButton").click()

# url = "http://www.thsrc.com.tw/tw/TimeTable/Search"
#
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
# }
#
# form_data = {
#    "StartStationName":"南港站",
#    "EndStationName":"台南站",
#    "SearchType":"S",
#    "StartStation":"2f940836-cedc-41ef-8e28-c2336ac8fe68",
#    "EndStation":"9c5ac6ca-ec89-48f8-aab0-41b738cb1814",
#    "DepartueSearchDate":"2019/04/02",
#    "DepartueSearchTime":"09:00",
#    "DepartueTrainCode":"",
#    "DestinationSearchDate":"",
#    "DestinationSearchTime":"",
#    "DiscountType":""
# }
#
# response = requests.post(url, headers=headers, data=form_data)
#
# jsdata = response.json()
#
##print(jsdata["data"])
# jsdata

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 是可以連到google網站，但是輸入字串後，按確定
# 他會出現系統偵測到機器人，需要人工驗證，

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("明志科技大學")  # 輸入表單資料
time.sleep(1)  # 等1秒
search_box.submit()  # 送出表單

print("------------------------------")  # 30個

url = "http://www.google.com"

# 對此網站 不可用  Chrome
# driver = webdriver.Chrome()  # 使用Chrome
driver = webdriver.Firefox()  # 使用Firefox

driver.get(url)  # 打開瀏覽器，開啟網頁

txtBox = driver.find_element(By.NAME, "q")
txtBox.send_keys("明志科技大學")  # 輸入表單資料
time.sleep(1)  # 等1秒
txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome(options=opt)  # 使用Chrome

url = "google.com"

#driver = webdriver.Chrome()  # 使用Chrome
driver = webdriver.Firefox()  # 使用Firefox

driver.get(url)  # 打開瀏覽器，開啟網頁
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()  # 使用Chrome
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
print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

# 從載入後的動態網頁裡，找到指定的元素
imgCount = driver.find_element(By.CSS_SELECTOR, "CSS 選擇器")

print("------------------------------")  # 30個

from selenium.webdriver.common.action_chains import ActionChains

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
actions = ActionChains(driver)
# 滑鼠先移到 submitBtn 上，然後再點擊 submitBtn
actions.move_to_element(submitBtn).click(submitBtn)
actions.perform()

print("------------------------------")  # 30個

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")

time.sleep(1)  # 等1秒

submitBtn.click()

time.sleep(1)  # 等1秒

submitBtn.click()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.common.alert import Alert

url = "https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒
driver.execute_script("window.scrollTo(0, 500)")  # 捲動到 500px 位置
time.sleep(1)  # 等1秒
driver.execute_script("window.scrollTo(0, 2500)")  # 捲動到 2500px 位置
time.sleep(1)  # 等1秒
driver.execute_script("window.scrollTo(0, 0)")  # 捲動到 0px 位置

h1 = driver.find_element(By.TAG_NAME, "h1")
h3 = driver.find_element(By.TAG_NAME, "h3")

script = """
  let h1 = arguments[0];
  let h3 = arguments[1];
  alert(h1, h3)
"""

driver.execute_script(script, h1, h3)  # 執行 JavaScript，印出元素

time.sleep(1)  # 等1秒

Alert(driver).accept()  # 點擊提示視窗的確認按鈕，關閉提示視窗

print("------------------------------------------------------------")  # 60個

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=opt)  # 使用Chrome
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
print("------------------------------------------------------------")  # 60個

url = "https://twitter.com"

driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒

driver.execute_script(f"window.scrollTo(0, 200)")  # 自動往下捲動 200px
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')  # 取得登入按鈕
login.click()  # 點擊登入按鈕

print("------------------------------------------------------------")  # 60個

time.sleep(1)  # 等1秒

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

time.sleep(1)  # 等1秒

try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")  # 輸入帳號
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()  # 如果按鈕是「下一步」或「Next」就點擊
            print("驗證使用者帳號，點擊下一步")
            break
    time.sleep(1)  # 等1秒
except:
    print("ok")
    time.sleep(1)  # 等1秒

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

time.sleep(1)  # 等1秒

textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")  # 在輸入框輸入文字
print("輸入文字")

time.sleep(1)  # 等1秒

imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")  # 提供圖片絕對路徑，上傳圖片
print("上傳圖片")

time.sleep(1)  # 等1秒

buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()  # 點擊推文按鈕
        print("推文完成")
        break

time.sleep(1)  # 等1秒

driver.close()  # 關閉瀏覽器視窗

print("------------------------------------------------------------")  # 60個

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")
opt.add_argument("--user-agent=%s" % user_agent)

driver = webdriver.Chrome(options=opt)  # 使用Chrome

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
driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒

driver.execute_script(f"window.scrollTo(0, 200)")
login = driver.find_element(By.CSS_SELECTOR, 'a[href="/login"]')
login.click()

time.sleep(1)  # 等1秒

username = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="username"]')
username.send_keys("你的 email")
print("輸入 email 完成")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "下一步" or i.text == "Next":
        i.click()
        print("點擊下一步")
        break

time.sleep(1)  # 等1秒

try:
    check = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="on"]')
    check.send_keys("你的帳號")
    buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
    for i in buttons:
        if i.text == "下一步" or i.text == "Next":
            i.click()
            print("驗證使用者帳號，點擊下一步")
            break
    time.sleep(1)  # 等1秒
except:
    print("ok")
    time.sleep(1)  # 等1秒

pwd = driver.find_element(By.CSS_SELECTOR, 'input[autocomplete="current-password"]')
pwd.send_keys("你的密碼")
print("輸入密碼")
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')

for i in buttons:
    if i.text == "登入" or i.text == "Log in":
        i.click()
        print("點擊登入")
        break

time.sleep(1)  # 等1秒

textbox = driver.find_element(By.CSS_SELECTOR, 'div[role="textbox"]')
textbox.send_keys("Hello World!I am Robot~ ^_^")
print("輸入文字")

time.sleep(1)  # 等1秒

imgInput = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="fileInput"]')
imgInput.send_keys("/Users/oxxo/Desktop/oxxo.png")
print("上傳圖片")

time.sleep(1)  # 等1秒

buttons = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"]')
for i in buttons:
    if i.text == "推文" or i.text == "Tweet":
        i.click()
        print("推文完成")
        break

time.sleep(1)  # 等1秒

driver.close()  # 關閉瀏覽器視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

e1 = driver.find_element_by_tag_name("head")  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name("title")  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到

driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

print("------------------------------------------------------------")  # 60個

url = "http://www.facebook.com"

opt = webdriver.ChromeOptions()  # ←建立選項物件
opt.add_experimental_option(
    "prefs",  # ←在選項物件中加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
driver = webdriver.Chrome(options=opt)  # 使用Chrome, 使用 options參數
driver.get(url)  # 打開瀏覽器，開啟網頁

# driver.find_element_by_id("email").send_keys("您的帳號")  # }  # old
driver.find_element(By.ID, "email").send_keys("您的帳號")

# driver.find_element_by_id("pass").send_keys("您的密碼")  # }輸入帳密並按登入鈕  # old
driver.find_element(By.ID, "pass").send_keys("您的密碼")  # 輸入帳密並按登入鈕

# driver.find_element_by_name("login").click() old
driver.find_element(By.NAME, "login").click()

print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"

opt = webdriver.ChromeOptions()  # 建立選項物件
opt.add_experimental_option(
    "prefs",  # 加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
driver = webdriver.Chrome(options=opt)  # 使用Chrome, 使用 options參數
driver.get(url)  # 打開瀏覽器，開啟網頁

driver.maximize_window()  # ←將視窗最大化以避免最右邊的登入鈕沒顯示出來

# driver.find_element_by_id("gb_70").click()  # ←按登入鈕 old
driver.find_element(By.ID, "gb_70").click()  # 按登入鈕

time.sleep(1)  # 等1秒

# driver.find_element_by_id("identifierId").send_keys("您的帳號")  # }←輸入帳號
driver.find_element(By.ID, "identifierId").send_keys("您的帳號")  # 輸入帳號

# driver.find_element_by_id("identifierNext").click()  # ←按繼續鈕 old
driver.find_element(By.ID, "identifierNext").click()  # ←按繼續鈕

time.sleep(1)  # 等1秒

# driver.find_element_by_name("password").send_keys("您的密碼")  # ←輸入帳密 old
driver.find_element(By.NAME, "password").send_keys("您的密碼")  # ←輸入帳密

# driver.find_element_by_id("passwordNext").click()  # ←按繼續鈕  # old
driver.find_element(By.ID, "passwordNext").click()  # ←按繼續鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.wikipedia.org/"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 打開瀏覽器，開啟網頁

# txtBox = driver.find_element_by_id("searchInput") old
txtBox = driver.find_element(By.ID, "searchInput")

txtBox.send_keys("Artificial Intelligence")  # 輸入表單資料

time.sleep(1)  # 等1秒

txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://oxxo.studio"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

print("標題 :", driver.title)

time.sleep(1)  # 等1秒

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 捲動到最下方

time.sleep(1)  # 等1秒

for i in range(1, 7):
    # img = driver.find_element_by_xpath('//*[@id="content-grid"]/ul/li[' + str(i) + "]/a[1]/div/img") old
    img = driver.find_element(By.XPATH, '//*[@id="content-grid"]/ul/li[' + str(i) + "]/a[1]/div/img")
    response = requests.get(img.get_attribute("src"))
    with open("demo/test" + str(i) + ".jpg", "wb") as f:
        f.write(response.content)  # 將response.content二進位內容寫入檔案

driver.close()  # 關閉瀏覽器視窗

print("------------------------------------------------------------")  # 60個

url = "https://www.dinbendon.net/do/login"

options = webdriver.ChromeOptions()
options.add_argument("headless")  # 不會開啟瀏覽器

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

# 輸入使用者 id
# user = driver.find_element_by_xpath('//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input') old
user = driver.find_element(By.XPATH, '//*[@id="signInPanel_signInForm"]/table/tbody/tr[1]/td[2]/input')

user.send_keys("XXX")

# 輸入使用者密碼
# pwd = driver.find_element_by_xpath('//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input') old
pwd = driver.find_element(By.XPATH, '//*[@id="signInPanel_signInForm"]/table/tbody/tr[2]/td[2]/input')

pwd.send_keys("XXX")

# 取得驗證碼訊息
# checkquestion = driver.find_element_by_xpath('//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]') old
checkquestion = driver.find_element(By.XPATH, '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[1]')

# check = driver.find_element_by_xpath('//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input') old
check = driver.find_element(By.XPATH, '//*[@id="signInPanel_signInForm"]/table/tbody/tr[3]/td[2]/input')

# 計算驗證碼
checktext = checkquestion.text
print(checktext)
a = int(re.findall(r"\d+", checktext)[0])  # 使用正則表達式提取數字
b = int(re.findall(r"\d+", checktext)[1])
result = a + b
print(result)
check.send_keys(result)  # 輸入驗證碼

# 點擊按鈕
# btn = driver.find_element_by_xpath(' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]') old
btn = driver.find_element(By.XPATH, ' //*[@id="signInPanel_signInForm"]/table/tbody/tr[5]/td[2]/input[1]')

btn.click()

time.sleep(1)  # 等1秒

# 抓取第一筆便當名稱，加入例外處理
try:
    # menu = driver.find_element_by_xpath('//*[@id="inProgressBox_inProgressOrders_0"]/td[2]/div[1]/a/span[2]') old
    menu = driver.find_element(By.XPATH, '//*[@id="inProgressBox_inProgressOrders_0"]/td[2]/div[1]/a/span[2]')
    print(menu.text)
except:
    print("找不到便當名稱")

driver.close()  # 關閉瀏覽器視窗

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.google.com.tw/imghp?hl=zh-TW&tab=wi&ogbl"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

# search = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input') old
search = driver.find_element(By.XPATH, '//*[@id="sbtc"]/div/div[2]/input')

search.send_keys("林志玲")

# btn = driver.find_element_by_xpath('//*[@id="sbtc"]/button') old
btn = driver.find_element(By.XPATH, '//*[@id="sbtc"]/button')

btn.click()

for i in range(1, 6):
    time.sleep(0.5)  # 等0.5秒
    # div = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div["+ str(i)+ "]") old
    div = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div["+ str(i)+ "]")
    div.click()

    time.sleep(0.5)  # 等0.5秒
    # img = driver.find_element_by_xpath('//*[@id="irc-ss"]/div[' + str(i) + "]/div[1]/div[4]/div[1]/a/div/img") old
    img = driver.find_element(By.XPATH, '//*[@id="irc-ss"]/div[' + str(i) + "]/div[1]/div[4]/div[1]/a/div/img")
    src = img.get_attribute("src")
    print(src)
    if str(src) != "None":
        if ".jpg" in src:
            filename = src.split("/")[-1]
            response = requests.get(src)
            with open("demo/" + str(filename), "wb") as f:
                f.write(response.content)  # 將response.content二進位內容寫入檔案
                # closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]') old
                closeBtn = driver.find_element(By.XPATH, '//*[@id="irc_ccbc"]')
                closeBtn.click()
        else:
            # closeBtn = driver.find_element_by_xpath('//*[@id="irc_ccbc"]') old
            closeBtn = driver.find_element(By.XPATH, '//*[@id="irc_ccbc"]')
            closeBtn.click()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 網址處理
url_yahoo = "https://tw.bid.yahoo.com/search/auction/product?"
url_product = "kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime"
url = url_yahoo + url_product

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(5)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器

# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
# product_links = driver.find_elements_by_xpath(linkPath) old
product_links = driver.find_elements(By.XPATH, linkPath)

product_link = product_links[0].get_attribute("href")
print("商品連結 : ", product_link)
# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
# product_titles = driver.find_elements_by_xpath(titlePath) old
product_titles = driver.find_elements(By.XPATH, titlePath)
product_title = product_titles[0].get_attribute("textContent")
print("商品名稱 : ", product_title)
# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
# product_prices = driver.find_elements_by_xpath(pricePath) old
product_prices = driver.find_elements(By.XPATH, pricePath)
product_price = product_prices[0].text
print("商品價格 : ", product_price)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 網址處理
url_yahoo = "https://tw.bid.yahoo.com/search/auction/product?"
url_product = "kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime"
url = url_yahoo + url_product

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(5)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器

# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
# product_links = driver.find_elements_by_xpath(linkPath) old
product_links = driver.find_elements(By.XPATH, linkPath)

# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
# product_titles = driver.find_elements_by_xpath(titlePath) old
product_titles = driver.find_elements(By.XPATH, titlePath)

# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
# product_prices = driver.find_elements_by_xpath(pricePath) old
product_prices = driver.find_elements(By.XPATH, pricePath)

# 計算商品數量
num = len(product_titles)
print("商品數量 : ", num)
print("-" * 50)

# 列出商品資訊
for title, link, price in zip(product_titles, product_links, product_prices):
    print("商品名稱 : ", title.get_attribute("textContent"))
    print("商品連結 : ", link.get_attribute("href"))
    print("商品價格 : ", price.text)
    print("-" * 70)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 搜尋條件
city = "台北巿"
checkin_time = "2019-11-24"
checkout_time = "2019-11-25"
# 網址處理
url = "https://tw.hotels.com/"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器

time.sleep(1)  # 等1秒

# searchNode = driver.find_elements_by_xpath("//input[contains(@id,'q-destination')]") old
searchNode = driver.find_elements(By.XPATH, "//input[contains(@id,'q-destination')]")

# checkInNode = driver.find_elements_by_xpath("//input[contains(@id,'q-localised-check-in')]") old
checkInNode = driver.find_elements(By.XPATH, "//input[contains(@id,'q-localised-check-in')]")

# checkOutNode = driver.find_elements_by_xpath("//input[contains(@id,'q-localised-check-out')]") old
checkOutNode = driver.find_elements(By.XPATH, "//input[contains(@id,'q-localised-check-out')]")

# 輸入搜尋關鍵資料
searchNode[0].clear()  # 清除城市欄位
searchNode[0].send_keys(city)  # 輸入搜尋城市

time.sleep(1)  # 等1秒

searchNode[0].send_keys(Keys.TAB)  # 按Tab跳到check in欄位
checkInNode[0].clear()  # 清除check in欄位
checkInNode[0].send_keys(checkin_time)  # 輸入check in時間

time.sleep(1)  # 等1秒

searchNode[0].send_keys(Keys.TAB)  # 按Tab跳至check out欄位
checkOutNode[0].clear()  # 清除check out欄位
checkOutNode[0].send_keys(checkout_time)  # 輸入check out時間

time.sleep(1)  # 等1秒

checkOutNode[0].send_keys(Keys.ENTER)  # 表單按Enter表示輸入完成

time.sleep(1)  # 等1秒

# 旅館名稱
hotelPath = "//ol[@class='listings infinite-scroll-enabled']//h3/a"
# names = driver.find_elements_by_xpath(hotelPath) old
names = driver.find_elements(By.XPATH, hotelPath)

name = names[0].text
print("旅館名稱 : ", name)

# 旅館地址
addressPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='address']"
# addresses = driver.find_elements_by_xpath(addressPath) old
addresses = driver.find_elements(By.XPATH, addressPath)

address = addresses[0].text
print("旅館地址 : ", address)

# 旅館星級評價
starPath = (
    "//ol[@class='listings infinite-scroll-enabled']//span[@class='star-rating-text']"
)
# stars = driver.find_elements_by_xpath(starPath) old
stars = driver.find_elements(By.XPATH, starPath)

star = stars[0].text
print("旅館星級 : ", star)

# 旅館定價
listingpricePath = (
    "//ol[@class='listings infinite-scroll-enabled']//del[@data-reason='DRR-448']"
)
# lprices = driver.find_elements_by_xpath(listingpricePath) old
lprices = driver.find_elements(By.XPATH, listingpricePath)

lprice = lprices[0].text  # 定價listing price
print("旅館定價 : ", lprice)

# 旅館售價
pricePath = "//ol[@class='listings infinite-scroll-enabled']//ins[@class='special-deal-animation']"
# prices = driver.find_elements_by_xpath(pricePath) old
prices = driver.find_elements(By.XPATH, pricePath)

price = prices[0].text  # 售價
print("旅館售價 : ", price)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 搜尋條件
city = "台北市"
checkin_time = "2019-11-24"
checkout_time = "2019-11-25"
# 網址處理
url = "https://tw.hotels.com/"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(10)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器

time.sleep(1)  # 等1秒

#searchNode = driver.find_elements_by_xpath("//input[contains(@id,'q-destination')]") old
searchNode = driver.find_elements(By.XPATH, "//input[contains(@id,'q-destination')]")

#checkInNode = driver.find_elements_by_xpath("//input[contains(@id,'q-localised-check-in')]") old
checkInNode = driver.find_elements(By.XPATH, "//input[contains(@id,'q-localised-check-in')]")

#checkOutNode = driver.find_elements_by_xpath("//input[contains(@id,'q-localised-check-out')]") old
checkOutNode = driver.find_elements(By.XPATH, "//input[contains(@id,'q-localised-check-out')]")

# 輸入搜尋關鍵資料
searchNode[0].clear()  # 清除城市欄位
searchNode[0].send_keys(city)  # 輸入搜尋城市

time.sleep(1)  # 等1秒

searchNode[0].send_keys(Keys.TAB)  # 按Tab跳到check in欄位
checkInNode[0].clear()  # 清除check in欄位
checkInNode[0].send_keys(checkin_time)  # 輸入check in時間

time.sleep(1)  # 等1秒

searchNode[0].send_keys(Keys.TAB)  # 按Tab跳至check out欄位
checkOutNode[0].clear()  # 清除check out欄位
checkOutNode[0].send_keys(checkout_time)  # 輸入check out時間

time.sleep(1)  # 等1秒

checkOutNode[0].send_keys(Keys.ENTER)  # 表單按Enter表示輸入完成

time.sleep(1)  # 等1秒

# 旅館名稱
hotelPath = "//ol[@class='listings infinite-scroll-enabled']//h3/a"
# names = driver.find_elements_by_xpath(hotelPath) old
names = driver.find_elements(By.XPATH, hotelPath)

# 旅館地址
addressPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='address']"
# addresses = driver.find_elements_by_xpath(addressPath) old
addresses = driver.find_elements(By.XPATH, addressPath)

# 旅館星級評價
starPath = (
    "//ol[@class='listings infinite-scroll-enabled']//span[@class='star-rating-text']"
)

# stars = driver.find_elements_by_xpath(starPath) old
stars = driver.find_elements(By.XPATH, starPath)

# 旅館定價
listingpricePath = (
    "//ol[@class='listings infinite-scroll-enabled']//del[@data-reason='DRR-448']"
)

# lprices = driver.find_elements_by_xpath(listingpricePath) old
lprices = driver.find_elements(By.XPATH, listingpricePath)

# 計算旅館數量
num = len(names)
print("旅館數量 : ", num)
print("-" * 70)
# 列出系列旅館資訊
for name, address, star, lprice in zip(names, addresses, stars, lprices):
    print("旅館名稱 : ", name.text)
    print("旅館地址 : ", address.text)
    print("旅館星級 : ", star.text)
    print("旅館定價 : ", lprice.text)
    print("-" * 70)
    time.sleep(1)  # 等1秒

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 登入 facebook

# 會出現 Alert 視窗
url = "https://www.facebook.com/"
email = "您的 Email 帳號"
password = "您的密碼"

driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox

# 取消 Alert 視窗
# url = 'https://www.facebook.com/'
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)  # 使用Chrome

driver.get(url)

# 執行自動登入動作
# driver.find_element_by_id("email").clear() old
driver.find_element(By.ID, "email").clear()

# driver.find_element_by_id("email").send_keys(email) old
driver.find_element(By.ID, "email").send_keys(email)

time.sleep(1)  # 等1秒 # 必須加入等待，否則會有誤動作

# driver.find_element_by_id("pass").clear() old
driver.find_element(By.ID, "pass").clear()

# driver.find_element_by_id("pass").send_keys(password) old
driver.find_element(By.ID, "pass").send_keys(password)

# driver.find_element_by_id("loginbutton").click()  # 按 登入 鈕 old
driver.find_element(By.ID, "loginbutton").click()  # 按 登入 鈕

# driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox

driver.get(url)

# 執行自動登入動作
# driver.find_element_by_id("email").clear() old
driver.find_element(By.ID, "email").clear()

# driver.find_element_by_id("email").send_keys(email)  # 輸入郵件 old 
driver.find_element(By.ID, "email").send_keys(email)  # 輸入郵件

time.sleep(1)  # 等1秒 # 必須加入等待，否則會有誤動作

# driver.find_element_by_id("pass").clear() old
driver.find_element(By.ID, "pass").clear()

# driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼 old
driver.find_element(By.ID, "pass").send_keys(password)  # 輸入密碼

# driver.find_element_by_id("loginbutton").click()  # 按登入鈕 old
driver.find_element(By.ID, "loginbutton").click()  # 按登入鈕

"""
print("準備關閉瀏覽器")
time.sleep(3)  # 等3秒
driver.close()  # 關閉瀏覽器視窗
driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# url = 'https://example.oxxostudio.tw/python/selenium/demo.html'
url = "D:/_git/vcs/_1.data/______test_files1/webdriver_data.html"  # NG
url = "D:/_git/vcs/_1.data/______test_files1/webdriver_data_old.html"

from selenium.webdriver.support.select import Select  # 使用 Select 對應下拉選單

driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 開啟網址

txt = driver.find_element(By.ID, "show")  # 取得 id 為 show 的網頁元素 ( TextArea )
a = driver.find_element(By.ID, "aaa")  # 取得 id 為 aaa 的網頁元素 ( 按鈕 AAA )
b = driver.find_element(By.NAME, "bbb")  # 取得屬性 name 為 bbb 的網頁元素 ( 按鈕 BBB )
c = driver.find_element(By.CLASS_NAME, "ccc")  # 取得 class 為 ccc 的網頁元素 ( 按鈕 CCC )
d = driver.find_element(
    By.CSS_SELECTOR, ".ddd"
)  # 取得 class 為 ddd 的網頁元素 ( 按鈕 DDD ), 多一個.
h1 = driver.find_element(By.TAG_NAME, "h1")  # 取得 tag h1 的網頁元素
link1 = driver.find_element(By.LINK_TEXT, "點擊開啟 Google 網站")  # 取得指定超連結文字的網頁元素
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, "Google")  # 取得超連結文字包含 Google 的網頁元素
select = Select(
    driver.find_element(By.XPATH, "/html/body/select")
)  # 取得 html > body > select 這個網頁元素
print("輸入文字")
txt.send_keys("在TextArea輸入一些文字")
print(txt.text)  # 印出 txt 元素的內容

time.sleep(1)  # 等1秒

print("點擊 AAA")
a.click()  # 點擊 a
print(a.text)  # 印出 a 元素的內容

time.sleep(1)  # 等1秒

print("點擊 BBB")
b.click()  # 點擊 b
print(b.text)  # 印出 b 元素的內容

time.sleep(1)  # 等1秒

print("點擊 CCC")
c.click()  # 點擊 c
print(c.text)  # 印出 c 元素的內容

time.sleep(1)  # 等1秒

print("點擊 DDD")
d.click()  # 點擊 d
print(d.text)  # 印出 d 元素的內容

time.sleep(1)  # 等1秒

print("下拉式選單")
select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )

time.sleep(1)  # 等1秒

print("點擊 h1")
h1.click()  # 點擊 h1

time.sleep(1)  # 等1秒

print("點擊 link1")
link1.click()  # 點擊 link1

time.sleep(1)  # 等1秒

print("點擊 link2")
link2.click()  # 點擊 link2
print(link2.get_attribute("href"))  # 印出 link2 元素的 href 屬性

time.sleep(1)  # 等1秒

"""
print("準備關閉瀏覽器")
time.sleep(3)  # 等3秒
driver.close()  # 關閉瀏覽器視窗
driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PyAutoGUI，自動控制滑鼠與鍵盤
import pyautogui as auto

url = 'https://www.google.com/'

driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒

txt = driver.find_element(By.NAME, 'q')  # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys('this is a lion-mouse')
time.sleep(1)  # 等1秒

print(txt.tag_name)
print(txt.get_attribute("type"))
print(txt.get_attribute("id"))

txt.submit()    #就是按了enter

# url = 'https://tw.yahoo.com/'
driver.get(url)  # 打開瀏覽器，開啟網頁
time.sleep(1)  # 等1秒

auto.PAUSE = 1

x_st = 60
y_st = 140
print("move to (", x_st, ", ", y_st, ")")
auto.moveTo(x_st, y_st, 2)
time.sleep(1)  # 等1秒
auto.click()
auto.typewrite("獅子")
auto.click()

x_st = 60
y_st = 200
time.sleep(1)  # 等1秒
print("move to (", x_st, ", ", y_st, ")")
auto.moveTo(x_st, y_st, 2)
time.sleep(1)  # 等1秒
auto.click()
time.sleep(1)  # 等1秒

y_st += 22
time.sleep(1)  # 等1秒
print("move to (", x_st, ", ", y_st, ")")
auto.moveTo(x_st, y_st, 2)
time.sleep(1)  # 等1秒
auto.click()
time.sleep(1)  # 等1秒

y_st += 22
time.sleep(1)  # 等1秒
print("move to (", x_st, ", ", y_st, ")")
auto.moveTo(x_st, y_st, 2)
time.sleep(1)  # 等1秒
auto.click()
time.sleep(1)  # 等1秒

y_st += 22
time.sleep(1)  # 等1秒
print("move to (", x_st, ", ", y_st, ")")
auto.moveTo(x_st, y_st, 2)
time.sleep(1)  # 等1秒
auto.click()
time.sleep(1)  # 等1秒

y_st += 22
time.sleep(1)  # 等1秒
print("move to (", x_st, ", ", y_st, ")")
auto.moveTo(x_st, y_st, 2)
time.sleep(1)  # 等1秒
auto.click()
time.sleep(1)  # 等1秒

"""
print("準備關閉瀏覽器")
time.sleep(3)  # 等3秒
driver.close()  # 關閉瀏覽器視窗
driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PyAutoGUI，自動控制滑鼠與鍵盤

# 有問題

import pyautogui as auto
import pandas as pd

driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox

# 台灣證券交易所
url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
driver.get(url)

time.sleep(1)  # 等1秒

auto.PAUSE = 3
auto.moveTo(1263, 438, 2)
auto.click()
auto.typewrite("2330")
auto.moveTo(1461, 438, 2)
auto.click()

time.sleep(1)  # 等1秒

html = driver.page_source  # 網頁原始碼

""" 找不到資料
data = pd.read_html(html)
print(data)
"""
print("------------------------------")  # 30個

import pyautogui as auto
import pandas as pd

stocks = [
    {"name": "聯電", "id": "2303"},
    {"name": "台積電", "id": "2330"},
    {"name": "華碩", "id": "2357"},
]

driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox

# 台灣證券交易所
url = "https://www.twse.com.tw/zh/page/trading/2303/STOCK_DAY.html"
driver.get(url)

auto.PAUSE = 3
for stock in stocks:
    auto.moveTo(1263, 438, 2)
    auto.doubleClick()
    auto.typewrite(stock["id"])
    auto.moveTo(1461, 438, 2)
    auto.click()
    time.sleep(1)  # 等1秒
    html = driver.page_source  # 網頁原始碼
    """ 找不到資料
    data = pd.read_html(html)
    print(stock["name"])
    print(data[0])
    """

"""
print("準備關閉瀏覽器")
time.sleep(3)  # 等3秒
driver.close()  # 關閉瀏覽器視窗
driver.quit()  # 關閉瀏覽器視窗 並退出驅動程序
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.books.com.tw/web/books"
# url = 'https://www.google.com/

# driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()  # 使用Firefox

driver.maximize_window()
driver.get(url)

time.sleep(1)  # 等1秒

# driver.find_element_by_id("key").send_keys("文淵閣工作室")  # 輸入搜尋文字 old
driver.find_element(By.ID, "key").send_keys("文淵閣工作室")  # 輸入搜尋文字

time.sleep(1)  # 等1秒

# driver.find_element_by_xpath('//*[@id="search"]/button').click()  # 按 搜尋 鈕 old
driver.find_element(By.XPATH, '//*[@id="search"]/button').click()  # 按 搜尋 鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pyautogui
from PIL import ImageGrab

x1, x2 = 260, 300
y1_bird, y2_bird = 305, 378
y1_cactus, y2_cactus = 379, 465


def isCollision_day(data):  # 白天
    # 檢查高飛翼手龍出現
    for i in range(x1, x2):
        for j in range(y1_bird, y2_bird):
            if data[i, j] < 150:
                pyautogui.keyDown("down")
                time.sleep(0.5)  # 等0.5秒
                pyautogui.keyUp("down")
                return
    # 檢查仙人掌出現
    for i in range(x1, x2):
        for j in range(y1_cactus, y2_cactus):
            if data[i, j] < 150:
                pyautogui.keyDown("up")
                return
    return


def isCollision_night(data):  # 晚上
    for i in range(x1, x2):
        for j in range(y1_bird, y2_bird):
            if data[i, j] > 150:
                pyautogui.keyDown("down")
                time.sleep(0.5)  # 等0.5秒
                pyautogui.keyUp("down")
                return
    for i in range(x1, x2):
        for j in range(y1_cactus, y2_cactus):
            if data[i, j] > 150:
                pyautogui.keyDown("up")
                return
    return


time.sleep(1)  # 等1秒

pyautogui.keyDown("up")

while True:
    image = ImageGrab.grab().convert("L")
    data = image.load()
    if data[260, 300] > 150:
        isCollision_day(data)
    else:
        isCollision_night(data)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import threading


def download_pic(url, path):
    response = requests.get(url)  # 使用 GET 對圖片連結發出請求
    path += url[url.rfind(".") :]  # 將路徑加上圖片的副檔名
    f = open(path, "wb")  # 以指定的路徑建立一個檔案
    f.write(response.content)  # 將 HTTP Response 物件的 content寫入檔案中
    f.close()  # 關閉檔案


def get_photolist(photo_name, download_num):
    page = 1  # 初始頁數為1
    photo_list = []  # 建立空的圖片 list

    url = "https://pixabay.com/zh/"  # Pixabay 網址
    option = webdriver.ChromeOptions()  # ←↓加入選項來指定不要有自動控制的訊息
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser = webdriver.Chrome(options=option)  # 以指定的選項啟動 Chrome
    browser.get(url)  # 連線到高鐵購票網頁, ●●注意, Chrome出現訊息窗時不可按【停用】鈕, 請按 x 將之關閉, 或不理它也可。
    # browser.find_element_by_name("q").send_keys(photo_name) old
    browser.find_element(By.NAME, "q").send_keys(photo_name)
    # browser.find_element_by_name("q").send_keys(Keys.RETURN) old
    browser.find_element(By.NAME, "q").send_keys(Keys.RETURN)

    while True:
        html = browser.page_source
        #        print(html)
        soup = BeautifulSoup(html, "lxml")  # 解析網頁
        # 先尋找標籤為 div, calss 為 'flex_grid ...' 的元素 (這區中才是免負圖庫)
        #  再尋找所有標籤為 div, calss 為 'item' 的元素
        photo_item = soup.find(
            "div", {"class": "flex_grid credits search_results"}
        ).find_all("div", {"class": "item"})
        if len(photo_item) == 0:
            print("Error, no photo link in page", page)
            return None
        for i in range(len(photo_item)):
            # 尋找標籤 img 並取出 'src' 之中的內容
            photo = photo_item[i].find("img")["src"]
            if photo == "/static/img/blank.gif":
                # 尋找標籤 img 並取出 'data-lazy' 之中的內容
                photo = photo_item[i].find("img")["data-lazy"]
            if photo in photo_list:
                #                print('photo duplicated in photo_list at page', page, photo)
                continue
            # 若要下載較高解析度的圖, 可將下行取消註解
            #            photo = photo.replace('_340', '1280')  #更換為1280解析度
            photo_list.append(photo)  # 將找到的連結新增進 list 之中
            if len(photo_list) >= download_num:
                print("end by get photo list size", len(photo_list))
                browser.close()
                return photo_list
        page += 1  # 頁數加1
        # 找出下一頁的連結網址
        try:
            next = browser.find_element_by_partial_link_text("›").get_attribute("href")
            browser.get(next)
        except:  # 沒下一頁了
            browser.close()
            return photo_list


def create_folder(photo_name):
    folder_name = input("請輸入要儲存的資料夾名稱: ")

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在, 建立資料夾: " + folder_name)
    else:
        print("找到資料夾: " + folder_name)

    if not os.path.exists(folder_name + os.sep + photo_name):
        os.mkdir(folder_name + os.sep + photo_name)
        print("建立資料夾: " + photo_name)
    else:
        print(photo_name + " 資料夾已存在")
    return folder_name


def get_photobythread(folder_name, photo_name, photo_list):
    download_num = len(photo_list)  # 設定下載數量為圖片連結串列的長度
    Q = int(download_num / 100)  # 取商數
    R = download_num % 100  # 取餘數

    for i in range(Q):
        threads = []
        for j in range(100):
            threads.append(
                threading.Thread(
                    target=download_pic,
                    args=(
                        photo_list[i * 100 + j],
                        folder_name
                        + os.sep
                        + photo_name
                        + os.sep
                        + str(i * 100 + j + 1),
                    ),
                )
            )
            threads[j].start()
        for j in threads:
            j.join()
        print(int((i + 1) * 100 / download_num * 100), "%")  # 顯示當前進度

    threads = []
    for i in range(R):
        threads.append(
            threading.Thread(
                target=download_pic,
                args=(
                    photo_list[Q * 100 + i],
                    folder_name + os.sep + photo_name + os.sep + str(Q * 100 + i + 1),
                ),
            )
        )
        threads[i].start()
    for i in threads:
        i.join()
    print("100%")  # 顯示當前進度


print("------------------------------")  # 30個

import threading


def download_pic(url, path):
    response = requests.get(url)  # 使用 GET 對圖片連結發出請求
    path += url[url.rfind(".") :]  # 將路徑加上圖片的副檔名
    f = open(path, "wb")  # 以指定的路徑建立一個檔案
    f.write(response.content)  # 將 HTTP Response 物件的 content寫入檔案中
    f.close()  # 關閉檔案


def get_photolist(photo_name, download_num):
    page = 1  # 初始頁數為1
    photo_list = []  # 建立空的圖片 list

    url = "https://pixabay.com/zh/"  # Pixabay 網址
    option = webdriver.ChromeOptions()  # ←↓加入選項來指定不要有自動控制的訊息
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    browser = webdriver.Chrome(options=option)  # 以指定的選項啟動 Chrome
    # 連線到pixabay網頁, ●●注意, Chrome出現訊息窗時不可按【停用】鈕, 請按 x 將之關閉, 或不理它也可。
    browser.get(url)
    # browser.find_element_by_name("q").send_keys(photo_name) old
    browser.find_element(By.NAME, "q").send_keys(photo_name)
    # browser.find_element_by_name("q").send_keys(Keys.RETURN) old
    browser.find_element(By.NAME, "q").send_keys(Keys.RETURN)

    while True:
        html = browser.page_source
        #        print(html)
        soup = BeautifulSoup(html, "lxml")  # 解析網頁
        #  先尋找標籤為 div, calss 為 'flex_grid ...' 的元素 (這區中才是免費圖庫)
        #  再尋找所有標籤為 div, calss 為 'item' 的元素
        photo_item = soup.find(
            "div", {"class": "flex_grid credits search_results"}
        ).find_all("div", {"class": "item"})
        if len(photo_item) == 0:
            print("Error, no photo link in page", page)
            return None
        for i in range(len(photo_item)):
            # 尋找標籤 img 並取出 'src' 之中的內容
            photo = photo_item[i].find("img")["src"]
            if photo == "/static/img/blank.gif":
                # 尋找標籤 img 並取出 'data-lazy' 之中的內容
                photo = photo_item[i].find("img")["data-lazy"]
            if photo in photo_list:
                #                print('photo duplicated in photo_list at page', page, photo)
                continue
            # 若要下載較高解析度的圖, 可將下行取消註解
            #            photo = photo.replace('_340', '1280')  #更換為1280解析度
            photo_list.append(photo)  # 將找到的連結新增進 list 之中
            if len(photo_list) >= download_num:
                print("end by get photo list size", len(photo_list))
                browser.close()
                return photo_list
        page += 1  # 頁數加1
        # 找出下一頁的連結網址
        try:
            next = browser.find_element_by_partial_link_text("›").get_attribute("href")
            browser.get(next)
        except:  # 沒下一頁了
            browser.close()
            return photo_list


def create_folder(photo_name):
    folder_name = input("請輸入要儲存的資料夾名稱: ")

    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print("資料夾不存在, 建立資料夾: " + folder_name)
    else:
        print("找到資料夾: " + folder_name)

    if not os.path.exists(folder_name + os.sep + photo_name):
        os.mkdir(folder_name + os.sep + photo_name)
        print("建立資料夾: " + photo_name)
    else:
        print(photo_name + " 資料夾已存在")
    return folder_name


def get_photobythread(folder_name, photo_name, photo_list):
    download_num = len(photo_list)  # 設定下載數量為圖片連結串列的長度
    Q = int(download_num / 100)  # 取商數
    R = download_num % 100  # 取餘數

    for i in range(Q):
        threads = []
        for j in range(100):
            threads.append(
                threading.Thread(
                    target=download_pic,
                    args=(
                        photo_list[i * 100 + j],
                        folder_name
                        + os.sep
                        + photo_name
                        + os.sep
                        + str(i * 100 + j + 1),
                    ),
                )
            )
            threads[j].start()
        for j in threads:
            j.join()
        print(int((i + 1) * 100 / download_num * 100), "%")  # 顯示當前進度

    threads = []
    for i in range(R):
        threads.append(
            threading.Thread(
                target=download_pic,
                args=(
                    photo_list[Q * 100 + i],
                    folder_name + os.sep + photo_name + os.sep + str(Q * 100 + i + 1),
                ),
            )
        )
        threads[i].start()
    for i in threads:
        i.join()
    print("100%")  # 顯示當前進度


print("------------------------------------------------------------")  # 60個

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")

    download_num = int(input("請輸入要下載的數量: "))

    photo_list = get_photolist(photo_name, download_num)

    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break

folder_name = create_folder(photo_name)

print("開始下載...")

get_photobythread(folder_name, photo_name, photo_list)

print("\n下載完畢")

print("------------------------------")  # 30個

import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")

    download_num = int(input("請輸入要下載的數量: "))

    photo_list = m.get_photolist(photo_name, download_num)

    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break

print("開始下載...")

for i in range(len(photo_list)):
    m.download_pic(photo_list[i], str(i + 1))

print("\n下載完畢")

print("------------------------------------------------------------")  # 60個

import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")

    download_num = int(input("請輸入要下載的數量: "))

    photo_list = m.get_photolist(photo_name, download_num)

    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break

folder_name = m.create_folder(photo_name)

print("開始下載...")

for i in range(len(photo_list)):
    m.download_pic(
        photo_list[i], folder_name + os.sep + photo_name + os.sep + str(i + 1)
    )

print("\n下載完畢")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


# 6060
print("------------------------------------------------------------")  # 60個
# 3030
print("------------------------------")  # 30個
# 1515
print("---------------")  # 15個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
find_element

Selenium 4.3.0 及以上版本已正式移除所有 

find_element_by_*   與 
find_elements_by_*  系列方法。你需要改用統一的 

find_elements() 方法並搭配 By 模組來定位網頁元素。

# 舊寫法（Selenium 3，已失效）
# elements = driver.find_elements_by_css_selector("你的CSS選擇器")

# 新寫法（Selenium 4+）
element = driver.find_element(By.ID, "author")  # 單數
elements = driver.find_elements(By.CSS_SELECTOR, btn_css)  # 複數

"""


"""
其他常見定位方式對照表

如果程式碼中還有其他舊版的 find_element_by_* 語法，可以參考下表一併替換（若要尋找多個元素，只需將 find_element 改為 find_elements 即可）

舊版語法 (Selenium 3)				新版語法 (Selenium 4+)
driver.find_element_by_name("...")		driver.find_element(By.NAME, "...")
driver.find_element_by_id("...")		driver.find_element(By.ID, "...")
driver.find_element_by_xpath("...")		driver.find_element(By.XPATH, "...")
driver.find_element_by_class_name("...")	driver.find_element(By.CLASS_NAME, "...")
driver.find_element_by_css_selector("...")	driver.find_element(By.CSS_SELECTOR, "...")
driver.find_element_by_tag_name("...")		driver.find_element(By.TAG_NAME, "...")

"""

