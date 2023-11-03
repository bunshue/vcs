from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋指定標籤下的直接子標籤
tag_a = soup.select("p > a")
for tag in tag_a:
    print(tag["href"])
tag_li = soup.select("ul > li:nth-of-type(2)")
for tag in tag_li:
    print(tag.text.replace("\n", ""))
tag_span = soup.select("div > #email")
for tag in tag_span:
    print(tag.prettify())  


