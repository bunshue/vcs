# Python 測試 BeautifulSoup Yahoo電影 台北票房榜

import sys
import requests
from bs4 import BeautifulSoup

import ssl
from urllib import request, parse

#urlopen https時需要驗證一次SSL證書，
#當網站目標使用自簽名的證書時就會跳出錯誤
#使用SSL module把證書驗證改成不需要驗證
#context = ssl._create_unverified_context()

url = 'https://movies.yahoo.com.tw/chart.html'
req_obj = request.Request(url)

#with request.urlopen(req_obj,context=context) as res_obj:
with request.urlopen(req_obj) as res_obj:
    html_data = res_obj.read()
    html_data = html_data.decode('utf-8')
    print(html_data)
    soup = BeautifulSoup(html_data, 'html.parser')
    print(soup.prettify())
    
    rows = soup.find_all('div', class_ = 'tr')

    colname = list(rows.pop(0).stripped_strings)
    contents = []
    for row in rows:
        thisweek_rank = row.find_next('div' , attrs={'class' : 'td'})
        updown = thisweek_rank.find_next('div')
        lastweek_rank = updown.find_next('div')

        if thisweek_rank.string == str(1):
            movie_title = lastweek_rank.find_next('h2')
        else:
            movie_title = lastweek_rank.find_next('div' , attrs={'class' : 'rank_txt'})

        release_date = movie_title.find_next('div' , attrs={'class' : 'td'})
        trailer = release_date.find_next('div' , attrs={'class' : 'td'})

        if trailer.find('a') is None:
            trailer_address = ''
        else:
            trailer_address = trailer.find('a')['href']

        starts = row.find('h6' , attrs={'class' : 'count'})
        lastweek_rank = lastweek_rank.string if lastweek_rank.string else ''

        c = [thisweek_rank.string , lastweek_rank , movie_title.string , release_date.string , trailer_address , starts.string]
        print('加入: ', c)
        contents.append(c)

print(contents)
print('BeautifulSoup 測試 作業完成')

