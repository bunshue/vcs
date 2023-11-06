from bs4 import BeautifulSoup
import requests
import csv

csvfile = "TaiwanRailway.csv"
url = "https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/querybytime"
post_data = {
    "startStation": "1000-臺北",
    "endStation": "1100-中壢",
    "transfer": "ONE",
    "rideDate": "2020/08/20",
    "startOrEndTime": "true",
    "startTime": "00:00",
    "endTime": "23:59",
    "trainTypeList": "ALL",   
    "query": "查詢" }

r = requests.post(url, data=post_data)
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
tag_table = soup.find("table", class_="itinerary-controls") 
title_row = tag_table.find("tr")                       
rows = tag_table.find_all("tr", class_="trip-column")  
rows.insert(0, title_row)

with open(csvfile, 'w+', newline='', encoding="utf-8") as fp:
    writer = csv.writer(fp)    
    for row in rows:
        lst = []
        for cell in row.find_all(["td", "th"]):
            lst.append(cell.text.replace("\n","").replace("\r",""))
        writer.writerow(lst)