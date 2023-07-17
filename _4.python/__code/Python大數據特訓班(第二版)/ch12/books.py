def showkind(url,kind):
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml') 
    try:
        pages=int(soup.select('.cnt_page span')[0].text)  # 該分類共有多少頁
        print("共有",pages,"頁")
        for page in range(1,pages+1):
            pageurl=url + '&page=' + str(page).strip()
            print("第",page,"頁",pageurl)
            #showpage(pageurl,kind)
    except:  # 沒有分頁的處理
        showpage(url,kind)   

def showpage(url,kind):
    html = requests.get(url,headers=headers).text
    soup = BeautifulSoup(html,'lxml') 
    #近期新書、在 class="mod type02_m012 clearfix" 中
    res = soup.find_all('div',{'class':'mod type02_m012 clearfix'})[0]
    items=res.select('.item')  # 所有 item
    n=0  # 計算該分頁共有多少本書
    for item in items:
        msg=item.select('.msg')[0] 
        src=item.select('a img')[0]["src"]
        title=msg.select('a')[0].text  #書名
        imgurl=src.split("?i=")[-1].split("&")[0] #圖片網址
        author=msg.select('a')[1].text #作者
        publish=msg.select('a')[2].text #出版社
        date=msg.find('span').text.split("：")[-1] #出版日期
        onsale=item.select('.price .set2')[0].text #優惠價
        content=item.select('.txt_cont')[0].text.replace(" ","").strip()  #內容
        print("\n分類：" + kind)  
        print("書名：" + title)   
        print("圖片網址：" + imgurl)  
        print("作者：" + author)      
        print("出版社：" + publish)  
        print("出版日期：" + date) 
        print(onsale) # 優惠價 
        print("內容：" + content)     
        n+=1
        print("n=",n)


def twobyte(kindno):
    if kindno<10:
        kindnostr="0"+str(kindno)
    else:
        kindnostr=str(kindno) 
    return kindnostr

#主程式
import requests
from bs4 import BeautifulSoup 
kindno=1  # 要下載的分類，預設為第1分類：文學小說
homeurl = 'http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1'
mode="?o=5&v=1" #顯示模式：直式  排序依：暢銷度
url="http://www.books.com.tw/web/books_nbtopm_" 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
html = requests.get(homeurl,headers=headers).text
soup = BeautifulSoup(html,'lxml') 

#中文書新書分類，取得分類資訊
res = soup.find('div', class_='mod_b type02_l001-1 clearfix')
hrefs=res.select("a")

kindno=int(input("請輸入要下載的分類："))
if 0 < kindno <= len(hrefs):
    kind = hrefs[kindno-1].text #分類名稱
    print("下載的分類編號：{}   分類名稱：{}" .format(kindno,kind))
    # 下載指定的分類
    kindurl = url + twobyte(kindno) + mode # 分類網址  
    print(kindurl)
    showkind(kindurl, kind) # 顯示該分類所有書籍
else:
    print("分類不存在!")     