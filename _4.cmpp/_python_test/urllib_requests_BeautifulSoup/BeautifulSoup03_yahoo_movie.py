# Python 測試 BeautifulSoup

import sys
import requests
from bs4 import BeautifulSoup


import ssl
from urllib import request, parse
from bs4 import BeautifulSoup

context = ssl._create_unverified_context()
req_obj = request.Request('https://movies.yahoo.com.tw/chart.html')
with request.urlopen(req_obj,context=context) as res_obj:
 resp = res_obj.read().decode('utf-8')
 soup = BeautifulSoup(resp , 'html.parser')
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
  contents.append(c)

print(contents)




print('BeautifulSoup 測試 作業完成')

