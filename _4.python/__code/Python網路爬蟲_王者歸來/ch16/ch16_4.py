# ch16_4.py
import requests, bs4

chapter_url = []
web_url = 'https://www.biqukan.com'
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
    ch_url = ch.a['href']                   # 取得章節標題片段網址
    chapter_url.append(web_url + ch_url)    # 將完整章節內容網址存入

for c_url in chapter_url:
    print(c_url)                            # 列出完整章節內容網址





