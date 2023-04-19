#解讀本地網頁資料, 都是使用 html.parser 解析器

import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

# 讀檔
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/beautifulsoup_data.html'

html_data = ""
with open(filename, "r", encoding="big5") as file:
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
data1=soup.find("a", {"href":"https://easun.org/perl/perl-toc/ch05.html"})
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
print('取得 p, p2 class red', soup.find('p', id='p2', class_= 'red'))
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

print('解讀本地網頁資料3')

print('尋找符合標籤的第一個節點 find h1')
h1 = soup.find("h1")
print("取得<h1>??</h1>: ", h1)        #印出整行資料
print("取得<h1>??</h1>: ", h1.text)   #只印出text部分

print('尋找符合標籤的第一個節點 find by class')
# 使用class屬性定位，但因為在Python中已經有class保留字了，所以改用class_
container = soup.find("div", class_="container")
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

#下載圖片
import requests
img = requests.get(img["src"])
with open('ccccc.png', "wb") as file:
    file.write(img.content)
print('圖片下載完成!')

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
            with open(os.path.join(images_dir,filename),'wb') as f:
                f.write(image.read())  
            n+=1
            if n>=1000: # 最多下載 1000 張
                break
            '''
        except:
            print("{} 無法讀取!".format(filename))
            
print("共下載",n,"張圖片")



