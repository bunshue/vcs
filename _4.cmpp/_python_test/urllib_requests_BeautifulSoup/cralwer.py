from bs4 import BeautifulSoup

# 讀檔
response = ""
with open("crawl_me.html", "r", encoding="utf8") as file:
    response = file.read()

# BeautifulSoup解析原始碼
soup = BeautifulSoup(response, "html.parser")
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
