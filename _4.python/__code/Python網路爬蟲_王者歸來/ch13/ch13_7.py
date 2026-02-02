# ch13_7.py
import requests, bs4

url = 'https://www.moneydj.com/funddj/ya/YP401000.djhtm'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')      # 取得物件
fundtable = objSoup.find('table', id='oMainTable')
# 抓標題
objhead = fundtable.find('tr', id='oScrollMenu')
heads = objhead.find_all('th')
for head in heads:                                      # 輸出基金表格標題
    print(head.text.strip(), ' ', end='')
print()
# 抓基金表格資料
objtable = fundtable.find('tbody')
tables = objtable.find_all('tr')
for table in tables:                                    # 輸出各基金績效
    rowtext = table.text.strip()
    txt = rowtext.split('\n')                           # 將字串轉成串列
    print(txt)
    
    
    














