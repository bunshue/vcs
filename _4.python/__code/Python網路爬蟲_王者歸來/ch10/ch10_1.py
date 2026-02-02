# ch10_1.py
import requests, bs4

url = 'https://tw.appledaily.com/hot/daily'      
applehtml = requests.get(url)
objSoup = bs4.BeautifulSoup(applehtml.text, 'lxml')         # 取得HTML

items = objSoup.find('ul', 'all').find_all('li')
for item in items:
    if item.find('div', 'aht_title_num atopred'):           # 前10條是紅色
        num = item.find('div', 'aht_title_num atopred').text
    else:
        num = item.find('div', 'aht_title_num').text        # 其它則黑色色
    txt = item.find('div', 'aht_title').text                
    print("新聞編號 : ",num)
    print(txt)


    
          


                     



    
    

    





















