import requests, json
from bs4 import BeautifulSoup

print('PC Home 電腦售價')
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc'

html = requests.get(url).text
products = json.loads(html)['prods']
for product in products:
    if product['price'] > 20000:
        print("NT$:{}, {}".format(product['price'], product['name']))





import requests, json
from bs4 import BeautifulSoup

url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=mac%20Mini&page=1&sort=sale/dc'
html = requests.get(url).text
products = json.loads(html)['prods']
message = ""
for product in products:
    if product['price'] > 20000:
        message = message + "NT$:{}, {}\n".format(product['price'], product['name'])
        
print("Mac Mini價格通知", message)

print("Done")


