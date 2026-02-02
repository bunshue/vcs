# ch12_6.py
import requests, bs4

url = 'https://tw.stock.yahoo.com/q/q?s=2330'

newshtml = requests.get(url)                        # 台積電
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')  # 取得HTML

tables = objSoup.find_all('table')
table1 = tables[1].find_all('th')                   # 表頭
for t_head in table1:
    print(t_head.text)
table2 = tables[2].find_all('td')                   # 表格值
print("------------------------------")
for t_info in table2:
    print(t_info.text)







    


    
          


                     



    
    

    





















