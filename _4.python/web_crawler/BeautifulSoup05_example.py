# class_ 的"_"符號是因為class是保留字，所以加上_符號作區別

import requests
from bs4 import BeautifulSoup
import urllib.parse
import html5lib


# 無參數
def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


# Yahoo字典 ST
def searchdic(search_word):
    result = ""

    # yahoo字典的網址，可修改網址查詢想要的單字，網址當中的%s為格式化字串
    url = "https://tw.dictionary.search.yahoo.com/search?p=%s" % (search_word)
    html_data = get_html_data1(url)
    """ same
    payload = {'p': search_word}
    html_data = requests.get('https://tw.dictionary.search.yahoo.com/search?', params = payload)
    #相當於寫了 : https://tw.dictionary.search.yahoo.com/search?p=search_word
    """

    if html_data:
        result += "擷取網頁資料 OK\n"
        # print(html_data.text)
    else:
        print("無法取得網頁資料")
        return None

    soup = BeautifulSoup(html_data.text, "html.parser")
    # soup = BeautifulSoup(html_data.text, 'html5lib')   #也可
    # soup = BeautifulSoup(html_data.text, 'lxml')   # 指定 lxml 作為解析器
    print(soup.prettify()) # 把排版後的 html 印出來


    sorry_word = soup.find_all("div", class_="w-100p fz-16 va-mid ta-c")
    for sw in sorry_word:
        #print(type(sorry_word))
        #print(len(sorry_word))
        for di in sw:
            #print(di.text)
            #result += di.text.replace("\n", "") + "\n"
            if "很抱歉" in di.text:
                return None

    """
    # 一些屬性或方法, BeautifulSoup的用法
    print('---title---')
    print(soup.title) # 把 tag 抓出來
    print('---title.name---')
    print(soup.title.name) # 把 title 的 tag 名稱抓出來
    print('---title.string---')
    print(soup.title.string) # 把 title tag 的內容抓出來
    print('---title.parent.name---')
    print(soup.title.parent.name) # title tag 的上一層 tag
    print('---a---')
    print(soup.a) # 把第一個 <a></a> 抓出來
    print('---all a---')
    print(soup.find_all('a')) # 把所有的 <a></a> 抓出來
    print('---all div---')
    print(soup.find_all('div')) # 把所有的 <a></a> 抓出來
    """

    result += "上框\n"
    result += "上框 搜尋英文字 :\n"
    search_word = soup.find_all("span", class_="fz-24 fw-500 c-black lh-24")
    for sw in search_word:
        for di in sw:
            result += di.text.replace("\n", "") + "\n"

    result += "上框 音標 :\n"

    # 音標
    pronunciation = soup.find_all("span", class_="fz-14")
    result += "000" + pronunciation[0].text + "\n"  # 第0個是KK音標
    result += "111" + pronunciation[1].text + "\n"  # 第1個是DJ音標

    result += "上框 詞性 :\n"
    divs = soup.find_all("div", "compList mb-25 p-rel")  # 如此可以框選較大範圍之資料 找到較大的區塊包含所有資料

    # print(divs)
    for div in divs:
        # print(div)
        for di in div:
            for tt in di.find_all("li"):
                cc = tt.find("div", "pos_button fz-14 fl-l mr-12")
                if cc != None:  # 如果標題包含資料, 印出來
                    result += "詞性\n"
                    result += cc.text.replace("\n", "") + "\n"  # 只是刪除換行符號, 或許不一定有

                dd = tt.find("div", "fz-16 fl-l dictionaryExplanation")
                if dd != None:  # 如果標題包含資料, 印出來
                    result += "解釋\n"
                    result += dd.text.replace("\n", "") + "\n"  # 只是刪除換行符號, 或許不一定有

    result += "中框\n"
    result += "中框 釋義 :\n"

    divs = soup.find_all(
        "div",
        class_="grp grp-tab-content-explanation tabsContent-s tab-content-explanation pt-24 tabActived",
    )  # 如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
    # print(divs)

    if divs == []:
        return result

    div1 = divs[0].find_all("div", "compTitle lh-25")
    length = len(div1)
    # print('a共找到', length, '筆資料')

    div2 = divs[0].find_all("div", "compTextList ml-50")
    length = len(div2)
    # print('b共找到', length, '筆資料')

    # 依照詞性數量的區塊做迴圈，將一個一個區塊作處理
    for nn in range(length):
        """debug
        print(nn)
        print('--------------------')
        print(div1[nn])   # 使用索引值, 只印出text部分
        print('--------------------')
        print(div2[nn])   # 使用索引值, 只印出text部分
        print('--------------------')
        """
        result += "詞性\n"
        result += (
            div1[nn].find("span", "pos_button fz-14").text.replace("\n", "")
        )  # 只是刪除換行符號, 或許不一定有
        result += (
            div1[nn].find("span", "fz-14 va-mid lh-22 ml-5").text.replace("\n", "")
            + "\n"
        )  # 只是刪除換行符號, 或許不一定有

        result += "解釋:\n"
        nnn2 = div2[nn].find_all("span")
        # print(nnn)
        # 這個迴圈將詞性區塊裡的單字意思一個一個抓出來顯示
        # 而每個單字意思及例句都是使用li標籤所包起來，所以將每個li標籤抓出來顯示他的單字意思及例句
        for n in nnn2:
            # print(n)
            for di in n:
                result += di.text.replace("\n", "")
            result += "\n"
    return result


# Yahoo字典 SP

"""test
print('------------------------------')
print('Yahoo字典')
search_word = 'coordinate'
#search_word = '英國'
result = searchdic(search_word)
print(result)
print('------------------------------')
print('Yahoo字典')
search_word = 'oat'
result = searchdic(search_word)
print(result)
print('------------------------------')
search_word = '英國'
result = searchdic(search_word)
print(result)
print('------------------------------')
"""

while True:
    print()
    search_word = input("請輸入查詢單字 : ")
    if search_word == "":
        continue
    if search_word == "q":
        break
    
    result = searchdic(search_word)
    if result == None:
        print('找不到 :', search_word)
    else:
        print(result)

print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup08_books1.py

# 有參數 之 requests.get

import requests
from bs4 import BeautifulSoup

print("------------------------------------------------------------")  # 60個

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/77.0.3865.120 Safari/537.36"
}

url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_020"  # old
url = "https://www.books.com.tw/web/sys_saletopb/books/19/?loc=P_0002_021"

html_data = requests.get(url, headers=headers)

soup = BeautifulSoup(html_data.text, "html.parser")
# print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

sel = "li.item"
ranking = soup.select(sel)

# print(ranking)

print()
print()
print()

cnt = 0
for rank, book in enumerate(ranking, 1):
    print(book)
    """
    title = book.h4.a.text
    detail = book.find_all("li")
    author = detail[0].text
    price = detail[1].text
    print(rank, title, author, price)

    print("第{}名".format(rank))
    print(book.h4.a.text)
    detail = book.find_all('a')
    print(detail[0].text)
    print(detail[1].text)
    """
    print("----")
    cnt += 1
    if cnt == 10:
        break

print("Done")


print("------------------------------------------------------------")  # 60個


def showbook(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        pages = int(soup.select(".cnt_page span")[0].text)  # 該分類共有多少頁
        print("共有", pages, "頁")
        for page in range(1, pages + 1):
            pageurl = url + "&page=" + str(page).strip()
            print("第", page, "頁", pageurl)
            showpage(pageurl, kind)
    except:  # 沒有分頁的處理
        showpage(url, kind)


def showpage(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    # 近期新書、在 class="mod type02_m012 clearfix" 中
    res = soup.find_all("div", {"class": "mod type02_m012 clearfix"})[0]
    items = res.select(".item")  # 所有 item
    n = 0  # 計算該分頁共有多少本書
    for item in items:
        msg = item.select(".msg")[0]
        src = item.select("a img")[0]["src"]
        title = msg.select("a")[0].text  # 書名
        imgurl = src.split("?i=")[-1].split("&")[0]  # 圖片網址
        author = msg.select("a")[1].text  # 作者
        publish = msg.select("a")[2].text  # 出版社
        date = msg.find("span").text.split("：")[-1]  # 出版日期
        onsale = item.select(".price .set2")[0].text  # 優惠價
        content = item.select(".txt_cont")[0].text.replace(" ", "").strip()  # 內容
        print("\n分類：" + kind)
        print("書名：" + title)
        print("圖片網址：" + imgurl)
        print("作者：" + author)
        print("出版社：" + publish)
        print("出版日期：" + date)
        print(onsale)  # 優惠價
        print("內容：" + content)
        n += 1
        print("n=", n)


#
#        if n==2: break  # 開發階段


def twobyte(kindno):
    if kindno < 10:
        kindnostr = "0" + str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr


# 主程式
import requests
from bs4 import BeautifulSoup

kindno = 1  # 計算共有多少分類
homeurl = "http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1"
mode = "?o=5&v=1"  # 顯示模式：直式  排序依：暢銷度
url = "http://www.books.com.tw/web/books_nbtopm_"
html = requests.get(homeurl).text
soup = BeautifulSoup(html, "html.parser")
# 中文書新書分類，算出共有多少分類
res = soup.find("div", {"class": "mod_b type02_l001-1 clearfix"})
hrefs = res.select("a")
for href in hrefs:
    kindurl = url + twobyte(kindno) + mode  # 分類網址
    print("\nkindno=", kindno)
    kind = href.text  # 分類
    showbook(kindurl, kind)  # 顯示該分類所有書籍
    kindno += 1
#    if kindno==2: break  # 開發階段


print("------------------------------------------------------------")  # 60個


def showbook(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    try:
        pages = int(soup.select(".cnt_page span")[0].text)  # 該分類共有多少頁
        print("共有", pages, "頁")
        for page in range(1, pages + 1):
            pageurl = url + "&page = " + str(page).strip()
            print("第", page, "頁", pageurl)
            showpage(pageurl, kind)
    except:  # 沒有分頁的處理
        showpage(url, kind)


def showpage(url, kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    # 近期新書、在 class = "mod type02_m012 clearfix" 中
    res = soup.find_all("div", {"class": "mod type02_m012 clearfix"})[0]
    items = res.select(".item")  # 所有 item
    n = 0  # 計算該分頁共有多少本書
    for item in items:
        msg = item.select(".msg")[0]
        src = item.select("a img")[0]["src"]
        title = msg.select("a")[0].text  # 書名
        imgurl = src.split("?i = ")[-1].split("&")[0]  # 圖片網址
        author = msg.select("a")[1].text  # 作者
        publish = msg.select("a")[2].text  # 出版社
        date = msg.find("span").text.split("：")[-1]  # 出版日期
        onsale = item.select(".price .set2")[0].text  # 優惠價
        content = item.select(".txt_cont")[0].text.replace(" ", "").strip()  # 內容
        # 將資料加入 list1 串列中
        listdata = [kind, title, imgurl, author, publish, date, onsale, content]
        list1.append(listdata)
        n += 1
        print("n = ", n)


def twobyte(kindno):
    if kindno < 10:
        kindnostr = "0" + str(kindno)
    else:
        kindnostr = str(kindno)
    return kindnostr


# 主程式
import requests
from bs4 import BeautifulSoup

list1 = []
kindno = 1  # 計算共有多少分類
homeurl = "http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1"
mode = "?o=5&v=1"  # 顯示模式：直式  排序依：暢銷度
url = "http://www.books.com.tw/web/books_nbtopm_"
html = requests.get(homeurl).text
soup = BeautifulSoup(html, "html.parser")
# 中文書新書分類，算出共有多少分類
res = soup.find("div", {"class": "mod_b type02_l001-1 clearfix"})
hrefs = res.select("a")
for href in hrefs:
    kindurl = url + twobyte(kindno) + mode  # 分類網址
    print("\nkindno = ", kindno)
    kind = href.text  # 分類
    showbook(kindurl, kind)  # 顯示該分類所有書籍
    kindno += 1

# excel 資料
listtitle = ["分類", "書名", "圖片網址", "作者", "出版社", "出版日期", "優惠價", "內容"]
print(listtitle)  # 標題

for _ in list1:  # 資料
    print(_)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup09_population.py

import requests
from bs4 import BeautifulSoup

url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

# 人口統計
person_data = list()  # 人口統計資料
data1 = soup.find("tbody")
# print(data1)

rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if len(cols) > 0:
        if cols[1].text != "─":
            person_data.append(
                (
                    (int)(cols[0].text.strip()[:-1]),
                    (int)(cols[1].text),
                    (int)(cols[2].text),
                    (int)(cols[3].text),
                )
            )
        else:
            print("xxxxxx1111")
    else:
        print("xxxxxx2222")

person_data.reverse()  # 反相
length = len(person_data)
year1 = []
person1 = []
person2 = []
person3 = []
for i in range(0, length):
    year1.append(person_data[i][0])
    person1.append(person_data[i][1])
    person2.append(person_data[i][2])
    person3.append(person_data[i][3])

# 戶數統計
house_data = list()  # 戶數統計資料
data1 = soup.select("table[summary^='歷年戶數統計列表排版用']")[0]
# print(data1)

rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if len(cols) > 0:
        if cols[1].text != "─":
            house_data.append(((int)(cols[0].text.strip()[:-1]), (int)(cols[1].text)))
        else:
            print("xxxxxx1111")
    else:
        print("xxxxxx2222")

house_data.reverse()  # 反相
length = len(house_data)
year2 = []
house = []
for i in range(0, length):
    year2.append(house_data[i][0])
    house.append(house_data[i][1])

"""
print('person_data')
print(person_data)
print('house_data')
print(house_data)
print('year1')
print(year1)
print('person1')
print(person1)
print('person2')
print(person2)
print('person3')
print(person3)
print('year2')
print(year2)
print('house')
print(house)
"""

print("------------------------------------------------------------")  # 60個

# 開始畫圖

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(
    num="plot 集合 1 函數曲線",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

# 第一張圖
plt.subplot(211)

plt.plot(year1, person1, linewidth=2.0, label="男")
plt.plot(year1, person2, linewidth=2.0, label="女")
plt.title("桃園市大溪區歷年人口數")
plt.xlabel("年度")
plt.ylabel("人口數")
plt.legend()

# 第二張圖
plt.subplot(212)

plt.plot(year2, house, linewidth=2.0)
plt.title("桃園市大溪區歷年戶數")
plt.xlabel("年度")
plt.ylabel("戶數")

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


"""
url = 'https://siluo.household.yunlin.gov.tw/popul05/List.aspx?Parser=99,5,47,,,,,,,,,,,,,,,,,,,,,4'
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

#print(soup)

links = soup.find_all("li", class_="list_date")    # 文章標題
for link in links:
    print(link.text.strip()) # strip()用來刪除文字前面和後面多餘的空白
    dddd = link.find_all("span", role="gridcell")    # 文章標題
    for ddd in dddd:
        print(ddd.text.strip())
    print()


"""

"""

#人口統計
person_data = list()    #人口統計資料
data1 = soup.find("tbody")
#print(data1)


<li class="list_date">


rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if(len(cols) > 0):
        if cols[1].text != "─":
            person_data.append(((int)(cols[0].text.strip()[:-1]), (int)(cols[1].text), (int)(cols[2].text), (int)(cols[3].text)))
        else:
            print('xxxxxx1111')
    else:
        print('xxxxxx2222')

person_data.reverse()   #反相
length = len(person_data)
year1 = []
person1 = []
person2 = []
person3 = []
for i in range(0, length): 
    year1.append(person_data[i][0])
    person1.append(person_data[i][1])
    person2.append(person_data[i][2])
    person3.append(person_data[i][3])
"""


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup10_gossiping1.py

import requests
from bs4 import BeautifulSoup

print("------------------------------------------------------------")  # 60個

print("有無 cookies 之比較")

# gossiping
url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # 八卦板的網址

print("無 cookies")
html_data = requests.get(url)
# print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print("有 cookies")
cookies = {"over18": "1"}
html_data = requests.get(url, cookies=cookies)
# print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print("BeautifulSoup 測試 1a 使用 cookie")

url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # 八卦板的網址

my_headers = {"cookie": "over18=1"}  # cookie設定

response = requests.get(url, headers=my_headers)  # 放在headers欄位中傳送
soup = BeautifulSoup(response.text, "html.parser")  # 解析原始碼
# print(soup.prettify())
links = soup.find_all("div", class_="title")  # 文章標題
# print(links)
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print("BeautifulSoup 測試 1b 使用 session")

# post要傳的資料
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}

rs = requests.session()  # 用session紀錄此次使用的cookie
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)  # post傳遞資料
response = rs.get(url)  # 再get一次PTT八卦板首頁
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("div", class_="title")  # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print("BeautifulSoup 測試 1c")

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"  # 八卦板的網址

payload = {"from": url, "yes": "yes"}
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
}
rs = requests.Session()
rs.post("https://www.ptt.cc/ask/over18", data=payload, headers=headers)
res = rs.get(url, headers=headers)

soup = BeautifulSoup(res.text, "html.parser")
items = soup.select(".r-ent")
for item in items:
    print(
        item.select(".date")[0].text,
        item.select(".author")[0].text,
        item.select(".title")[0].text,
    )


import requests
from bs4 import BeautifulSoup

# post要傳的資料
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}

# 用session紀錄此次使用的cookie
rs = requests.session()
# post傳遞資料
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
# 再get一次PTT八卦板首頁
response = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(response.status_code)

root = BeautifulSoup(response.text, "html.parser")
links = root.find_all("div", class_="title")  # 文章標題
for link in links:
    page_url = "https://www.ptt.cc" + link.a["href"]
    print(page_url)
    response = rs.get(page_url)
    result = BeautifulSoup(response.text, "html.parser")
    main_content = result.find("div", id="main-content")
    article_info = main_content.find_all("span", class_="article-meta-value")
    if len(article_info) != 0:
        author = article_info[0].string  # 作者
        title = article_info[2].string  # 標題
        time = article_info[3].string  # 時間
    else:  # 避免有沒有資訊的狀況
        author = "無"  # 作者
        title = "無"  # 標題
        time = "無"  # 時間
    # print(author + ' ' + title + ' ' + time)
    # 將整段文字內容抓出來
    all_text = main_content.text
    # 以--切割，抓最後一個--前的所有內容
    pre_texts = all_text.split("--")[:-1]
    # 將前面的所有內容合併成一個
    one_text = "--".join(pre_texts)
    # 以\n切割，第一行標題不要
    texts = one_text.split("\n")[1:]
    # 將每一行合併
    content = "\n".join(texts)
    print(content)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup10_gossiping2.py

# PTT八卦版爬蟲

from bs4 import BeautifulSoup
import requests
import json

# 基本參數
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}
data = []  # 全部文章的資料
num = 0

# 用session紀錄此次使用的cookie
rs = requests.session()
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)

# 爬取兩頁
for i in range(2):
    # get取得頁面的HTML
    # print(url)
    response = rs.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    # 找出每篇文章的連結
    links = soup.find_all("div", class_="title")
    for link in links:
        # 如果文章已被刪除，連結為None
        if link.a != None:
            article_data = {}  # 單篇文章的資料
            page_url = "https://www.ptt.cc/" + link.a["href"]

            # 進入文章頁面
            response = rs.get(page_url)
            result = BeautifulSoup(response.text, "html.parser")
            # print(soup.prettify())

            # 找出作者、標題、時間、留言
            main_content = result.find("div", id="main-content")
            article_info = main_content.find_all("span", class_="article-meta-value")

            if len(article_info) != 0:
                author = article_info[0].string  # 作者
                title = article_info[2].string  # 標題
                time = article_info[3].string  # 時間
            else:
                author = "無"  # 作者
                title = "無"  # 標題
                time = "無"  # 時間

            # print(author)
            # print(title)
            # print(time)

            article_data["author"] = author
            article_data["title"] = title
            article_data["time"] = time

            # 將整段文字內容抓出來
            all_text = main_content.text
            # 以--切割，抓最後一個--前的所有內容
            pre_texts = all_text.split("--")[:-1]
            # 將前面的所有內容合併成一個
            one_text = "--".join(pre_texts)
            # 以\n切割，第一行標題不要
            texts = one_text.split("\n")[1:]
            # 將每一行合併
            content = "\n".join(texts)

            # print(content)
            article_data["content"] = content

            # 一種留言一個列表
            comment_dic = {}
            push_dic = []
            arrow_dic = []
            shu_dic = []

            # 抓出所有留言
            comments = main_content.find_all("div", class_="push")
            for comment in comments:
                push_tag = comment.find("span", class_="push-tag").string  # 分類標籤
                push_userid = comment.find("span", class_="push-userid").string  # 使用者ID
                push_content = comment.find(
                    "span", class_="push-content"
                ).string  # 留言內容
                push_time = comment.find(
                    "span", class_="push-ipdatetime"
                ).string  # 留言時間

                # print(push_tag, push_userid, push_content, push_time)

                dict1 = {
                    "push_userid": push_userid,
                    "push_content": push_content,
                    "push_time": push_time,
                }
                if push_tag == "推 ":
                    push_dic.append(dict1)
                if push_tag == "→ ":
                    arrow_dic.append(dict1)
                if push_tag == "噓 ":
                    shu_dic.append(dict1)

            # print(push_dic)
            # print(arrow_dic)
            # print(shu_dic)
            # print("--------")

            comment_dic["推"] = push_dic
            comment_dic["→"] = arrow_dic
            comment_dic["噓"] = shu_dic
            article_data["comment"] = comment_dic

            # print(article_data)
            data.append(article_data)
            num += 1
            print("第 " + str(num) + " 篇文章完成!")

    # 找到上頁的網址，並更新url
    url = "https://www.ptt.cc/" + soup.find("a", string="‹ 上頁")["href"]

# print(data)
# 輸出JSON檔案
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup10_gossiping3.py

import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

session = requests.Session()
payload = {"from": "/bbs/Gossiping/index.html", "yes": "yes"}
session.post(
    "https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html", payload
)

# html_data = requests.get(url)  #直接抓, 抓不到資料, 因為有擋
html_data = session.get(url)

soup = BeautifulSoup(html_data.text, "html.parser")

titles = soup.select(".title")

for title in titles:
    print(title.a.text)
    print(title.a["href"])

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup10_gossiping4a.py

import requests
from bs4 import BeautifulSoup

url = "http://blog.castman.net/web-crawler-tutorial/ch1/connect.html"

try:
    resp = requests.get(url)
except:
    resp = None

if resp and resp.status_code == 200:
    print(resp.status_code)
    print(resp.text)
    soup = BeautifulSoup(resp.text, "html.parser")
    print(soup)
    try:
        h1 = soup.find("h1")
    except:
        h1 = None
    if h1:
        print(soup.find("h1"))
        print(soup.find("h1").text)
    try:
        h2 = soup.find("h2")
    except:
        h2 = None
    if h2:
        print(soup.find("h2").text)
    else:
        print("h2 tag not found!")


import requests
from bs4 import BeautifulSoup


def get_header_text(url, header_tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            return soup.find(header_tag).text
    except Exception as exception:
        return None


url = "http://blog.castman.net/web-crawler-tutorial/ch1/connect.html"

h1 = get_header_text(url, "h1")
if h1:
    print("h1: " + h1)

h2 = get_header_text(url, "h2")
if h2:
    print("h2: " + h2)

p = get_header_text(url, "p")
if p:
    print("p: " + p)


# PTT八卦版今日熱門文章

import requests
import time
import json
from bs4 import BeautifulSoup

PTT_URL = "https://www.ptt.cc"


def get_web_page(url):
    resp = requests.get(url=url, cookies={"over18": "1"})
    if resp.status_code != 200:
        print("Invalid url:", resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, "html5lib")
    # Retrieve the link of previous page
    paging_div = soup.find("div", "btn-group btn-group-paging")
    prev_url = paging_div.find_all("a")[1]["href"]

    articles = []
    divs = soup.find_all("div", "r-ent")
    for d in divs:
        # If post date matched:
        if d.find("div", "date").text.strip() == date:
            # To retrieve the push count:
            push_count = 0
            push_str = d.find("div", "nrec").text
            if push_str:
                try:
                    push_count = int(push_str)
                except ValueError:
                    # If transform failed, it might be '爆', 'X1', 'X2', etc.
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
                        push_count = -10

            # To retrieve title and href of the article:
            if d.find("a"):
                href = d.find("a")["href"]
                title = d.find("a").text
                author = d.find("div", "author").text if d.find("div", "author") else ""
                articles.append(
                    {
                        "title": title,
                        "href": href,
                        "push_count": push_count,
                        "author": author,
                    }
                )

    return articles, prev_url


def get_author_ids(posts, pattern):
    ids = set()
    for post in posts:
        if pattern in post["author"]:
            ids.add(post["author"])
    return ids


def main():
    current_page = get_web_page(PTT_URL + "/bbs/Gossiping/index.html")
    if current_page:
        # To keep all of today's articles.
        articles = []
        # Today's date, here we remove the 0 at the head to match the format of PTT date.
        # API doc for strftime: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        # API doc for lstrip: https://www.tutorialspoint.com/python/string_lstrip.htm
        today = time.strftime("%m/%d").lstrip("0")
        current_articles, prev_url = get_articles(current_page, today)

        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)

        print("Today's 5566:")
        print(get_author_ids(articles, "5566"))

        print("\nThere are ", len(articles), " posts today.")
        threshold = 50
        print("Hot post(≥ %d push): " % threshold)
        for article in articles:
            if int(article["push_count"]) > threshold:
                print(article)
        # with as: https://openhome.cc/Gossip/Python/WithAs.html
        # json.dump: http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html
        with open("gossiping.json", "w", encoding="UTF-8") as file:
            json.dump(articles, file, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    main()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup10_gossiping4b.py

import requests
import time
import json
import re
from bs4 import BeautifulSoup

PTT_URL = "https://www.ptt.cc"
FREEGEOIP_API = "http://freegeoip.net/json/"


def get_web_page(url):
    resp = requests.get(url=url, cookies={"over18": "1"})
    if resp.status_code != 200:
        print("Invalid url: ", resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, "html5lib")
    # Retrieve the link of previous page
    paging_div = soup.find("div", "btn-group btn-group-paging")
    prev_url = paging_div.find_all("a")[1]["href"]

    articles = []
    divs = soup.find_all("div", "r-ent")
    for d in divs:
        # If post date matched:
        if d.find("div", "date").text.strip() == date:
            # To retrieve the push count:
            push_count = 0
            push_str = d.find("div", "nrec").text
            if push_str:
                try:
                    push_count = int(push_str)
                except ValueError:
                    # If transform failed, it might be '爆', 'X1', 'X2', etc.
                    if push_str == "爆":
                        push_count = 99
                    elif push_str.startswith("X"):
                        push_count = -10

            # To retrieve title and href of the article:
            if d.find("a"):
                href = d.find("a")["href"]
                title = d.find("a").text
                author = d.find("div", "author").text if d.find("div", "author") else ""
                articles.append(
                    {
                        "title": title,
                        "href": href,
                        "push_count": push_count,
                        "author": author,
                    }
                )

    return articles, prev_url


def get_ip(dom):
    # e.g., ※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 27.52.6.175
    pattern = "來自: \d+\.\d+\.\d+\.\d+"
    match = re.search(pattern, dom)
    if match:
        return match.group(0).replace("來自: ", "")
    else:
        return None


def main():
    print("取得今日文章列表:")
    current_page = get_web_page(PTT_URL + "/bbs/Gossiping/index.html")
    if current_page:
        articles = []
        today = time.strftime("%m/%d").lstrip("0")
        current_articles, prev_url = get_articles(current_page, today)
        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)

        length = len(articles)
        print("共 %d 篇文章" % length)

        for i in range(0, 10):
            print(articles[i])

        print()
        print()
        print("取得前10篇文章的資料")
        for article in articles[:10]:
            print(article["title"])

        print("取得前10篇文章的IP:")
        country_to_count = dict()
        for article in articles[:10]:
            print("查詢 IP:", article["title"])
            print("111")
            page = get_web_page(PTT_URL + article["href"])
            print("222")
            if page:
                ip = get_ip(page)
                print(ip)


if __name__ == "__main__":
    main()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\web_crawler\BeautifulSoup11_taiwanlottery.py

import requests
from bs4 import BeautifulSoup

url = "https://www.taiwanlottery.com.tw/"
r = requests.get(url)
# sp = BeautifulSoup(r.text, 'lxml')
sp = BeautifulSoup(r.text, "html.parser")
# 找到威力彩的區塊
datas = sp.find("div", class_="contents_box02")
# 開獎期數
title = datas.find("span", "font_black15").text
print("威力彩期數：", title)
# 開獎號碼
nums = datas.find_all("div", class_="ball_tx ball_green")
# 開出順序
print("開出順序：", end=" ")
for i in range(0, 6):
    print(nums[i].text, end=" ")
# 大小順序
print("\n大小順序：", end=" ")
for i in range(6, 12):
    print(nums[i].text, end=" ")
# 第二區
num = datas.find("div", class_="ball_red").text
print("\n第二區：", num)


print("------------------------------------------------------------")  # 60個
