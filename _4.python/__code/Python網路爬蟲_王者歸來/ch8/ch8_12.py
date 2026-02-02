# ch8_12.py
import requests, bs4

ptturl = 'https://www.ptt.cc'
page = '/bbs/Gossiping/index.html'
ptthtml = requests.get(ptturl+page, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')       # 目前頁

div_page = objSoup.find('div', 'btn-group-paging')
last_page = div_page.find_all('a')[1]['href']           # 前一頁超連結

ptthtml = requests.get(ptturl+last_page, cookies={'over18':'1'})                # 前一頁
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')       # 前一頁

articles = []                                           # 本頁面文章
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        title = p.find('a').text
        author = p.find('div', 'author').text
        href = p.find('a')['href']
        push_num = p.find('div', 'nrec').text
        publish_time = p.find('div', 'date').text
        articles.append({'title':title,                 # 文章標題
                         'publish_time':publish_time,   # 發表時間
                         'author':author,               # 文章作者
                         'href':href,                   # 文章超連結
                         'push_num':push_num,           # 推文數
                        })
print('本頁的文章數量 = ', len(articles))
count = 0                                               # 文章編號計數器
for article in articles:
    count += 1
    print('文章編號 : ', count)
    print('文章標題 : ', article['title'])
    print('發表時間 : ', article['publish_time'])
    print('文章作者 : ', article['author'])
    print('文章連結 : ', article['href'])
    print('推文數量 : ', article['push_num'],'\n')
    

















