# ch5_13_6.py
import requests, bs4

url = 'ch5_2_1.html'
htmlFile = open(url, encoding='utf-8')              
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
titleobj = objSoup.find('h2')                       # h2標題
title = titleobj.find_next_siblings('h2')           # 下一系列節點
print('find_next_siblings     = ', title)

titleobj = objSoup.find_all('h2')
title = titleobj[2].find_previous_siblings('h2')    # 前一系列節點
print('find_previous_siblings = ', title)
    


    
          


                     



    
    

    





















