# ch8_5.py
import requests, bs4

url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
ptthtml = requests.get(url, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

articles = []                                           # 本頁面文章
pttdivs = objSoup.find_all('div', 'r-ent')
for p in pttdivs:
    if p.find('a'):
        title = p.find('a').text
        author = p.find('div', 'author').text
        href = p.find('a')['href']
        push_num = p.find('div', 'nrec').text
        if push_num.startswith('X'):                    # 表示推文被噓超過10次
            push_num = '0'
        if push_num == '爆':                            # 表示推文超過100次
            push_num = '100'
        articles.append({'title':title,                 # 文章標題
                         'author':author,               # 文章作者
                         'href':href,                   # 文章超連結
                         'push_num':push_num,           # 推文數
                        })
print('本頁的文章數量 = ', len(articles))
count = 0                                               # 文章編號計數器
pushcounts = 20                                         # 最低推文數
print('下列是推文數大於20的文章','\n')
for article in articles:
    count += 1
    if article['push_num'] != '':                       # 測試是否空的
        push_min = int(article['push_num'])             # 不是空的,直接獲得推文數
    else:
        push_min = 0                                    # 是空的,推文數是0
    if push_min > pushcounts:                           # 如果推文數大於最低推文數
        print('文章編號 : ', count)
        print('文章標題 : ', article['title'])
        print('文章作者 : ', article['author'])
        print('文章連結 : ', article['href'])
        print('推文數量 : ', article['push_num'],'\n')
    

















