from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有標籤串列
tag_all = tag_div.find_all(True)
for tag in tag_all:
    print(tag.name)

