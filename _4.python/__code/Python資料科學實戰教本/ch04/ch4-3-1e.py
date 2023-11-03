from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")   
    
# 測試取出<li>標籤的內容
tag_str = soup.find(text="女 - ")
print(tag_str)
tag_li = soup.find(class_="response")
print(tag_li.text)
print(tag_li.string)
print(tag_li.span.string)

