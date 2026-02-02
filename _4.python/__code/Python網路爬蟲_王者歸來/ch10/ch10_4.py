# ch10_4.py
import requests, bs4

url = 'https://money.udn.com/money/cate/5591'       # 經濟日報新聞
newshtml = requests.get(url)
objSoup = bs4.BeautifulSoup(newshtml.text, 'lxml')  # 取得HTML
itemobj = objSoup.find('div', 'category_box_list author')
items = itemobj.find_all('dt', 'more_5612')
for item in items:
    txt = item.a.text.strip()                
    print(txt)
    


    
          


                     



    
    

    





















