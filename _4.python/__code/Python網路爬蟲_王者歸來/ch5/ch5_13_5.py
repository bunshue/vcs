# ch5_13_5.py
import requests, bs4

url = 'ch5_2_3.html'
htmlFile = open(url, encoding='utf-8')              
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

myriver = []                                    # 河川
mystate = []                                    # 洲名
tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')

for table in tables:
    countries = table.find_all('td')
    country = countries[1]                      # 國家節點
    river = country.find_previous_sibling('td') # 前一個節點
    myriver.append(river.text)
    state = country.find_next_sibling('td')     # 下一個節點
    mystate.append(state.text)
    
print("洲名 = ", mystate)
print("河川 = ", myriver)
data = dict(zip(mystate, myriver))
print(data)                                     # 字典顯示結果
    








    
          


                     



    
    

    





















