# ch10_5.py
import requests, bs4

url = 'https://www.chinatimes.com/world/?chdtv'
newshtml = requests.get(url)                        # 中國時報新聞
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')  # 取得HTML
itemobj = objSoup.find('section', 'hot-news')
itemobj = itemobj.find('ol', 'vertical-list')
items = itemobj.find_all('li')
for item in items:
    txt = item.h4.text               
    print(txt)
    


    
          


                     



    
    

    





















