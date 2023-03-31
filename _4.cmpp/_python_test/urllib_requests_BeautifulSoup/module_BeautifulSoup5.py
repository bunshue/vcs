import requests
from bs4 import BeautifulSoup

'''
print('有無 cookies 之比較')

#gossiping
url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #八卦板的網址

print('無 cookies')
html_data = requests.get(url)
#print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print('有 cookies')
cookies = {'over18':'1'}
html_data = requests.get(url, cookies=cookies)
#print(html_data.text)
soup = BeautifulSoup(html_data.text, "html.parser")
print(soup.prettify())

print('BeautifulSoup 測試 1a 使用 cookie')

url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #八卦板的網址

my_headers = {"cookie": "over18=1"}  # cookie設定

response = requests.get(url, headers = my_headers)  # 放在headers欄位中傳送
soup = BeautifulSoup(response.text, "html.parser")  # 解析原始碼
#print(soup.prettify())
links = soup.find_all("div", class_ = "title")    # 文章標題
#print(links)
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print('BeautifulSoup 測試 1b 使用 session')

# post要傳的資料
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

rs = requests.session() # 用session紀錄此次使用的cookie
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)   # post傳遞資料
response = rs.get(url)  # 再get一次PTT八卦板首頁
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
links = soup.find_all("div", class_="title")    # 文章標題
for link in links:
    print(link.text.strip())  # strip()用來刪除文字前面和後面多餘的空白

print('BeautifulSoup 測試 1c')

import requests
from bs4 import BeautifulSoup

url = 'https://www.ptt.cc/bbs/Gossiping/index.html' #八卦板的網址

payload = {
   'from': url,
	'yes': 'yes'
}
headers = {
	'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
rs = requests.Session()
rs.post('https://www.ptt.cc/ask/over18', data=payload, headers=headers)
res = rs.get(url, headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
items = soup.select('.r-ent')
for item in items:
    print(item.select('.date')[0].text, item.select('.author')[0].text, item.select('.title')[0].text)
'''


'''
import requests
from bs4 import BeautifulSoup

# post要傳的資料
payload = {
    'from': '/bbs/Gossiping/index.html',
    'yes': 'yes'
}

# 用session紀錄此次使用的cookie
rs = requests.session()
# post傳遞資料
response = rs.post("https://www.ptt.cc/ask/over18", data=payload)
# 再get一次PTT八卦板首頁
response = rs.get("https://www.ptt.cc/bbs/Gossiping/index.html")
print(response.status_code)

root = BeautifulSoup(response.text, "html.parser")
links = root.find_all("div", class_="title")    # 文章標題
for link in links:
    page_url = "https://www.ptt.cc"+link.a["href"]
    print(page_url)
    response = rs.get(page_url)
    result = BeautifulSoup(response.text, "html.parser")
    main_content = result.find("div", id="main-content")
    article_info = main_content.find_all("span", class_="article-meta-value")
    if len(article_info) != 0:
        author = article_info[0].string  # 作者
        title = article_info[2].string  # 標題
        time = article_info[3].string   # 時間
    else: # 避免有沒有資訊的狀況
        author = "無"  # 作者
        title = "無"  # 標題
        time = "無"   # 時間
    #print(author + ' ' + title + ' ' + time)
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

'''
    
'''
import json
import pandas as pd
import requests

# 台灣證券交易所，個股日成交資訊
search_date = '20220101'
search_stock = '2330'
url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+search_date+'&stockNo='+search_stock

# 取得股票資料json字串
response = requests.get(url)
#print(response.text)

# 從json字串轉為python的字典格式
json_data = json.loads(response.text)
datas = json_data["data"]
fields = json_data["fields"]
print(datas)    #由List組成的二維陣列
print(fields)

# 存成Pandas的Dataframe
df = pd.DataFrame(datas, columns=fields)
print(df)

# Pandas匯出
# 轉成csv檔
df.to_csv("./month_stock.csv", encoding="big5")
# 轉成xlsx檔
df.to_excel("./month_stock.xlsx", encoding="big5")
# 轉成html檔
df.to_html("./month_stock.html")


#抓一整年的資料 2022年
year_df = pd.DataFrame()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
}
search_year = '2022'
search_stock = '2330'
#url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+search_date+'&stockNo='+search_stock

# 從1到12月
for m in range(1, 13):
    print(m)
    url = ('https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date='+search_year+'{0:02d}01&stockNo='+search_stock).format(m)
    print(url)

    # 取得股票資料json字串
    response = requests.get(url, headers=headers)
    # print(response.text)

    # 從json字串轉為python的字典格式
    json_data = json.loads(response.text)
    datas = json_data["data"]
    fields = json_data["fields"]

    # 存成Pandas的Dataframe
    month_df = pd.DataFrame(datas, columns=fields)
    # print(month_df)

    # 合併於整年的Dataframe
    year_df = year_df.append(month_df, ignore_index=True)

#print(year_df)
# 轉成csv檔
year_df.to_csv("./year_stock.csv", encoding="big5")
'''





import pandas as pd

# 讀取csv
df = pd.read_csv("./month_stock.csv", encoding="big5")
#print(df)

'''
# 讀取excel
df2 = pd.read_excel("./month_stock.xlsx")
print(df2)

# 讀取html
df3 = pd.read_html("./month_stock.html", encoding="utf8")
print(df3)
'''

#使用 Matplotlib 畫圖
import matplotlib.pyplot as plt


# 篩選我們要的資料
date = df["日期"]
high_price = df["最高價"]
low_price = df["最低價"]
end_price = df["收盤價"]

# 繪圖
#plt.plot(date, high_price)
#plt.plot(date, low_price)
#plt.plot(date, end_price)

plt.plot(date, high_price, color="#ff2121")
plt.plot(date, low_price, color="#00bd42", linewidth=5)
plt.plot(date, end_price, color="#005de0", linestyle="dashed")

'''
plt.xlabel("日期")    # x軸標籤
plt.ylabel("價格")    # y軸標籤
plt.legend(["最高價", "最低價", "收盤價"], loc="lower right")    # 圖示，共有左下、左上、右下、右上四個方位
plt.title("110年8月股市趨勢圖")    # 主標題
'''
plt.grid(True)    # 是否有網格?

# 存成圖片, 要放在show()之前
# plt.savefig("matplotlib_chart.png")

# 顯示圖片
plt.show()

#使用 Pandas 畫圖

# 篩選我們要的資料
chart_df = df[["日期", "最高價", "最低價", "收盤價"]]
# 將日期設為x軸
chart_df.set_index("日期", inplace=True)
print(chart_df)


# 繪圖
chart = chart_df.plot(xlabel="日期", ylabel="價格", title="110年8月股市趨勢圖", legend=True)
#chart = chart_df.plot(xlabel="日期", ylabel="價格", title="109年股市趨勢圖", legend=True)
plt.grid()


# 存成圖片, 要放在show()之前
# plt.savefig("pandas_chart.png")
# 顯示圖片
plt.show()




    
