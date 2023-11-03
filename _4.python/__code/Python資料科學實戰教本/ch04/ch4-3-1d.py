from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")

# 使用文字內容來搜尋標籤
tag_str = soup.find(text="請問你的")
print(tag_str)
tag_str = soup.find(text="10")
print(tag_str)
print(type(tag_str))        # NavigableString型態
print(tag_str.parent.name)  # 父標籤名稱
tag_str = soup.find(text="男 - ")
print(tag_str)