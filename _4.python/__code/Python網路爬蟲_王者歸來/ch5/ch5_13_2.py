# ch5_13_2.py
import requests, bs4

url = 'ch5_2_2.html'
htmlFile = open(url, encoding='utf-8')              
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')

mycity = []
cityobj = objSoup.find('dl')          
cities = cityobj.find_all('dt')
for city in cities:
    mycity.append(city.text)                # mycity串列

mycountry = []    
countryobj = objSoup.find('dl')
countries = countryobj.find_all('dd')
for country in countries:
    mycountry.append(country.text)          # mycountry串列

print("國家 = ", mycountry)
print("首都 = ", mycity)
data = dict(zip(mycountry, mycity))
print(data)                                 # 字典顯示結果







    
          


                     



    
    

    





















