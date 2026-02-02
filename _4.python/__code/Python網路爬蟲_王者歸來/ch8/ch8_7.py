# ch8_7.py
import requests, bs4
import json

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
        publish_time = p.find('div', 'date').text
        articles.append({'title':title,                 # 文章標題
                         'publish_time':publish_time,   # 發表時間
                         'author':author,               # 文章作者
                         'href':href,                   # 文章超連結
                         'push_num':push_num,           # 推文數
                        })

fn = 'out8_7.json'
with open(fn, 'w', encoding='utf-8') as fnObj:
    json.dump(articles, fnObj, ensure_ascii= False, indent=2)


    

















