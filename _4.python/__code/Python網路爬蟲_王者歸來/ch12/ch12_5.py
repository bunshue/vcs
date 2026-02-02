# ch12_5.py
import requests, bs4

url = 'https://www.google.com/search?q=TPE:1101'
headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101\
            Safari/537.36', }
newshtml = requests.get(url, headers=headers)           # 台灣水泥
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')      # 取得HTML
gcards = objSoup.find_all('g-card-section')
company = gcards[1].div
company = company.find('div', 'oPhL2e')                 # 取得公司名稱
print(company.text)
spans = gcards[1].find_all('div', recursive=False)[1]   # False只搜尋第一層
info = spans.find_all('span',recursive=False)           # False只搜尋第一層
price = info[0].text
change = info[1].text
print('收盤價 = ', price)
print('帳跌   = ', change)
for table in gcards[3].find_all('table'):
    for row in table.find_all('tr')[:3]:
        key = row.find_all('td')[0].text
        value = row.find_all('td')[1].text
        print(key, '=',  value)




    


    
          


                     



    
    

    





















