import requests
from bs4 import BeautifulSoup

url = 'http://www.taiwanlottery.com.tw/'
html = requests.get(url)
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.select("#rightdown")
#print(data1)

data2 = data1[0].find('div', {'class':'contents_box02'})
#print(data2)

data3 = data2.find_all('div', {'class':'ball_tx'})
#print(data3)
#
# 威力彩號碼
print("開出順序：",end="")
for n in range(0,6):
    print(data3[n].text,end="  ") 

print("\n大小順序：",end="")    
for n in range(6,len(data3)):
    print(data3[n].text,end="  ")
     
## 第二區
red = data2.find('div', {'class':'ball_red'})        
print("\n第二區：{}".format(red.text)) 