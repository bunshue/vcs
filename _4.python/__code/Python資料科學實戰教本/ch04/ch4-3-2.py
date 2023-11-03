from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 找出所有問卷的題目串列
tag_list = soup.find_all("p", class_="question")
print(tag_list[0].prettify())

for question in tag_list:
    print(question.a.text)
