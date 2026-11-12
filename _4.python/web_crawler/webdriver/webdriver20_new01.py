# url = 'https://example.oxxostudio.tw/python/selenium/demo.html'
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


"""
新進測試

"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 建立瀏覽器物件
driver = webdriver.Chrome()  # 使用Chrome
# driver = webdriver.Firefox()  # 使用Firefox
# driver = webdriver.Edge("./msedgedriver") # 還不能用
driver.set_window_position(0, 0)  # 設定視窗位置
driver.set_window_size(800, 600)  # 設定視窗大小
driver.maximize_window()  # 全螢幕顯示

print("------------------------------------------------------------")  # 60個

url = "http://aaa.24ht.com.tw"

driver = webdriver.Firefox()
driver = webdriver.Chrome()
print(type(driver))

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://aaa.24ht.com.tw"
driver.get(url)  # 網頁下載至瀏覽器
print(driver.page_source)  # 列印網頁原始碼

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://aaa.24ht.com.tw"
driver.get(url)  # 網頁下載至瀏覽器
print("瀏覽器名稱 = ", driver.name)  # 列印瀏覽器名稱
print("網頁url    = ", driver.current_url)  # 列印網頁url
print("網頁連線id = ", driver.session_id)  # 網頁連線id
print("瀏覽器功能 = \n", driver.capabilities)  # 瀏覽器功能設定訊息

print("------------------------------------------------------------")  # 60個

urls = [
    "http://aaa.24ht.com.tw",
    "http://www.mcut.edu.tw",
    "http://www.siliconstone.com",
]

driver = webdriver.Firefox()

for url in urls:
    driver.get(url)  # 網頁下載至瀏覽器
    time.sleep(5)

driver.quit()

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://aaa.24ht.com.tw"
driver.get(url)  # 網頁下載至瀏覽器

tag = driver.find_element_by_id("main")
print(tag.tag_name)

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://aaa.24ht.com.tw"
driver.get(url)  # 網頁下載至瀏覽器

try:
    tag = driver.find_element_by_id("main")
    print(tag.tag_name)
except:
    print("沒有找到相符的元素")

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://aaa.24ht.com.tw"
driver.get(url)  # 網頁下載至瀏覽器

print("網頁標題內容是 = ", driver.title)

tag2 = driver.find_element_by_id("author")  # 傳回<h1>
print("\n標籤名稱 = %s, 內容是 = %s " % (tag2.tag_name, tag2.text))

print()
tag3 = driver.find_elements_by_id("content")  # 傳回<h1>
for t3 in tag3:
    print("標籤名稱 = %s, 內容是 = %s " % (t3.tag_name, t3.text))

print()
tag4 = driver.find_elements_by_tag_name("p")  # 傳回<p>
for t4 in tag4:
    print("標籤名稱 = %s, 內容是 = %s " % (t4.tag_name, t4.text))

print()
tag5 = driver.find_elements_by_tag_name("img")  # 傳回<img>
for t5 in tag5:
    print("標籤名稱 = %s, 內容是 = %s " % (t5.tag_name, t5.get_attribute("src")))

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()
url = "d:\Web_Crawler\ch7\h7_1.html"
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element_by_xpath("//h4")
print(n1.text)
n2 = driver.find_element_by_xpath("//body/section/h4")
print(n2.text)
n3 = driver.find_element_by_xpath("//section/h4")
print(n3.text)
n4 = driver.find_element_by_xpath("//body/*/h4")
print(n4.text)

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()
url = "d:\Web_Crawler\ch7\h7_1.html"
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element_by_xpath("//p")
print(n1.text)

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()
url = "d:\Web_Crawler\ch7\h7_1.html"
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element_by_xpath("//section/p[1]")
print(n1.text)
n2 = driver.find_element_by_xpath("//section/p[2]")
print(n1.text)

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()
url = "d:\Web_Crawler\ch7\h7_1.html"
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element_by_xpath("//section/p[@class='year']")
print(n1.text)
n1 = driver.find_element_by_xpath("//section/p[@class='price']")
print(n1.text)

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()
url = "d:\Web_Crawler\ch7\h7_2.html"
driver.get(url)  # 網頁下載至瀏覽器

pict = driver.find_element_by_xpath("//section/img")
print(pict.get_attribute("src"))

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()
url = "d:\Web_Crawler\ch7\h7_3.html"
driver.get(url)  # 網頁下載至瀏覽器

n1 = driver.find_element_by_xpath("//h1/em")
print("em          : ", n1.text)
n2 = driver.find_element_by_xpath("//h1")
print("h1          : ", n2.text)
n3 = driver.find_element_by_xpath("//h1")
print("textContent : ", n3.get_attribute("textContent"))
n4 = driver.find_element_by_xpath("//h1")
print("innerHTML : ", n4.get_attribute("innerHTML"))
n5 = driver.find_element_by_xpath("//h1")
print("outerHTML : ", n5.get_attribute("outerHTML"))

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome()
url = "d:\Web_Crawler\ch7\h7_4.html"
driver.get(url)  # 網頁下載至瀏覽器

n = driver.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute("outerHTML"))
print(n.get_attribute("href"))

print("------------------------------------------------------------")  # 60個

headless = webdriver.ChromeOptions()
headless.add_argument("headless")  # 隱藏參數
driver = webdriver.Chrome(options=headless)
url = "d:\Web_Crawler\ch7\h7_4.html"
driver.implicitly_wait(5)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器

n = driver.find_element_by_xpath("//div[@id='Traveling']//a[contains(text(),'深石')]")
print(n.get_attribute("outerHTML"))
print(n.get_attribute("href"))

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://www.deepmind.com.tw"
driver.get(url)  # 網頁下載至瀏覽器

eleLink = driver.find_element_by_link_text("深智數位緣起")
print(type(eleLink))  # 列印eleLink資料類別
time.sleep(5)  # 暫停5秒
eleLink.click()

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://www.mcut.edu.tw/?Lang=en"
driver.get(url)  # 網頁下載至瀏覽器

txtBox = driver.find_element_by_id("hdSchKey")
txtBox.send_keys("王永慶")  # 輸入表單資料
time.sleep(5)  # 暫停5秒
txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()
url = "http://www.mcut.edu.tw/?Lang=en"
driver.get(url)  # 網頁下載至瀏覽器

txtBox = driver.find_element_by_name("SchKey")
txtBox.send_keys("王永慶")  # 輸入表單資料
time.sleep(5)  # 暫停5秒
txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個

url = "http://www.mcut.edu.tw"

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

ele = driver.find_element_by_tag_name("body")
time.sleep(3)
ele.send_keys(Keys.PAGE_DOWN)  # 網頁捲動到下一頁
time.sleep(3)
ele.send_keys(Keys.END)  # 網頁捲動到最底端
time.sleep(3)
ele.send_keys(Keys.PAGE_UP)  # 網頁捲動到上一頁
time.sleep(3)
ele.send_keys(Keys.HOME)  # 網頁捲動到最上端

print("------------------------------------------------------------")  # 60個

url = "http://www.deepmind.com.tw"

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

time.sleep(3)
driver.refresh()  # 更新網頁
time.sleep(3)
driver.quit()  # 關閉網頁

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

driver.find_element_by_id("gb_70").click()

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

driver.find_element_by_id("gb_70").click()  # 按登入鈕
driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

driver.find_element_by_id("gb_70").click()  # 按登入鈕
driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)

# 按繼續鈕
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

driver.find_element_by_id("gb_70").click()  # 按登入鈕
driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)

# 按繼續鈕
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

# 輸入密碼
driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
time.sleep(3)

print("------------------------------------------------------------")  # 60個

url = "https://www.google.com"
email = input("請輸入你的Google Email的帳號 : ")
pwd = input("請輸入你的Google Email的密碼 : ")

driver = webdriver.Firefox()
driver.get(url)  # 網頁下載至瀏覽器

driver.find_element_by_id("gb_70").click()  # 按登入鈕
driver.find_element_by_id("identifierId").send_keys(email)  # 輸入帳號
time.sleep(3)

# 按繼續鈕
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

# 輸入密碼
driver.find_element_by_xpath("//input[@type='password']").send_keys(pwd)
time.sleep(3)

# 按繼續鈕
driver.find_element_by_xpath("//span[@class='RveJvd snByac']").click()
time.sleep(3)

print("------------------------------------------------------------")  # 60個

url = "https://opendata.epa.gov.tw/data/contents/aqi/"

driver = webdriver.Chrome()
driver.get(url)  # 網頁下載至瀏覽器

driver.find_element_by_link_text("JSON").click()  # 按JSON鈕
time.sleep(3)

driver.find_element_by_link_text("XML").click()  # 按XML鈕
time.sleep(3)

driver.find_element_by_link_text("CSV").click()  # 按CSV鈕
time.sleep(3)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print(driver.title)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome("./chromedriver", options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&jobcatExpansionType=1&order=12&asc=0&page=6&mode=s&jobsource=2018indexpoc"
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
print(driver.title)
print(len(driver.page_source))
for x in range(5):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)
    print(x + 1, len(driver.page_source))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
cookies = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookies)

print("------------------------------")  # 30個

print(driver.title)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
cookies = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookies)

print("------------------------------")  # 30個

print(driver.title)
driver.quit()

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
)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")

tag_ol = soup.find("ol", {"id": "list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")

tag_ol = soup.find("ol", {"id": "list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, "/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, "//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")

tag_ol = driver.find_element(By.XPATH, "/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, "//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Edge("./msedgedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")

tag_ol = driver.find_element_by_xpath("/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
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
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://www.momoshop.com.tw/search/"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(url + "searchShop.jsp?keyword=NBA")

print("------------------------------")  # 30個

print(driver.title)
html = driver.page_source
fp = open("tmp_NBA.html", "w", encoding="utf8")
fp.write(html)
print("寫入檔案tmp_NBA.html...")
fp.close()
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://fchart.github.io/Ashion/"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
driver.quit()
with open("tmp_products.json", "w", encoding="utf-8") as fp:  # 寫入JSON檔案
    json.dump(products, fp, indent=2, sort_keys=True, ensure_ascii=False)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

url = "https://fchart.github.io/ML/nba_items.html"

# 使用ChromeDriverManager自動下載chromedriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
            time.sleep(5)
            page_num = page_num + 1
        else:
            pages_remaining = False
    except Exception:
        pages_remaining = False
driver.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_id("loginbutton").click()  # 按登入鈕
driver.find_element_by_name("login").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"

# 取消 Alert
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 建立瀏覽器物件
driver = webdriver.Chrome(chrome_options=chrome_options)
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)

# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_name("login").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
print(driver.title)

soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id": "list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath("/html/body/ol")
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath("//li")
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute("innerHTML"))

soup = BeautifulSoup(tag_ol.get_attribute("innerHTML"), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

email_address = "<電子郵件地址>"
password = "<密碼>"

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
url = "https://www.facebook.com/"
driver.get(url)

email = driver.find_element_by_css_selector("#email")
email.send_keys(email_address)

time.sleep(0.5)

passwd = driver.find_element_by_css_selector("#pass")
passwd.send_keys(password)

time.sleep(0.5)

button = driver.find_element_by_css_selector("#loginbutton")
button.click()

time.sleep(5)

soup = BeautifulSoup(driver.page_source, "lxml")
tag_title = soup.find("title")
print(tag_title.text)
driver.quit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間
# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
# 輸入出發站
driver.find_element_by_id("StartStation").send_keys(ss)
# 輸入到達站
driver.find_element_by_id("EndStation").send_keys(es)
# 輸入日期
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id("DepartueSearchDate").send_keys(dd)
# 輸入時間
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id("DepartueSearchTime").send_keys(dt)
driver.find_element_by_id("SearchButton").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站

# 建立瀏覽器物件開啟網站
driver = webdriver.Chrome()
driver.get(url)
# 按我同意
driver.find_element_by_xpath("//button[@class='swal2-confirm swal2-styled']").click()
# 輸入出發站
driver.find_element_by_id("select_location01").send_keys(ss)
# #輸入到達站
driver.find_element_by_id("select_location02").send_keys(es)
# 輸入日期
driver.find_element_by_id("Departdate03").click()
driver.find_element_by_xpath(
    "//div[@id='tot-1']/div/div/ul/li/div/div/table/tbody/tr[2]/td[1]"
).click()
# #輸入時間
driver.find_element_by_id("outWardTime").click()
driver.find_element_by_xpath(
    "//div[@id='tot-1']/div[2]/div/ul/li[2]/div/div/table/tr[3]/td[3]/a/i"
).click()
driver.find_element_by_id("start-search").click()  # 按查詢鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高鐵時刻表查詢網站
url = "http://www.thsrc.com.tw/tw/TimeTable/SearchResult"
ss = "台中站"  # 出發站
es = "台北站"  # 到達站
dd = "2020/03/26"  # 日期
dt = "09:00"  # 時間
# 建立瀏覽器物件
driver = webdriver.Chrome()
## 最大化視窗後開啟facebook網站
# driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("StartStation").send_keys(ss)  # 輸入郵件
driver.find_element_by_id("EndStation").send_keys(es)  # 輸入密碼密碼
driver.find_element_by_id("DepartueSearchDate").click()
driver.find_element_by_id("DepartueSearchDate").send_keys(dd)  # 輸入
driver.find_element_by_id("DepartueSearchTime").click()
driver.find_element_by_id("DepartueSearchTime").send_keys(dt)  # 輸入密碼
driver.find_element_by_id("SearchButton").click()  # 按登入鈕

#
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

# url = 'http://www.thsrc.com.tw/tw/TimeTable/Search'
#
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)                         Chrome/73.0.3683.86 Safari/537.36'
# }
#
# form_data = {
#    'StartStationName':'南港站',
#    'EndStationName':'台南站',
#    'SearchType':'S',
#    'StartStation':'2f940836-cedc-41ef-8e28-c2336ac8fe68',
#    'EndStation':'9c5ac6ca-ec89-48f8-aab0-41b738cb1814',
#    'DepartueSearchDate':'2019/04/02',
#    'DepartueSearchTime':'09:00',
#    'DepartueTrainCode':'',
#    'DestinationSearchDate':'',
#    'DestinationSearchTime':'',
#    'DiscountType':''
# }
#
# response = requests.post(url, headers=headers, data=form_data)
#
# jsdata = response.json()
#
##print(jsdata['data'])
# jsdata

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# loginFacebook.py

# 設定facebook登入資訊
url = "https://www.facebook.com/"
email = "你的faceook電子郵件"
password = "你的faceook密碼"
# 建立瀏覽器物件
driver = webdriver.Chrome()
# 最大化視窗後開啟facebook網站
driver.maximize_window()
driver.get(url)
# 執行自動登入動作
driver.find_element_by_id("email").send_keys(email)  # 輸入郵件
driver.find_element_by_id("pass").send_keys(password)  # 輸入密碼
driver.find_element_by_id("loginbutton").click()  # 按登入鈕

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# PyAutoGUI，自動控制滑鼠與鍵盤
import pyautogui as auto

"""
url = 'https://www.google.com/'

driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒

txt = driver.find_element(By.NAME, 'q')             # 取得屬性 name 為 xxxx 的網頁元素 ( TextArea )

txt.send_keys('this is a lion-mouse')
time.sleep(1)  # 等1秒

print(txt.tag_name)
print(txt.get_attribute("type"))
print(txt.get_attribute("id"))


txt.submit()    #就是按了enter
"""

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

print("------------------------------------------------------------")  # 60個
print("完成")

"""
print('準備關閉瀏覽器')
for i in range(0, 10):
    print(i, '秒')	# 0~9
    time.sleep(1)  # 等1秒

#print('關閉瀏覽器')
#driver.close()  #關閉瀏覽器

print('關閉瀏覽器並且退出驅動程序')
driver.quit()   #關閉瀏覽器並且退出驅動程序
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "http://aaa.24ht.com.tw"

driver = webdriver.Chrome()  # 使用Chrome
driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 打開瀏覽器，開啟網頁

print(f"網頁標題內容是 = {driver.title}")

tag1 = driver.find_element_by_id("author")  # 傳回<h1>
print(f"\n標籤名稱 = {tag1.tag_name}, 內容是 = {tag1.text}")

print()
tag2 = driver.find_elements_by_id("content")  # 傳回<h1>
for i in range(len(tag2)):
    print(f"標籤名稱 = {tag2[i].tag_name}, 內容是 = {tag2[i].text}")

print()
tag3 = driver.find_elements_by_tag_name("p")  # 傳回<p>
for i in range(len(tag3)):
    print(f"標籤名稱 = {tag3[i].tag_name}, 內容是 = {tag3[i].text}")

print()
tag4 = driver.find_elements_by_tag_name("img")  # 傳回<img>
for i in range(len(tag4)):
    print(f"標籤名稱 = {tag4[i].tag_name}, 內容是 = {tag4[i].get_attribute('src')}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()  # 使用Firefox

url = "https://deepwisdom.com.tw"
driver.get(url)  # 打開瀏覽器，開啟網頁

eleLink = driver.find_element_by_link_text("深智數位緣起")
print(type(eleLink))  # 列印eleLink資料類別
time.sleep(1)  # 等1秒
eleLink.click()

print("------------------------------------------------------------")  # 60個

driver = webdriver.Firefox()  # 使用Firefox

url = "http://www.google.com"
driver.get(url)  # 打開瀏覽器，開啟網頁

txtBox = driver.find_element_by_name("q")
txtBox.send_keys("明志科技大學")  # 輸入表單資料
time.sleep(1)  # 等1秒
txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個

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

url = "https://deepwisdom.com.tw"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒
driver.refresh()  # 更新網頁
time.sleep(1)  # 等1秒
driver.quit()  # 關閉網頁

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

url = "https://hophd.wordpress.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.implicitly_wait(60)
driver.get(url)  # 打開瀏覽器，開啟網頁
driver.set_window_position(0, 0)
time.sleep(1)  # 等1秒
driver.quit()
sssss
print("------------------------------------------------------------")  # 60個

""" NG
# 假的 headers 資訊
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15"
opt = webdriver.ChromeOptions()
# 加入 headers 資訊
opt.add_argument("--user-agent=%s" % user_agent)
driver = webdriver.Chrome(options=opt)  # 使用Chrome

url = "google.com"

#driver = webdriver.Chrome()    #使用Chrome
driver = webdriver.Firefox()   #使用Firefox

driver.get(url)  # 打開瀏覽器，開啟網頁
"""

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

url = "https://www.google.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

# 從載入後的動態網頁裡，找到指定的元素
imgCount = driver.find_element(By.CSS_SELECTOR, "CSS 選擇器")

print("------------------------------------------------------------")  # 60個

from selenium.webdriver.common.action_chains import ActionChains

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
actions = ActionChains(driver)
# 滑鼠先移到 submitBtn 上，然後再點擊 submitBtn
actions.move_to_element(submitBtn).click(submitBtn)
actions.perform()

print("------------------------------------------------------------")  # 60個

submitBtn = driver.find_element(By.CSS_SELECTOR, "#submitBtn")
time.sleep(1)  # 等1秒
submitBtn.click()
time.sleep(1)  # 等1秒
submitBtn.click()

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
driver.close()

print("------------------------------------------------------------")  # 60個

url = "http://www.flag.com.tw"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

time.sleep(1)  # 等1秒
driver.close()  # 關閉網頁(目前分頁)A

print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

print("標題：" + driver.title)  # 輸出網頁標題
print("網址：" + driver.current_url)  # 輸出網頁網址
print("內容：" + driver.page_source[0:50])  # 輸出網頁原始碼的前 50 個字
print("視窗：", driver.get_window_rect())  # 輸出視窗的位置及寬高
driver.save_screenshot("d:/scrcap.png")  # 截取網頁畫面
time.sleep(1)  # 等1秒
driver.set_window_rect(200, 100, 500, 250)  # 改變視窗位置及大小
time.sleep(1)  # 等1秒
driver.fullscreen_window()  # 將視窗設為全螢幕
time.sleep(1)  # 等1秒
driver.quit()  # 關閉視窗結束驅動

print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

e1 = driver.find_element_by_tag_name("head")  # 尋找 head 標籤
print(e1.tag_name)  # 輸出 head 確認已找到 (tag_name 屬性為標籤名稱, 詳見下表)
e2 = e1.find_element_by_tag_name("title")  # 在 head 元素中尋找 title 標籤
print(e2.tag_name)  # 輸出 tite 確認已找到
driver.quit()  # 關閉視窗結束驅動

print("------------------------------------------------------------")  # 60個

url = "http://www.facebook.com"

opt = webdriver.ChromeOptions()  # ←建立選項物件
opt.add_experimental_option(
    "prefs",  # ←在選項物件中加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
driver = webdriver.Chrome(options=opt)  # ←以 options 指名參數來建立瀏覽器物件
driver.get(url)  # 打開瀏覽器，開啟網頁

driver.find_element_by_id("email").send_keys("您的帳號")  # }
driver.find_element_by_id("pass").send_keys("您的密碼")  # }輸入帳密並按登入鈕
driver.find_element_by_name("login").click()  # }

print("------------------------------------------------------------")  # 60個

url = "http://www.google.com"

opt = webdriver.ChromeOptions()  # 建立選項物件
opt.add_experimental_option(
    "prefs",  # 加入「禁止顯示訊息框」的選項
    {"profile.default_content_setting_values": {"notifications": 2}},
)
driver = webdriver.Chrome(options=opt)  # 以 options 參數來建立瀏覽器物件
driver.get(url)  # 打開瀏覽器，開啟網頁

driver.maximize_window()  # ←將視窗最大化以避免最右邊的登入鈕沒顯示出來

driver.find_element_by_id("gb_70").click()  # ←按登入鈕
time.sleep(1)  # 等1秒
driver.find_element_by_id("identifierId").send_keys("您的帳號")  # }←輸入帳號
driver.find_element_by_id("identifierNext").click()  # ←按繼續鈕
time.sleep(1)  # 等1秒
driver.find_element_by_name("password").send_keys("您的密碼")  # ←輸入帳密
driver.find_element_by_id("passwordNext").click()  # ←按繼續鈕

print("------------------------------------------------------------")  # 60個

url = "https://www.wikipedia.org/"

driver = webdriver.Firefox()  # 使用Firefox
driver.get(url)  # 打開瀏覽器，開啟網頁

txtBox = driver.find_element_by_id("searchInput")
txtBox.send_keys("Artificial Intelligence")  # 輸入表單資料
time.sleep(1)  # 等1秒
txtBox.submit()  # 送出表單

print("------------------------------------------------------------")  # 60個

url = "http://oxxo.studio"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

print(driver.title)
time.sleep(1)  # 等1秒
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 捲動到最下方
time.sleep(1)  # 等1秒
for i in range(1, 7):
    img = driver.find_element_by_xpath(
        '//*[@id="content-grid"]/ul/li[' + str(i) + "]/a[1]/div/img"
    )
    response = requests.get(img.get_attribute("src"))
    with open("demo/test" + str(i) + ".jpg", "wb") as f:
        f.write(response.content)  # 將response.content二進位內容寫入檔案
driver.close()

print("------------------------------------------------------------")  # 60個

url = "https://www.dinbendon.net/do/login"

options = webdriver.ChromeOptions()
options.add_argument("headless")  # 不會開啟瀏覽器
driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

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

time.sleep(1)  # 等1秒

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
print("------------------------------------------------------------")  # 60個

url = "https://www.google.com.tw/imghp?hl=zh-TW&tab=wi&ogbl"

driver = webdriver.Chrome()  # 使用Chrome
driver.get(url)  # 打開瀏覽器，開啟網頁

search = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
search.send_keys("林志玲")

btn = driver.find_element_by_xpath('//*[@id="sbtc"]/button')
btn.click()

for i in range(1, 6):
    time.sleep(0.5)  # 等0.5秒
    div = driver.find_element_by_xpath(
        "/html/body/div[6]/div[3]/div[3]/div[2]/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div["
        + str(i)
        + "]"
    )
    div.click()

    time.sleep(0.5)  # 等0.5秒
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

# 網址處理
url_yahoo = "https://tw.bid.yahoo.com/search/auction/product?"
url_product = "kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime"
url = url_yahoo + url_product

driver = webdriver.Chrome()
driver.implicitly_wait(5)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器
# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
product_links = driver.find_elements_by_xpath(linkPath)
product_link = product_links[0].get_attribute("href")
print("商品連結 : ", product_link)
# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = driver.find_elements_by_xpath(titlePath)
product_title = product_titles[0].get_attribute("textContent")
print("商品名稱 : ", product_title)
# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = driver.find_elements_by_xpath(pricePath)
product_price = product_prices[0].text
print("商品價格 : ", product_price)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 網址處理
url_yahoo = "https://tw.bid.yahoo.com/search/auction/product?"
url_product = "kw=薩爾達傳說&p=薩爾達傳說&sort=-ptime"
url = url_yahoo + url_product

driver = webdriver.Chrome()

driver.implicitly_wait(5)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器
# 商品連結
linkPath = "//ul[@class='gridList']/li/a"
product_links = driver.find_elements_by_xpath(linkPath)

# 商品名稱
titlePath = "//span[contains(@class,'BaseGridItem__title___2HWui')]"
product_titles = driver.find_elements_by_xpath(titlePath)

# 商品價格
pricePath = "//span[contains(@class,'BaseGridItem__price___31jkj')]/em"
product_prices = driver.find_elements_by_xpath(pricePath)

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
driver = webdriver.Chrome()

driver.implicitly_wait(10)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器
time.sleep(3)
searchNode = driver.find_elements_by_xpath("//input[contains(@id,'q-destination')]")
checkInNode = driver.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-in')]"
)
checkOutNode = driver.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-out')]"
)

# 輸入搜尋關鍵資料
searchNode[0].clear()  # 清除城市欄位
searchNode[0].send_keys(city)  # 輸入搜尋城市
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳到check in欄位
checkInNode[0].clear()  # 清除check in欄位
checkInNode[0].send_keys(checkin_time)  # 輸入check in時間
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳至check out欄位
checkOutNode[0].clear()  # 清除check out欄位
checkOutNode[0].send_keys(checkout_time)  # 輸入check out時間
time.sleep(3)
checkOutNode[0].send_keys(Keys.ENTER)  # 表單按Enter表示輸入完成
time.sleep(3)

# 旅館名稱
hotelPath = "//ol[@class='listings infinite-scroll-enabled']//h3/a"
names = driver.find_elements_by_xpath(hotelPath)
name = names[0].text
print("旅館名稱 : ", name)

# 旅館地址
addressPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='address']"
addresses = driver.find_elements_by_xpath(addressPath)
address = addresses[0].text
print("旅館地址 : ", address)

# 旅館星級評價
starPath = (
    "//ol[@class='listings infinite-scroll-enabled']//span[@class='star-rating-text']"
)
stars = driver.find_elements_by_xpath(starPath)
star = stars[0].text
print("旅館星級 : ", star)

# 旅館定價
listingpricePath = (
    "//ol[@class='listings infinite-scroll-enabled']//del[@data-reason='DRR-448']"
)
lprices = driver.find_elements_by_xpath(listingpricePath)
lprice = lprices[0].text  # 定價listing price
print("旅館定價 : ", lprice)

# 旅館售價
pricePath = "//ol[@class='listings infinite-scroll-enabled']//ins[@class='special-deal-animation']"
prices = driver.find_elements_by_xpath(pricePath)
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

driver = webdriver.Chrome()

driver.implicitly_wait(10)  # 等待網頁載入
driver.get(url)  # 網頁下載至瀏覽器
time.sleep(3)
searchNode = driver.find_elements_by_xpath("//input[contains(@id,'q-destination')]")
checkInNode = driver.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-in')]"
)
checkOutNode = driver.find_elements_by_xpath(
    "//input[contains(@id,'q-localised-check-out')]"
)

# 輸入搜尋關鍵資料
searchNode[0].clear()  # 清除城市欄位
searchNode[0].send_keys(city)  # 輸入搜尋城市
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳到check in欄位
checkInNode[0].clear()  # 清除check in欄位
checkInNode[0].send_keys(checkin_time)  # 輸入check in時間
time.sleep(3)
searchNode[0].send_keys(Keys.TAB)  # 按Tab跳至check out欄位
checkOutNode[0].clear()  # 清除check out欄位
checkOutNode[0].send_keys(checkout_time)  # 輸入check out時間
time.sleep(3)
checkOutNode[0].send_keys(Keys.ENTER)  # 表單按Enter表示輸入完成
time.sleep(3)

# 旅館名稱
hotelPath = "//ol[@class='listings infinite-scroll-enabled']//h3/a"
names = driver.find_elements_by_xpath(hotelPath)
# 旅館地址
addressPath = "//ol[@class='listings infinite-scroll-enabled']//span[@class='address']"
addresses = driver.find_elements_by_xpath(addressPath)
# 旅館星級評價
starPath = (
    "//ol[@class='listings infinite-scroll-enabled']//span[@class='star-rating-text']"
)
stars = driver.find_elements_by_xpath(starPath)
# 旅館定價
listingpricePath = (
    "//ol[@class='listings infinite-scroll-enabled']//del[@data-reason='DRR-448']"
)
lprices = driver.find_elements_by_xpath(listingpricePath)
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
    time.sleep(1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
