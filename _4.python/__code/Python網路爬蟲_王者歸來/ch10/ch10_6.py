# ch10_6.py
import requests, bs4

url = 'https://www.chinatimes.com/newspapers/2602?chdtv'
newshtml = requests.get(url)                        # 工商時報熱門新聞
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')  # 取得HTML
itemobj = objSoup.find('section', 'hot-news')
print(itemobj.h4.text,'\n')                         # 熱門新聞標題
itemobj = itemobj.find('ol', 'vertical-list')
items = itemobj.find_all('li')
for item in items:
    txt = item.h4.text               
    print(txt)
    


    
          


                     



    
    

    





















