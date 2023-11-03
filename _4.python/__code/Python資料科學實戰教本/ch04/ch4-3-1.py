from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<a>標籤
tag_a = soup.find("a") 
print(tag_a.text)
# 呼叫多次find()方法
tag_p = soup.find(name="p")
tag_a = tag_p.find(name="a")
print(tag_p.a.text)
print(tag_a.text)


