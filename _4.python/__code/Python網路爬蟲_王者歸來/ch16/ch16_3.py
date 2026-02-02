# ch16_3.py
import requests, bs4

url = 'https://www.biqukan.com/50_50096/'
htmlfile = requests.get(url)
htmlfile.encoding = 'gbk'
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')

storys = objSoup.find('div', 'listmain')
story = storys.find_all('dt')               # 取書籍標題
print(story[1].text)                        # 列出書籍標題
print()
sto = storys.find_all('dd')                 # 取全部章節標題
sto = sto[12:]                              # 切片捨去前12回標題
for ch in sto:                              # 列出三國演義正文卷
    print(ch.text)







