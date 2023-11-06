import requests 
from bs4 import BeautifulSoup
import csv

url = "https://www.bbc.com/zhongwen/trad/business"
csvfile = "news.csv"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
tag_div = soup.find("div", class_="eagle")
tags_div = tag_div.find_all("div", class_="eagle-item")
output = []
for tag in tags_div:
    item = []
    title = tag.find("h3", class_="title-link__title").find("span") 
    item.append(title.text.strip())
    summary = tag.find("p", class_="eagle-item__summary")
    item.append(summary.text)
    a = tag.find("a")
    item.append(a.get("href", None))
    output.append(item)
    
with open(csvfile, 'w+', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(["title","summary","href"])
    for row in output:
        writer.writerow(row)
    


