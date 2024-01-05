from bs4 import BeautifulSoup
import requests

addr = 'https://tw.stock.yahoo.com/d/i/fgbuy_tse.html'

#取得網頁原始程式碼
res = requests.get(addr).text 
#以html.parser解析程式解析程式碼
bs = BeautifulSoup(res, 'html.parser')
#以<tr>並配合屬性取得表格中每列內容
rows = bs.find_all('tr', {'bgcolor':'#FFFFFF'})

#印出要查詢資料各欄位名稱
print('名 次 股票代號/名稱  成交價  漲　跌  買超張數  外資持股張數  外資持股比率')

#讀取每列的內容，找出<td>
for row in rows:
    if row.find('td'):
        #屬性stripped_strings去餘每欄中字串的空白符號
        cols =[item for item in row.stripped_strings]
        #讀取List物件的元素
        for item in range(0,len(cols)):
            print(cols[item], end = ' ')
        print() #換行
