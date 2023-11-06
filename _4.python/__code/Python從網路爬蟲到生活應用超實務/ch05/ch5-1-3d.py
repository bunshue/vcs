import requests
from bs4 import BeautifulSoup 

url = "https://fchart.github.io/Elements.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag_ans1 = soup.find("li", class_="response")
print(tag_ans1.text)
tag_ans2 = tag_ans1.find_next()
print(tag_ans2.text)

