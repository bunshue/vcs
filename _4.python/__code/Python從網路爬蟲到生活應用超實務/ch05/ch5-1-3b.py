import requests
from bs4 import BeautifulSoup 

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag = soup.find("h2")
print("h2: ", tag.text)
tag = soup.find("b")
print("b: ", tag.text)
tags = soup.find_all("b")
print("b: ", tags[0].text)
tag = soup.find("li", {"id":"q2"})
tag_q = tag.find("b")
print("Question: ", tag_q.text)
tags_a = tag.find_all("li", class_="response")
for tag in tags_a:                           
    print("Ans: ", tag.text)

