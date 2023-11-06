from bs4 import BeautifulSoup
import requests

url = "https://www.railway.gov.tw/tra-tip-web/tip/tip004/tip421/restCode?RestNo=A110"
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
lst = soup.find("ul", class_="shop-item")
items = lst.find_all("li") 
print(len(items))
for item in items:
    title = item.find("div", class_="pro-title")
    print("便當名稱:", title.text)
    price = item.find("strong")
    print("便當價格:", price.text)
    print("-------------------------------")        


