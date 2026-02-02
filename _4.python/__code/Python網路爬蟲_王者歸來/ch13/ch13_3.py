# ch13_3.py
import requests, bs4

url = 'http://www.taiwanrate.com/'
htmlfile = requests.get(url)
htmlfile.encoding = 'utf-8'                                 # 轉成utf-8
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
ratetable = objSoup.find_all('table')
# 列印表格欄位名稱
lefttop = ratetable[4].find('tr').find('tr').find('td')     # 第4個表格
print(lefttop.text,end=' ')                                 # 左上角內容                  
ratehead = ratetable[4].find('tr').find_all('a', 'bodytablehead')
for head in ratehead:
    print(head.text, end=' ')                               # 列出其它欄位名稱
# 以上是列印表格欄位名稱
print()
# 以下是列印各銀行利率, 先找出第一個class='bodytabletr1'
ratetd = ratetable[4].find('tr', 'bodytabletr1')            
print(ratetd.text)                                          # 列出第一家銀行
while ratetd.find_next_sibling('tr'):
    ratetd = ratetd.find_next_sibling('tr')
    print(ratetd.text)                                      # 列出其它家銀行

    











