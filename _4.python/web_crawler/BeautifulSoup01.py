# Python 測試 BeautifulSoup
#解讀 本地 網頁資料, 都是使用 html.parser 解析器

print('------------------------------------------------------------')	#60個
print('準備工作')

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

print('------------------------------------------------------------')	#60個
print('BeautifulSoup 測試 1')

# 讀檔
filename = 'C:/_git/vcs/_1.data/______test_files1/beautifulsoup_data.html'

html_data = ""
with open(filename, "r", encoding = "big5") as file:
    html_data = file.read()

print('解讀本地網頁資料1')

soup = BeautifulSoup(html_data, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
print("取得網頁標題 : ", soup.title)  #印出整行資料
print("取得網頁標題 : ", soup.title.text) #只印出text部分
#print("取得網頁內容 : ", soup.text)

print("取得<h1>??</h1>: ", soup.find('h1'))       #印出整行資料
print("取得<h1>??</h1>: ", soup.find('h1').text)  #只印出text部分
print("取得全部 title h1: ", soup.find_all(['title', 'h1'])) # [..., ...]
print("取得文字")
print("取得全部 a : ", soup.find_all('a'))
print('有3個, 需要縮小範圍')
print("取得全部 a class red : ", soup.find_all("a", {"class":"red"}))
print('有2個, 需要縮小範圍')
data1 = soup.find("a", {"href":"https://easun.org/perl/perl-toc/ch05.html"})
print("取得a 指明 href: ", data1)   #印出整行資料
print("取得a 指明 href: ", data1.text) #只印出text部分

print("取得超連結")
data2 = soup.select("#link1")
print("取得link1: ", data2)   #印出整行資料
print("取得link1 text: ", data2[0].text) #只印出text部分
print("取得link1 get : ", data2[0].get("href")) #https://easun.org/perl/perl-toc/ch01.html
print("取得link1 href: ", data2[0]["href"])     #https://easun.org/perl/perl-toc/ch01.html

print("取得圖片超連結")
print("取得div img: ", soup.select('div img')[0]['src']) #https://easun.org/perl/perl-toc/index_2.png

print('解讀本地網頁資料2')

#用find
print('取得一個 p', soup.find('p'))
print('取得全部 p', soup.find_all('p'))
print('取得 p, p2 class red', soup.find('p', {'id':'p2', 'class':'red'}))
print('取得 p, p2 class red', soup.find('p', id = 'p2', class_ = 'red'))
#用select
print('select title', soup.select('title'))
print('select p', soup.select('p'))
print('select #p1', soup.select('#p1'))
print('select .red', soup.select('.red'))
#用select
print('取得圖片超連結 取得 img src', soup.select('img')[0].get('src'))
print('取得網頁超連結 取得 a href', soup.select('a')[0].get('href'))
print('取得圖片超連結 取得 img src', soup.select('img')[0]['src'])
print('取得網頁超連結 取得 a href', soup.select('a')[0]['href'])

print('多重條件選擇')
data = soup.select('div div p') #尋找 div 標籤裡面的 div 標籤裡面的 p 標籤 三者都要符合的抓出來
print('符合條件的資料', len(data), '筆')
print(data)

print('解讀本地網頁資料3')

print('尋找符合標籤的第一個節點 find h1')
h1 = soup.find("h1")
print("取得<h1>??</h1>: ", h1)        #印出整行資料
print("取得<h1>??</h1>: ", h1.text)   #只印出text部分

print('尋找符合標籤的第一個節點 find by class')
# 使用class屬性定位，但因為在Python中已經有class保留字了，所以改用class_
container = soup.find("div", class_ = "container")
print("取得div container: ", container)        #印出整行資料
print("取得div container: ", container.text)   #只印出text部分

print('尋找符合標籤的第一個節點 find by id')
# 用id屬性定位。
this = soup.find("h2", id = "this")
print("取得h2 this: ", this)        #印出整行資料
print("取得h2 this: ", this.text)   #只印出text部分

print('尋找全部 h2')
# find_all()定位符合標籤的全部節點，回傳的是一個列表。
h2s = soup.find_all("h2")
length = len(h2s)
print('共找到', length, '筆資料')
for nn in range(length):
    print(h2s[nn].text)   # 使用索引值, 只印出text部分
#print("取得全部 h2: ", h2s)        #印出全部資料, 一個list

# find_all h1 and h2
# 定位多個標籤，則將標籤打包成一個列表就好了。limit屬性則可以限制數量。
print('尋找全部 h1 h2')
h1_h2s = soup.find_all(["h1", "h2"], limit=3)
length = len(h1_h2s)
print('共找到', length, '筆資料')
for nn in range(length):
    print(h1_h2s[nn].text)   # 使用索引值, 只印出text部分
#print("取得全部 h1 h2: ", h1_h2s)        #印出全部資料, 一個list

#用select_one
# select_one()使用CSS選擇器的語法來定位節點
h1 = soup.select_one("h1")
print(h1)
print("取得<h1>??</h1>: ", h1)        #印出整行資料
print("取得<h1>??</h1>: ", h1.text)   #只印出text部分

#用select
# select()其實就是使用CSS選擇器語法的find_all()
h2s = soup.select("h2")
length = len(h2s)
print('共找到', length, '筆資料')
for nn in range(length):
    print(h2s[nn].text)   # 使用索引值, 只印出text部分
#print("取得全部 h2: ", h2s)        #印出全部資料, 一個list

#用select_one by class
# class 定位
p = soup.select_one("div.container")
print("取得div.container: ", p)        #印出整行資料
print("取得div.container: ", p.text)   #只印出text部分

#用select_one by id
# id定位
this = soup.select_one("h2#this")
print("h2#this: ", this)        #印出整行資料
print("h2#this: ", this.text)   #只印出text部分

# 尋找parent和sibling
# this = soup.find("h2", id="this")
# print(this)
# print(this.find_previous_sibling())
# print(this.find_next_sibling())
# print(this.find_parent())

# 取得文字
# 定位到指定的節點後，可以使用text或string取得文字，或者也可以用getText()
h1 = soup.find("h1")
print('h1 getText(): ', h1.getText())
print('h1 text: ', h1.text)
print('h1 strint: ', h1.string)
print("取得<h1>??</h1>: ", h1)        #印出整行資料
print("取得<h1>??</h1>: ", h1.text)   #只印出text部分

# 取得屬性值
# 對於有屬性值的節點，就用get("屬性")或類似字典的方式["屬性"]取得屬性值。
# 取得<img>標籤中的src屬性值：
img = soup.find("img")
print('取得圖片超連結 取得 img src', img["src"])
print('取得圖片超連結 取得 img src', img.get("src"))

#下載圖片 另存新檔
filename = img["src"].split('/')[-1]  # 取得圖檔名
foldername = 'C:/_git/vcs/_1.data/______test_files2/'
filename2 = os.path.join(foldername, filename)
    
img = requests.get(img["src"])

with open(filename2, "wb") as file:
    file.write(img.content)
print('圖片下載完成, 檔案 : ' + filename2)

print('下載網頁中的所有圖片')

# 以標題建立目錄儲存圖片
title = soup.title.text
images_dir = '下載圖片_' + title + "/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

#all_imgs = soup.find_all('img', {"class": "photo_img photo-img"})
all_imgs = soup.find_all('img')
print(all_imgs)

# 處理所有 <img> 標籤
n=0
for img in all_imgs:
    print(img)
    # 讀取 src 屬性內容
    src=img.get('src')
    print(src)
    # 讀取 .jpg 檔
    if src != None and ('.png' in src):
        # 設定圖檔完整路徑
        full_path = src
        print(full_path)
        filename = full_path.split('/')[-1]  # 取得圖檔名
        print(filename)
        # 儲存圖片
        try:
            print(full_path)
            image = urlopen(full_path) #問題在此
            print('aaaaaaaaaaaa')
            '''
            with open(os.path.join(images_dir, filename),'wb') as f:
                f.write(image.read())  
            n+=1
            if n>=1000: # 最多下載 1000 張
                break
            '''
        except:
            print("{} 無法讀取!".format(filename))
            
print("共下載",n,"張圖片")


print('------------------------------------------------------------')	#60個
print('BeautifulSoup 測試 2')

html_data = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
</div>
"""

soup = BeautifulSoup(html_data, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

print('用 re 搭配搜尋')
print('搜尋網頁中的 e-mail')
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html_data)
for email in emails:
    print(email)

print('搜尋網頁中的 價格')
price = re.findall(r"[\d]+", soup.select('.price')[0].text)[0] #價格
print(price)

print('搜尋網頁中的 jpg圖片連結')
regex = re.compile('.*\.jpg')
imglist = soup.find_all("img", {"src":regex})
for img in imglist:
    print(img["src"])


print('------------------------------------------------------------')	#60個
print('BeautifulSoup 測試 3')


from bs4 import BeautifulSoup

html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
'''

sp = BeautifulSoup(html, 'lxml')

print(sp.find('p'))
print(sp.find_all('p'))
print(sp.find('p', {'id':'p2', 'class':'red'}))
print(sp.find('p', id='p2', class_= 'red'))


print('------------------------------------------------------------')	#60個
print('BeautifulSoup 測試 4')

from bs4 import BeautifulSoup

html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')

print(sp.select('title'))
print(sp.select('p'))
print(sp.select('#p1'))
print(sp.select('.red'))

print('------------------------------------------------------------')	#60個
print('BeautifulSoup 測試 5')


from bs4 import BeautifulSoup

html = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
'''
sp = BeautifulSoup(html, 'lxml')

print(sp.select('img')[0].get('src'))
print(sp.select('a')[0].get('href'))
print(sp.select('img')[0]['src'])
print(sp.select('a')[0]['href'])


print('------------------------------------------------------------')	#60個
print('BeautifulSoup 測試 6')

html = """
<html><head><title>網頁標題</title></head>
<h1>文件標題</h1>
<div class="content">
    <div class="item1">
        <a href="http://example.com/one" class="red" id="link1">First</a>
        <a href="http://example.com/two" class="red" id="link2">Second</a>
    </div>
    <a href="http://example.com/three" class="blue" id="link3">
        <img src="http://example.com/three.jpg">Third
    </a>
</div>
"""

from bs4 import BeautifulSoup
sp = BeautifulSoup(html,'lxml') 

print(sp.title) # <title>網頁標題</title>

print(sp.find('h1')) # <h1>文件標題</h1>

print(sp.find_all('a')) 
print(sp.find_all("a", {"class":"red"}))

data1=sp.find("a", {"href":"http://example.com/one"})
print(data1.text) # First

data2 = sp.select("#link1") 
print(data2[0].text) # First
print(data2[0].get("href")) # http://example.com/one
print(data2[0]["href"])     # http://example.com/one

print(sp.find_all(['title','h1'])) # [<title>網頁標題</title>, <h1>文件標題</h1>]

print(sp.select('div img')[0]['src']) # http://example.com/three.jpg






print('BeautifulSoup 測試 作業完成')



