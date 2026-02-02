# ch10_3.py
import requests, bs4

url = 'https://udn.com/news/cate/2/7225'            # 全球頭條新聞
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')  # 取得HTML
items = objSoup.find('div', 'area')
items = items.find_all('div', 'ms-info')
for item in items:
    txt = item.h1.text                
    print(txt)
    print()


    
          


                     



    
    

    





















