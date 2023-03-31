#解讀本地網頁資料, 都是使用 html.parser 解析器

from bs4 import BeautifulSoup

print('解讀本地網頁資料2')

html_data = """
<html><head><title>網頁標題</title></head>
<p class="header"><h2>文件標題</h2></p>
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

soup = BeautifulSoup(html_data, 'html.parser') 
print("取得網頁標題")
print(soup.title)
print("取得網頁內容")
print(soup.text)
print(soup.title) # <title>網頁標題</title>
print(soup.find('h2')) # <h2>文件標題</h2>
print(soup.find_all('a')) 
print(soup.find_all("a", {"class":"red"}))
data1=soup.find("a", {"href":"http://example.com/one"})
print(data1.text) # First
data2 = soup.select("#link1") 
print(data2[0].text) # First
print(data2[0].get("href")) # http://example.com/one
print(data2[0]["href"])     # http://example.com/one
print(soup.find_all(['title','h2'])) # [<title>網頁標題</title>, <h2>文件標題</h2>]
print(soup.select('div img')[0]['src']) # http://example.com/three.jpg


print('解讀本地網頁資料3')

html_data = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <p id="p1">我是段落一</p>
      <p id="p2" class='red'>我是段落二</p>
  </body>
</html>
'''
soup = BeautifulSoup(html_data, 'html.parser')
#用find
print(soup.find('p'))
print(soup.find_all('p'))
print(soup.find('p', {'id':'p2', 'class':'red'}))
print(soup.find('p', id='p2', class_= 'red'))
#用select
print(soup.select('title'))
print(soup.select('p'))
print(soup.select('#p1'))
print(soup.select('.red'))


print('解讀本地網頁資料5')
html_data = '''
<html>
  <head><meta charset="UTF-8"><title>我是網頁標題</title></head>
  <body>
      <img src="http://www.ehappy.tw/python.png">
      <a href="http://www.e-happy.com.tw">超連結</a>
  </body>
</html>
'''
soup = BeautifulSoup(html_data, 'html.parser')
print(soup.select('img')[0].get('src'))
print(soup.select('a')[0].get('href'))
print(soup.select('img')[0]['src'])
print(soup.select('a')[0]['href'])


print('解讀本地網頁資料6')
html_data = """
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

soup = BeautifulSoup(html_data, 'html.parser') 
print(soup.title) # <title>網頁標題</title>
print(soup.find('h1')) # <h1>文件標題</h1>
print(soup.find_all('a')) 
print(soup.find_all("a", {"class":"red"}))
data1=soup.find("a", {"href":"http://example.com/one"})
print(data1.text) # First
data2 = soup.select("#link1") 
print(data2[0].text) # First
print(data2[0].get("href")) # http://example.com/one
print(data2[0]["href"])     # http://example.com/one
print(soup.find_all(['title','h1'])) # [<title>網頁標題</title>, <h1>文件標題</h1>]
print(soup.select('div img')[0]['src']) # http://example.com/three.jpg


print('解讀本地網頁資料7')

# 讀檔
filename = 'C:/_git/vcs/_4.cmpp/_python_test/data/beautifulsoup_data.html'

html_data = ""
with open(filename, "r", encoding="utf8") as file:
    html_data = file.read()

# BeautifulSoup解析原始碼
soup = BeautifulSoup(html_data, 'html.parser')
print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

# find h1
#尋找符合標籤的第一個節點
h1 = soup.find("h1")
print(h1)

# find by class
# 使用class屬性定位，但因為在Python中已經有class保留字了，所以改用class_
container = soup.find("div", class_="container")
print(container)

# find by id
# 用id屬性定位。
this = soup.find("h2", id="this")
print(this)

# find_all h2
# find_all()定位符合標籤的所有節點，回傳的是一個列表。
h2s = soup.find_all("h2")
print(h2s)
print(len(h2s)) # 共找到幾筆資料
print(h2s[1])   # 使用索引值

# find_all h1 and h2
# 定位多個標籤，則將標籤打包成一個列表就好了。limit屬性則可以限制數量。
h1_h2s = soup.find_all(["h1", "h2"], limit=3)
print(h1_h2s)
print(len(h1_h2s))


# select_one
# select_one()使用CSS選擇器的語法來定位節點
h1 = soup.select_one("h1")
print(h1)

# select
# select()其實就是使用CSS選擇器語法的find_all()
h2s = soup.select("h2")
print(h2s)
print(len(h2s)) # 共找到幾筆資料
print(h2s[1])   # 使用索引值

# select by class
# class 定位
p = soup.select_one("div.container")
print(p)

# select by id
# id定位
this = soup.select_one("h2#this")
print(this)

# 尋找parent和sibling
# this = soup.find("h2", id="this")
# print(this)
# print(this.find_previous_sibling())
# print(this.find_next_sibling())
# print(this.find_parent())

# 取得文字
# 定位到指定的節點後，可以使用text或string取得文字，或者也可以用getText()
h1 = soup.find("h1")
print(h1.getText())
print(h1.text)
print(h1.string)

# 取得屬性值
# 對於有屬性值的節點，就用get("屬性")或類似字典的方式["屬性"]取得屬性值。
# 取得<img>標籤中的src屬性值：
img = soup.find("img")
print(img["src"])
print(img.get("src"))



