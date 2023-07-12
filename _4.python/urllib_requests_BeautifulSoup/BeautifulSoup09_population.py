import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

person_data = list()
house_data = list()

url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

#人口統計
data1 = soup.find("tbody")
#print(data1)

rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if(len(cols) > 0):
        if cols[1].text != "─":
            person_data.append(((int)(cols[0].text.strip()[:-1]), (int)(cols[1].text), (int)(cols[2].text), (int)(cols[3].text)))
        else:
            print('xxxxxx1111')
    else:
        print('xxxxxx2222')

person_data.reverse()   #反相
'''
print('person_data')
print(person_data)
'''

year = []
person1 = []
person2 = []
person3 = []

length = len(person_data)
for i in range(0, length): 
    year.append(person_data[i][0])
    person1.append(person_data[i][1])
    person2.append(person_data[i][2])
    person3.append(person_data[i][3])
print('year')
print(year)
print('person1')
print(person1)
print('person2')
print(person2)
print('person3')
print(person3)

'''
plt.plot(year, person1, linewidth = 2.0)
plt.plot(year, person2, linewidth = 2.0)
#plt.title("桃園市大溪區歷年人口數")
#plt.xlabel("年度")
#plt.ylabel("人口數")
'''

#戶數統計
data1 = soup.select("table[summary^='歷年戶數統計列表排版用']")[0]
#print(data1)

rows = data1.find_all("tr")
for row in rows:
    cols = row.find_all("td")
    if(len(cols) > 0):
        if cols[1].text != "─":
            house_data.append(((int)(cols[0].text.strip()[:-1]), (int)(cols[1].text)))
        else:
            print('xxxxxx1111')
    else:
        print('xxxxxx2222')

house_data.reverse()   #反相
'''
print('house_data')
print(house_data)
'''

year = []
house = []

length = len(house_data)
for i in range(0, length): 
    year.append(house_data[i][0])
    house.append(house_data[i][1])
print('year')
print(year)
print('house')
print(house)

plt.plot(year, house, linewidth = 2.0)
#plt.title("桃園市大溪區歷年戶數")
#plt.xlabel("年度")
#plt.ylabel("戶數")

plt.show()
