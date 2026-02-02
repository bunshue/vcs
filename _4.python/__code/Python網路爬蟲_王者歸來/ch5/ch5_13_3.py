# ch5_13_3.py
import requests, bs4

url = 'ch5_2_3.html'
htmlFile = open(url, encoding='utf-8')              
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

myriver = []                        # 河川
tableobj = objSoup.find('table').find('tbody')
tables = tableobj.find_all('tr')
for table in tables:
    river = table.find('td')
    myriver.append(river.text)

mycountry = []                      # 國家
for table in tables:
    countries = table.find_all('td')
    country = countries[1]
    mycountry.append(country.text)
    
print("國家 = ", mycountry)
print("河川 = ", myriver)
data = dict(zip(mycountry, myriver))
print(data)                         # 字典顯示結果
    








    
          


                     



    
    

    





















