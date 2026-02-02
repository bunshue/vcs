# ch16_7.py
import requests, bs4

story = ''                                              # 小說內文
url = 'https://www.biqukan.com/50_50096/18520412.html'  # 第一回的網址
htmlfile = requests.get(url)
htmlfile.encoding = 'gbk'
objSoup = bs4.BeautifulSoup(htmlfile.text, 'lxml')
title = objSoup.find('h1')                              # 第一回標題
story = story + title.text + '\n'                       # 標題加入內文
contents = objSoup.find('div', id='content')            # 內文位置
for content in contents: 
    if type(content) == bs4.element.NavigableString:    # 確定資料格式
        txt = content.strip()
        if type(txt) == str and txt != '':              # 確定是字串和不是空字串
            txt = content.strip()
            txt = txt.replace('&1t;/p>', '')            # 將末端字元刪除
            story = story + txt + '\n\n'                # 加入小說內文

fn = title.text
with open(fn, 'w', encoding='utf-8') as obj:
    obj.write(story)
print('小說 %s 儲存成功' % title.text)









