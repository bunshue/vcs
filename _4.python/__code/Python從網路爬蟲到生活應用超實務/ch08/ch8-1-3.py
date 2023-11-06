from bs4 import BeautifulSoup
import requests

url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
item_lst = soup.find("div", class_="item-list")
items = item_lst.find_all("div", class_="restaurant-item")
print(len(items))
for index in range(5):
    item = items[index]
    title = item.find("a", class_="title-text")
    if title: print(title.text)
    address = item.find("div", class_="address-row")
    if address: print(address.text)
    avg_price = item.find("div", class_="avg-price")
    if avg_price: print(avg_price.text[2:])
    message = item.find("div", class_="message-text")
    if message: print(message.text)
    print("-------------------")

