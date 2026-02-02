# ch5_13_8.py
import requests, bs4

url = 'ch5_2_3.html'
htmlFile = open(url, encoding='utf-8')              
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

myriver = []                        # 河川
tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')
river = tables[1].find('td')
print(river.text)

previous_row = river.parent.find_previous_sibling()
print(previous_row)
next_row = river.parent.find_next_sibling()
print(next_row)









    
          


                     



    
    

    





















