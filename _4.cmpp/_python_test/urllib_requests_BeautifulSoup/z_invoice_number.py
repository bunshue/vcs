import requests

print('取得網頁資料 9')
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

url = 'http://invoice.etax.nat.gov.tw/invoice.xml'   #統一發票中獎號碼
html_data = requests.get(url)
print('1111')
#print(html_data.text)
tree = ET.fromstring(html_data.text)
print('2222')
print(tree)
print('根目錄標籤：' + tree.tag)
print('根目錄屬性：' + str(tree.attrib))
print('根目錄值：' + str(tree.text))

item = tree[0].find('item')
print('find 方法：' + item[0].text)

items = tree[0].findall('item')
print('findall 方法：' + items[0][0].text)

items = list(tree.iter(tag='item'))
print('iter 方法：' + items[0][0].text)



import requests
url = 'https://invoice.etax.nat.gov.tw/index.html'
# 取得網頁html
web = requests.get(url)    
# 設置編碼，避免中文亂碼
web.encoding='utf-8'       

from bs4 import BeautifulSoup
# 轉換成標籤樹
tree = BeautifulSoup(web.text, "html.parser")  
# 取出開獎月份
issue = tree.select(".carousel-item")[0].getText(); 
print(issue)
# 取出中獎號碼陣列
winlist = tree.select('.container-fluid')[0].select('.etw-tbiggest')  
#特別獎
nss = winlist[0].getText()  
#特獎
ns = winlist[1].getText() 
# 頭獎
n1 = [winlist[2].getText()[-8:], winlist[3].getText()[-8:], winlist[4].getText()[-8:]] 
print("特別獎:\n" + "　　"+nss + "\n")
print("特獎:\n"+"　　" + ns + "\n")
print("頭獎:")
for j in n1:
  print("　　"+j)
print("\n")


print('done')

