# ch15_2.py
import requests, bs4

url = 'http://www.xzw.com/fortune/'
htmlfile = requests.get(url)
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')          # 取得物件
constellation = objSoup.find('div', id='list')
print(constellation.find('h1').text)                        # 標題
cons = constellation.find('div', 'alb').find_all('div')
for con in cons:
    c = con.find('dd').find('strong')                       # 星座
    print(c.text)
    dateofbirth = con.find('dd').find('small')              # 出生日期
    print(dateofbirth.text)
    forturn = con.find('dd').find('span')                   # 整體運勢
    print(forturn.text)
    txt = con.find('dd').find('p')                          # 簡略說明
    print(txt.text)




