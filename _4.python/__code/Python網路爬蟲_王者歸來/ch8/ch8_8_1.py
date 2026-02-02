# ch8_8_1.py
import requests, bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

div_page = objSoup.find('div', 'btn-group-paging')
print(type(div_page))
print(div_page)







    

















