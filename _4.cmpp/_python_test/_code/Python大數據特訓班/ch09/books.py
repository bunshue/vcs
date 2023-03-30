def showbook(url,kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser') 
    try:
        pages=int(soup.select('.cnt_page span')[0].text)  # 該分類共有多少頁
        print("共有",pages,"頁")
        for page in range(1,pages+1):
            pageurl=url + '&page=' + str(page).strip()
            print("第",page,"頁",pageurl)
            showpage(pageurl,kind)
    except:  # 沒有分頁的處理
        showpage(url,kind)        

def showpage(url,kind):
    html = requests.get(url).text
    soup = BeautifulSoup(html,'html.parser') 
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
#
#        if n==2: break  # 開發階段

def twobyte(kindno):
    if kindno<10:
        kindnostr="0"+str(kindno)
    else:
        kindnostr=str(kindno) 
    return kindnostr

#主程式
import requests
from bs4 import BeautifulSoup 
kindno=1  # 計算共有多少分類  
homeurl = 'http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1'
mode="?o=5&v=1" #顯示模式：直式  排序依：暢銷度
url="http://www.books.com.tw/web/books_nbtopm_" 
html = requests.get(homeurl).text
soup = BeautifulSoup(html,'html.parser') 
#中文書新書分類，算出共有多少分類
res = soup.find('div',{'class':'mod_b type02_l001-1 clearfix'})
hrefs=res.select("a")
for href in hrefs:
    kindurl=url + twobyte(kindno) + mode # 分類網址  
    print("\nkindno=",kindno)  
    kind=href.text #分類
    showbook(kindurl,kind) # 顯示該分類所有書籍
    kindno+=1  
#    if kindno==2: break  # 開發階段    
    