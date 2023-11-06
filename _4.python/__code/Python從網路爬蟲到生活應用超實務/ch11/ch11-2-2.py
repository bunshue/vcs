import requests, os 
from selenium import webdriver
import time
from bs4 import BeautifulSoup

keyword = "dog"
pathdir = "imgur2"
url = "http://imgur.com/search?q=" + keyword
os.makedirs(pathdir, exist_ok=True)
driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get(url)
for x in range(3):
    js = "window.scrollTo(0, document.body.scrollHeight)"
    driver.execute_script(js)
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, "lxml")
images = soup.find_all("a", class_="image-list-link")
print("圖檔數:", len(images))
for img in images:
    try:
        imgUrl = "http:" + img.find("img").get("src")
        print("下載:", imgUrl)
        res = requests.get(imgUrl)
    except requests.exceptions.MissingSchema:
        print("圖檔下載錯誤...")
        continue
    
    imgFile = os.path.join(pathdir, os.path.basename(imgUrl))
    fp = open(imgFile, "wb")
    for chunk in res.iter_content(100000):
        fp.write(chunk)
    fp.close()
print("結束 Imgur 網頁圖檔下載...")
driver.quit()
