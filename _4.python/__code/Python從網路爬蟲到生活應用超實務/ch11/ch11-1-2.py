import requests, os 
from bs4 import BeautifulSoup

url = "https://fchart.github.io/"
os.makedirs("fchart", exist_ok=True)
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
for img in soup.find_all("img"):
    try:
        imgUrl = url + img.get("src").replace('\\','/')
        print("下載:", imgUrl)
        res = requests.get(imgUrl)
    except requests.exceptions.MissingSchema:
        print("圖檔下載錯誤...")
        continue
    
    imgFile = os.path.join("fchart", os.path.basename(imgUrl))
    fp = open(imgFile, "wb")
    for chunk in res.iter_content(100000):
        fp.write(chunk)
    fp.close()
print("結束網頁圖檔下載...")
