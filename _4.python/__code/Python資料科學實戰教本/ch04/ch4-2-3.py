from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 走訪下一層HTML標籤
print(soup.html.body.div.div.p.a.text)
print("----------------------")
# 走訪上一層HTML標籤
tag_div = soup.select_one("#q1") # 找到第1題的<div>標籤
tag_li = tag_div.ul.li    # 走訪到之下的<ul>
print(tag_li.text)
# 使用parent屬性取得父標籤
print(tag_li.parent.parent.p.a.text)
print("----------------------")
tag_div = soup.select_one("#q2") # 找到第2題的<div>標籤
print(tag_div.find_previous_sibling().p.a.text)
print(tag_div.find_next_sibling().p.a.text)



