# ch5_13_9.py
import requests, bs4

url = 'ch5_2_3.html'
htmlFile = open(url, encoding='utf-8')              
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

myriver = []                        # 河川
tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')
river = tables[0].find('td')
print(river.text)
previous_rows = river.parent.find_next_siblings()
print(previous_rows)

river = tables[2].find('td')
print(river.text)
next_rows = river.parent.find_previous_siblings()
print(next_rows)









    
          


                     



    
    

    





















