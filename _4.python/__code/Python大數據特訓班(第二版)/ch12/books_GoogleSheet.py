def showkind(url,kind):
    html = requests.get(url,headers=headers).text
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
    html = requests.get(url,headers=headers).text 
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
        # 將資料加入 list1 串列中
        listdata=[kind,title,imgurl,author,publish,date,onsale,content]
        list1.append(listdata)
        n+=1
        print("n=",n)

def twobyte(kindno):
    if kindno<10:
        kindnostr="0"+str(kindno)
    else:
        kindnostr=str(kindno) 
    return kindnostr

def auth_gss_client(path, scopes): #建立憑證
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path,scopes)
    return gspread.authorize(credentials)  

#主程式
import requests
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep

auth_json_path = 'PythonUpload.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']
gss_client = auth_gss_client(auth_json_path, gss_scopes) #連線

spreadsheet_key = '您自己的key' 
sheet = gss_client.open_by_key(spreadsheet_key).sheet1 #開啟工作表
sheet.clear() # 清除工作表內容

list1=[]    
kindno=1  # 要下載的分類，預設為第 1分類：文學小說
homeurl = 'http://www.books.com.tw/web/books_nbtopm_01/?o=5&v=1'
mode="?o=5&v=1" #顯示模式：直式  排序依：暢銷度
url="https://www.books.com.tw/web/books_nbtopm_" 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
html = requests.get(homeurl,headers=headers).text
soup = BeautifulSoup(html,'html.parser') 
#中文書新書分類，取得分類資訊
res = soup.find('div',{'class':'mod_b type02_l001-1 clearfix'})
hrefs=res.select("a")
kindno=int(input("請輸入要下載的分類："))
if 0 < kindno <= len(hrefs):
    kind=hrefs[kindno-1].text #分類名稱
    print("下載的分類編號：{}   分類名稱：{}" .format(kindno,kind))
    # 下載指定的分類
    kindurl=url + twobyte(kindno) + mode # 分類網址  
    showkind(kindurl,kind) # 顯示該分類所有書籍    
    # 儲存 Google 試算表
    print("資料寫入雲端 Google 試算表中，請等侯幾分鐘!")
    listtitle=["分類","書名","圖片網址","作者","出版社","出版日期","優惠價","內容"]
    sheet.append_row(listtitle)  # 標題
    for item1 in list1: #資料
        sheet.append_row(item1)
        sleep(1) # 必須加上適當的 delay      
else:
    print("分類不存在!") 
print("資料儲存完畢!")    