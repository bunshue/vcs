from bs4 import BeautifulSoup
from bs4.element import NavigableString

with open("Example.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
# 使用屬性取得所有子標籤
tag_div = soup.select("#q2") # 找到第2題
tag_ul = tag_div[0].ul       # 走訪到之下的<ul>            
for child in tag_ul.children:
    if not isinstance(child, NavigableString):
        print(child.name)
        for tag in child:
            if not isinstance(tag, NavigableString):
                print(tag.name, tag.string)
            else:
                print(tag.replace('\n', ''))