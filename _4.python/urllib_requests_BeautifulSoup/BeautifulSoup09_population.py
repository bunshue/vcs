import requests
from bs4 import BeautifulSoup

url = "http://www.daxi-hro.tycg.gov.tw/home.jsp?id=25&parentpath=0,21,22"
content = requests.get(url).text
soup = BeautifulSoup(content, "html.parser")

#人口統計
person_data = list()    #人口統計資料
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
length = len(person_data)
year1 = []
person1 = []
person2 = []
person3 = []
for i in range(0, length): 
    year1.append(person_data[i][0])
    person1.append(person_data[i][1])
    person2.append(person_data[i][2])
    person3.append(person_data[i][3])

#戶數統計
house_data = list()     #戶數統計資料
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
length = len(house_data)
year2 = []
house = []
for i in range(0, length): 
    year2.append(house_data[i][0])
    house.append(house_data[i][1])

'''
print('person_data')
print(person_data)
print('house_data')
print(house_data)
print('year1')
print(year1)
print('person1')
print(person1)
print('person2')
print(person2)
print('person3')
print(person3)
print('year2')
print(year2)
print('house')
print(house)
'''

print('----------------------------------------------------------------------')	#70個
# 開始畫圖

selected_font = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'plot 集合 1 函數曲線', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(211)

plt.plot(year1, person1, linewidth = 2.0, label="男")
plt.plot(year1, person2, linewidth = 2.0, label="女")
plt.title("桃園市大溪區歷年人口數")
plt.xlabel("年度")
plt.ylabel("人口數")
plt.legend()

#第二張圖
plt.subplot(212)

plt.plot(year2, house, linewidth = 2.0)
plt.title("桃園市大溪區歷年戶數")
plt.xlabel("年度")
plt.ylabel("戶數")

plt.show()


