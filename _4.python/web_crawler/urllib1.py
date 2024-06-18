# Python 測試 urllib

print('------------------------------------------------------------')	#60個
print('準備工作')

import csv
import sys
import urllib
import urllib.request   #用來建立請求

def get_html_data_by_urlopen(url):
    print('取得網頁資料: ', url)
    resp = urllib.request.urlopen(url)
    return resp.read()

print('------------------------------------------------------------')	#60個
print('urllib 測試 1')

print('讀取遠端html檔或純文字檔')
url = 'http://pythonscraping.com/pages/page1.html'
#url = 'http://www.pythonscraping.com/pages/warandpeace/chapter1.txt'
html_data = get_html_data_by_urlopen(url)

print(html_data)
print('OK')

print('------------------------------------------------------------')	#60個
print('urllib 測試 2')

print('讀取遠端純文字檔2')
#encoding:Big5
#Perl的基本語法
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm

print('讀取遠端html檔1')
url = 'http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm'

html_data = get_html_data_by_urlopen(url)
html_data = html_data.decode('Big5')      #將bytes轉成str
print(html_data)
print('OK')

print('資料寫出到本地檔案')
filename = 'C:/_git/vcs/_1.data/______test_files2/perl.html'
fd = open(filename, "w")
fd.write(html_data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)
print('OK')

print('------------------------------------------------------------')	#60個
print('urllib 測試 3')

print("抓取網頁資料, 並存檔")
data={}
data['word']='明仁天皇'
 
url_values = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
url = url + url_values
 
html_data = get_html_data_by_urlopen(url)

#html_data = html_data.decode('UTF-8')
print(html_data)
print('OK')

print('------------------------------------------------------------')	#60個
print('urllib 測試 4')

print('資料寫出到本地檔案')
filename = 'C:/_git/vcs/_1.data/______test_files2/b2.html'
fd = open(filename, "wb")
fd.write(html_data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)
print('OK')


print('------------------------------------------------------------')	#60個
print('urllib 測試 5')


print('抓取網頁資料 1')
url = 'http://pythonscraping.com/pages/page1.html'

html_data = get_html_data_by_urlopen(url)

print(html_data, 'utf-8')
print('OK')


print('------------------------------------------------------------')	#60個
print('urllib 測試 6')


print('抓取網頁資料 2')
#encoding:UTF-8

#百度
#http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm
url = "http://www.baidu.com"

html_data = get_html_data_by_urlopen(url)

print(html_data)

print('資料寫出到本地檔案')
filename = 'C:/_git/vcs/_1.data/______test_files2/bbb.html'
fd = open(filename, "wb")
fd.write(html_data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)
print('OK')

print('------------------------------------------------------------')	#60個
print('urllib 測試 7')

print('讀取遠端純文字檔3')
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
url = url + url_values

html_data = get_html_data_by_urlopen(url)
html_data = html_data.decode('UTF-8')
print(html_data)
print('OK')

print('------------------------------------------------------------')	#60個
print('urllib 測試 8')

print('抓取網頁資料 4')

url = 'https://www.cnblogs.com/angelyan/'
result = urllib.parse.urlparse(url = url, scheme = 'http', allow_fragments = True)
print(result)
print(result.scheme)
print('OK')

print('------------------------------------------------------------')	#60個
print('urllib 測試 9')

print('抓取網頁資料 5')
url = 'https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&filter_uid=none&listKeyword=&pageNum=2&pageSize=18&view_mode=listView&subSite=main&l=ch&tagUid='
uc = urllib.parse.urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
    print(cmd)

print('抓取網頁資料 OK')

print('------------------------------------------------------------')	#60個
print('urllib 測試 10')

url = "http://ind.ntou.edu.tw/~dada/cgi/Perlsynx.htm"
resp = urllib.request.urlopen(url)

print("type : ")
print(type(resp))
print("info : ")
print(resp.info())

print("geturl : ")
print(resp.geturl())
print("getcode : ")
print(resp.getcode())
print("getheaders : ")
print(resp.getheaders())
print("length : ")
print(resp.length)
print("version : ")
print(resp.version)

data = resp.read()
#data = data.decode('UTF-8')
#print(data)
print('資料寫出到本地檔案')
filename = 'C:/_git/vcs/_1.data/______test_files2/tmp.html'
fd = open(filename, "wb")
fd.write(data)
fd.close()
print('抓取網頁資料 並存檔成 : ' + filename)

print('------------------------------------------------------------')	#60個
print('urllib 測試 11')

import ssl
import requests
from urllib.request import urlopen
import urllib.request   #用來建立請求
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()
url = 'https://movies.yahoo.com.tw/chart.html'
html_data = get_html_data_by_urlopen(url)
html_data = html_data.decode('utf-8')
print(html_data)
soup = BeautifulSoup(html_data, 'html.parser')
print(soup.prettify())

print('------------------------------------------------------------')	#60個
print('urllib 測試 12')

'''
#新北市公共自行車即時資訊

print('讀取遠端zip檔')

# 公開資料檔案
url ='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
filename = 'ntpc_bicycle.zip'   #壓縮檔案名稱
file_dir = './'     #解壓縮目錄

urllib.request.urlretrieve(url, filename) #下載壓縮檔
f = zipfile.ZipFile(filename) #開啟壓縮檔
for fileName in f.namelist(): #壓縮檔案列表檔名
    f.extract(fileName, file_dir) #擷取壓縮檔案
    print(fileName) #印出解壓縮檔案名稱
f.close() #關檔

f = open(fileName, 'r',encoding = 'utf8') #開啟CSV檔案，，唯讀utf-8解碼
plots = csv.reader(f, delimiter=',') #讀取CSV檔案間隔逗號，設定給plots串列物件
for row in plots: #印出UBIKE資料
    print('%5s' %row[0], '%15s' %row[1], '%5s' %row[3], '%5s' %row[12])
f.close()

print('作業完成')
'''

'''
row[0]	sno：站點代號
row[1]	sna：場站名稱(中文)
row[2]	tot：場站總停車格
row[3]	sbi：場站目前車輛數量
row[4]	sarea：場站區域(中文)
row[5]	mday：資料更新時間
row[6]	lat：緯度
row[7]	lng：經度
row[8]	ar：地址(中文)
row[9]	sareaen：場站區域(英文)
row[10]	snaen：場站名稱(英文)
row[11]	aren：地址(英文)
row[12]	bemp：空位數量
row[13]	act：全站禁用狀態
'''

print('------------------------------------------------------------')	#60個
print('urllib 測試 13')


#全國環境輻射偵測即時資訊

print('讀取遠端zip檔')

# 公開資料檔案
url ='https://www.aec.gov.tw/dataopen/index.php?id=2'
filename = 'data.csv'   #壓縮檔案名稱

urllib.request.urlretrieve(url, filename) #下載csv檔

with open(filename, 'r', encoding = 'big5') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        print(row[0]+" "+row[2]+" "+row[3])

'''
row[0]	監測站
row[1]	監測站(英文)
row[2]	監測值(微西弗/時)
row[3]	時間
row[4]	GPS經度
row[5]	GPS緯度
'''

print('------------------------------------------------------------')	#60個
print('urllib 測試 14')

print('讀取遠端圖檔')

url ='https://upload.wikimedia.org/wikipedia/commons/4/4c/SMS_Bussard_Sydney_1890s_Flickr_3229538689_b69ae42426_o.jpg'

filename = url.split('/')[-1] #圖片檔名

urllib.request.urlretrieve(url, filename) #下載圖檔

print('------------------------------------------------------------')	#60個
print('urllib 測試 15')

import urllib.request

url = 'https://upload.wikimedia.org/wikipedia/commons/6/6d/Le_Serment_du_Jeu_de_paume.jpg'
filename = '網球場宣言.jpg'

print(url)
urllib.request.urlretrieve(url, filename = filename)
#需指明下載後的檔名, 否則不知道存到哪?

print('------------------------------------------------------------')	#60個
print('urllib 測試 15')


import json
import urllib.parse
import requests

url = "https://udn.com/api/more?page=2&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"

''' many
html = requests.get(url).text
data = json.loads(html)
titles = data['lists']
for title in titles:
    print(title['title'])
    print(urllib.parse.urljoin("https://udn.com", title['titleLink']))
'''


print('------------------------------------------------------------')	#60個
print('urllib 測試 16')


import json, time
import urllib.parse
import requests

url_pattern = "https://udn.com/api/more?page={}&id=&channelId=1&cate_id=0&type=breaknews&totalRecNo=6561"
alldata = list()
for page in range(1, 11):
    url = url_pattern.format(page)
    print(url)
    html = requests.get(url).text
    data = json.loads(html)
    titles = data['lists']
    for title in titles:
        item = dict()
        #print(title['title'])  many
        item['title'] = title['title']
        item['url'] = urllib.parse.urljoin("https://udn.com", title['titleLink'])
        alldata.append(item)
    time.sleep(3)
''' many
with open("allnews.json", "w") as fp:
    json.dump(alldata, fp)
'''
print("下載完畢！")



print('------------------------------------------------------------')	#60個
print('urllib 測試 17')

#行政院農業委員會資料開放平台
url = 'https://data.coa.gov.tw/Service/OpenData/FromM/FarmTransData.aspx'

with urllib.request.urlopen(url) as res:
    data = json.loads(res.read().decode())

print(data)
print()
print(data[0])

filename = 'C:/_git/vcs/_1.data/______test_files2/products.csv'
print('將資料寫出到csv檔, 檔案 : ', filename)

with open(filename, 'w', encoding = 'big5', newline = '\n') as fp:
    writer = csv.writer(fp)
    writer.writerow(('作物名稱','平均價','交易量'))
    for item in data:
        writer.writerow((item['作物名稱'],item['平均價'],item['交易量']))

print('------------------------------------------------------------')	#60個
print('urllib 測試 18')





print('urllib 測試 作業完成')



