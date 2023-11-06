from bs4 import BeautifulSoup
import requests
from flask import Flask, jsonify
 
url = "https://ifoodie.tw/explore/台北市/list?sortby=rating"

def getTop(limit=5):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    item_lst = soup.find("div", class_="item-list")
    items = item_lst.find_all("div",class_="restaurant-item",limit=limit)
    outputs = []
    for item in items:
        title = item.find("a", class_="title-text")
        title_txt = title.text if title else "N/A"
        address = item.find("div", class_="address-row") 
        address_txt = address.text if address else "N/A"
        price = item.find("div", class_="avg-price")
        price_txt = price.text[2:] if price else "N/A"
        result = { "title":   title_txt, 
                   "address": address_txt,
                   "price":   price_txt }
        outputs.append(result)        
    return outputs

app = Flask(__name__)
@app.route("/")
def main():
    return jsonify(getTop(5))
@app.route("/top/<limit>")
def top(limit):
    return jsonify(getTop(int(limit)))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
