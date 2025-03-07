print("------------------------------------------------------------")  # 60個

'''
# books.py
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

    
    
# books_GoogleSheet.py
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
'''



print("------------------------------------------------------------")  # 60個

# compare1.py


# 1111data.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

df = []
baseurl = 'https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks=電腦&ss=s&ps=100&page='  #電腦

#取得總頁數
html = requests.get(baseurl + '1')
soup = BeautifulSoup(html.text, 'lxml')
tem = soup.find('span', class_='Nexup').text  
page = int(tem.replace('1 / ', ''))
if page > 15:  #最多取15頁資料
    page = 15
#逐頁讀取資料
for i in range(page):
    url = baseurl + str(i+1)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    job = soup.select(".jbInfoin")  #取class=jbInfoin內容
    for j in range(len(job)):
        work = job[j].h3.a.text  #職務名稱
        work = work.replace('【誠徵】', '').replace('【急徵】', '').replace('誠徵', '')
        site = 'https:' + job[j].h3.a.get('href')  #工作網址
        company = job[j].h4.a.text  #公司名稱
        companysort = job[j].find('div', class_='csort').a.text  #公司類別
        area = job[j].find('span', class_='location').a.text  #工作地點
        tem = job[j].find('div', class_='needs').text
        temlist = tem.split('|')
        salary = temlist[0]  #薪資
        experiment = temlist[1]  #工作經驗
        school = temlist[2]  #學歷
        tem = job[j].find('div', class_='jbInfoTxt')
        temlist = tem.find_all('p')
        content = ''  #工作內容
        for k in range(len(temlist)):
            content = content + temlist[k].text

        dfmono = pd.DataFrame([{'職務名稱':work,
                             '工作網址': site,
                             '公司名稱': company,
                             '公司類別': companysort,
                             '工作地點':area,
                             '薪資':salary,
                             '工作經驗':experiment,
                             '學歷':school,
                             '工作內容':content }],
                             )
        df.append(dfmono)
    print('處理第 ' + str(i+1) + ' 頁完畢！')
df = pd.concat(df, ignore_index=True)
df.to_excel('tmp_1111data.xlsx', index=0)  #存為excel檔

print("------------------------------------------------------------")  # 60個

# compare2.py

# 1111data.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

df = []
baseurl = 'https://www.1111.com.tw/job-bank/job-index.asp?si=1&ks=電腦&ss=s&ps=100&page='  #電腦

#取得總頁數
html = requests.get(baseurl + '1')
soup = BeautifulSoup(html.text, 'lxml')
tem = soup.find('select', class_='custom-select').text
page = int(tem.replace('1 / ', ''))
if page > 15:  #最多取15頁資料
    page = 15
#逐頁讀取資料
for i in range(page):
    url = baseurl + str(i+1)
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    job = soup.select(".it-md")  #取class=jbInfoin內容
    for j in range(len(job)):
        work = job[j].find('div', class_='position0').a.text  #職務名稱
        work = work.replace('【誠徵】', '').replace('【急徵】', '').replace('誠徵', '')
        site = 'https://www.1111.com.tw' + job[j].find('div', class_='position0').a.get('href')  #工作網址
        company = job[j].find('div', class_='d-none d-md-flex jb-organ').a.text  #公司名稱
        companysort = job[j].find('span', class_='d-none d-md-block').text.replace('｜', '')  #公司類別
        tem = job[j].find('div', class_='text-truncate needs').select('span')        
        area = tem[0].text  #工作地點
        salary = tem[1].text  #薪資
        experiment = tem[2].text  #工作經驗
        school = tem[3].text  #學歷
        tem = job[j].find('div', class_='col-12 jbInfoTxt UnExtension').select('p')
        content = ''  #工作內容
        for k in range(len(tem)):
            content = content + tem[k].text

        dfmono = pd.DataFrame([{'職務名稱':work,
                              '工作網址': site,
                              '公司名稱': company,
                              '公司類別': companysort,
                              '工作地點':area,
                              '薪資':salary,
                              '工作經驗':experiment,
                              '學歷':school,
                              '工作內容':content }],
                              )
        df.append(dfmono)
    print('處理第 ' + str(i+1) + ' 頁完畢！')
df = pd.concat(df, ignore_index=True)
df.to_excel('tmp_1111data.xlsx', index=0)  #存為excel檔

print("------------------------------------------------------------")  # 60個
