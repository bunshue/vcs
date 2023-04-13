# python import module : urllib

from urllib.request import urlopen

import urllib.request as req

url = 'https://www.ptt.cc/bbs/movie/index.html'

#建立一個Request物件, 附加Request Headers的資訊
request = req.Request(url, headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    })
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
#print(data)

import bs4
root = bs4.BeautifulSoup(data, "html.parser")
print(root.title)   #抓整個標籤
print(root.title.text)  #抓標籤裡面的文字
print(root.title.string)#抓標籤裡面的文字

#尋找class = 'title' 的 div 標籤
titles = root.find("div", class_= "title")

#尋找所有class = 'title' 的 div 標籤 用列表表示
titles = root.find_all("div", class_= "title")

#print(titles)
for title in titles:
    if title.a != None: #如果標題包含a標籤(沒有被刪除), 印出來
        print(title.a.string)

print('作業完成')

