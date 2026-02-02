# ch10_2.py
import requests, bs4

url = 'https://udn.com/news/cate/2/7225'            # 全球頭條新聞
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')  # 取得HTML
items = objSoup.find('div', 'area')                 
print(type(items))
print(items)




    
          


                     



    
    

    





















