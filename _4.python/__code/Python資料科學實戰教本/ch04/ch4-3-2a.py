from bs4 import BeautifulSoup

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")     
    
# 找出前2個問卷的題目串列
tag_list = soup.find_all("p", class_="question", limit=2)
print(len(tag_list))

for question in tag_list:
    print(question.a.text)
