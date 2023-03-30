def showsite(siteurl):
    html = requests.get(siteurl).text
    soup = BeautifulSoup(html,'html.parser')  
    kind=soup.select(".content-header-desc__detail")[1].text.strip() #分類
    area=soup.select(".content-header-desc__detail")[2].text.strip() #區
    item_desc=soup.select(".location-item .location-item__desc") #店名、地址
    name=item_desc[0].select("p")[0].text #店名    
    imgurl=soup.find('div',{'class':'images-featured-big-slider'}).get('style').split("'")[1] # 圖片名稱    
    lat=soup.select("#js-location-map")[0]["data-lat"] #緯度
    lng=soup.select("#js-location-map")[0]["data-lon"] #經度
    tel=soup.select(".location-item .location-item__desc")[2].text.strip()  #電話 
    addr=item_desc[0].select("p")[1].text.replace(" ","").replace("\n","").strip() #地址
    desc=soup.select(".restaurant-desc")[0].text.strip() #說明
    working_hours=soup.select(".location-item .location-item__desc")[1].text.strip()  #營業時間
    print("分類:",kind)    #分類
    print("地區:",area)    #地區
    print("店名:",name)    #店名
    print("網址:",siteurl) #網址
    print("圖片名稱:",imgurl)  #圖片名稱
    print("緯度:",lat)     #緯度
    print("經度:",lng)     #經度
    print("電話:",tel)     #電話
    print("地址:",addr)    #地址
    print("說明:",desc)    #說明
    print("營業時間:",working_hours+"\n")  #營業時間

def getpageurl(page,url):
    global n,totpages
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser') 
    items = soup.select('.grid-restaurants__item__inner')
    print("第" + str(page)+"頁,共有"+ str(len(items)) + "間")
    for item in items:
        n+=1
        print("n=",n)
        itemurl=item.select('.resto-inner-title a')[0]['href'] #網址
        siteurl=rooturl + itemurl #組成完整網址
        showsite(siteurl) #顯示該店資訊
        if n==1:
            totpages=int(soup.find("input",{"class":"form-control"})['data-max_page']) # 總頁數

#主程式    
import requests
from bs4 import BeautifulSoup        
n=0 #計算總共有多少家店
homeurl = 'https://guide.michelin.com/tw/taipei/restaurants?max=30&sort=relevance'
rooturl='https://guide.michelin.com'
getpageurl(1,homeurl)  # 首頁

for page in range(2,totpages+1): #第 2~totpages頁
    html = requests.get(homeurl).text
    soup = BeautifulSoup(html,'html.parser') 
    path=soup.find("a",{"class":"page-arrow"}) # 「>」 下一頁按鈕
    fullurl = path["href"] #讀取 href 內容
    #以「?」分割，刪除前面字串中的最後一個字元，再加上 page 後，組成完整的路徑
    url = rooturl + fullurl.split("?")[0][:-1] + str(page)+ "?" + fullurl.split("?")[1]
    getpageurl(page,url)
    
print("\n總共有",n,"間")