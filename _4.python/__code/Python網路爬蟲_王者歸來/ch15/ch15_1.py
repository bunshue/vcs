# ch15_1.py
import requests, bs4

url = 'http://www.xzw.com/fortune/'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
constellation = objSoup.find('div', id='list')
print(constellation.find('h1').text)                        # 標題
con = constellation.find('dd').find('strong')               # 星座
print(con.text)
dateofbirth = constellation.find('dd').find('small')        # 出生日期
print(dateofbirth.text)
fortune = constellation.find('dd').find('span')             # 整體運勢
print(fortune.text)
txt = constellation.find('dd').find('p')                    # 簡略說明
print(txt.text)




