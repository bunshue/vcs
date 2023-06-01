# Python 測試 urllib

print('----------------------------------------------------------------------')	#70個
print('準備工作')


import urllib
import urllib.request   #用來建立請求
import zipfile
import csv
from bs4 import BeautifulSoup

import requests
from urllib.parse import urlparse
from urllib.request import urlopen

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

print('----------------------------------------------------------------------')	#70個
print('urllib 測試 1')

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


print('作業完成')


'''
row[0]	監測站
row[1]	監測站(英文)
row[2]	監測值(微西弗/時)
row[3]	時間
row[4]	GPS經度
row[5]	GPS緯度
'''



print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 4')
from urllib.request import urlopen
from urllib.error import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        soup = BeautifulSoup(html, "html.parser")
        title = soup.body.h1
    except AttributeError as e:
        return None
    return title

url = 'http://www.pythonscraping.com/exercises/exercise1.html'
title = getTitle(url)
if title == None:
    print("找不到網頁標題")
else:
    print("取得網頁標題:")
    print(title)



print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 10')

#用 BeautifulSoup 分析網頁資料

url = 'https://www.ptt.cc/bbs/C_Chat/index.html'

domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
all_links = soup.find_all(['a','img'])

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'):
                print(t)
            else:
                print(domain+t)




print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 11')

domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。
all_links = soup.find_all(['a','img'])

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'): full_path = t
            else:                    full_path = domain+t
            print(full_path)
            image_dir = url.split('/')[-1]
            if not os.path.exists(image_dir): os.mkdir(image_dir)
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext: filename = filename + '.jpg'
            else:            filename = filename + '.png'
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir,filename),'wb')
            fp.write(image.read())
            fp.close()



print('----------------------------------------------------------------------')	#70個
print('BeautifulSoup 測試 12')

post_html = '''
</body>
</html>
'''

domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html_data = get_html_data1(url)
soup = BeautifulSoup(html_data.text, 'html.parser')
#print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

pre_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>網頁搜集來的資料</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <style>
  .carousel-inner > .item > img,
  .carousel-inner > .item > a > img {
      border: 5px solid white;
      width: 50%;
      box-shadow: 10px 10px 5px #888888;
      margin: auto;
  }
  </style>

</head>
<body>
<center><h3>以下是從網頁搜集來的圖片跑馬燈</h3></center>
"""

all_links = soup.find_all(['a','img'])

carousel_part1 = ""
carousel_part2 = ""
picno = 0

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'): full_path = t
            else:                    full_path = domain+t
            print(full_path)
            image_dir = url.split('/')[-1]
            if not os.path.exists(image_dir): os.mkdir(image_dir)
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext: filename = filename + '.jpg'
            else:            filename = filename + '.png'
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir,filename),'wb')
            fp.write(image.read())
            fp.close()

            if picno==0:
                carousel_part1 += "<li data-target='#myC' data-slide-to='{}' class='active'></li>".format(picno)
                carousel_part2 += """
                    <div class='item active'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(filename, filename)

            else:
                carousel_part1 += "<li data-target='#myC' data-slide-to='{}'></li>".format(picno)
                carousel_part2 += """
                    <div class='item'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(filename, filename)
            picno += 1

            html_body = """
            <div id='myC' class='carousel slide' data-ride='carousel'>
                <ol class='carousel-indicators'>
                {}
                </ol>
                <div class='carousel-inner' role='listbox'>
                {}
                </div>
                <a class="left carousel-control" href="#myC" role="button" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                    <span class="sr-only">前一張</span>
                </a>
                <a class="right carousel-control" href="#myC" role="button" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                    <span class="sr-only">後一張</span>
                </a>
            </div>
            """.format(carousel_part1, carousel_part2)

'''
fp = open('index.html', 'w')
fp.write(pre_html+html_body+post_html)
fp.close()            
'''


import urllib.parse
from bs4 import BeautifulSoup
import requests

html_data = requests.get('https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo#')
soup = BeautifulSoup(html_data.text, 'html.parser')
captcha_image = soup.find('img', id='pickimg')['src'] 
csrf_token = soup.find_all('input', type='hidden') 
image_url = urllib.parse.urljoin('https://www.mvdis.gov.tw/', captcha_image)
print(image_url)
captcha = input("請輸入驗證碼：")
headers = {
    "user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
    "Cookie":'DWRSESSIONID=qNiI6i9UPxr4DV2G7PrFV8pkahn; _ga=GA1.3.1352658715.1598224971; BSESSIONID1=D106D274717EDF2C4EFDD9D698E61581.tsb22; _gid=GA1.3.615895194.1598974412; JSESSIONID1=B71AEB3133E436EA9619A6F6F3CDA2EA.tsp12'
}
data = {
    'method': 'qryPickNo',
    'selDeptCode': "2",
    'selStationCode': "30",
    'selWindowNo': "01",
    'selCarType': "M",
    'selEnergyType': "C",
    'selPlateType': "F",
    'plateVer': "2",
    'validateStr': str(captcha),
    'queryType': 0,
    'queryNo': '*',
    'CSRFToken': str(csrf_token[2]['value']),
}

html = requests.post('https://www.mvdis.gov.tw/m3-emv-plate/webpickno/queryPickNo', data = data, headers = headers).text
soup = BeautifulSoup(html, 'html.parser')
plate_numbers = soup.find_all('a','number')
print(plate_numbers)

for plate_number in plate_numbers:
    print('aaaaaaaaaaaaaa')
    print(plate_number.text)

    
print('urllib 測試 作業完成')

