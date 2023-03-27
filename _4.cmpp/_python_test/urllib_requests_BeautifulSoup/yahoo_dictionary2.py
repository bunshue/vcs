import requests
from bs4 import BeautifulSoup

def searchdic():
  global search_word
  a = "https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXGvbWIJibWYAFCp9rolQ"
  b = ";_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyA3NmcARmcjIDc2ItdG9wBGdwcmlkAwRuX3JzbHQDMARuX3N1Z2cDMARvcmlnaW4DdHcuZGljdGlvbmFyeS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAM0BHF1ZXJ5A3RhcGUEdF9zdG1wAzE2NTI3MDk5NTM-?"
  c = "p="
  e = "&fr2=sb-top&fr=sfp"
  search = a + b + c + search_word + e
  
  #print(search)

  html_data = requests.get(search)
  if html_data.status_code != 200:
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print('Invalid url: ', html_data.url)
    return None
  else:
    page = html_data.text
  
  soup = BeautifulSoup(page, 'html.parser')

  '''
  print('主解釋 :')
  divs = soup.find_all('div', 'compList mb-25 p-rel') #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
  #print(divs)
  for div in divs:
    #print(div)
    lis = div.find_all('li')  #把li下的所有資料印出來
    for li in lis:
      print('2')
      print(li)
      print(li.text.replace('\n', ''))
  '''
  '''
  print(soup.prettify()) # 把排版後的 html 印出來
  # 一些屬性或方法
  print('---title---')
  print(soup.title) # 把 tag 抓出來
  print('---title.name---')
  print(soup.title.name) # 把 title 的 tag 名稱抓出來
  print('---title.string---')
  print(soup.title.string) # 把 title tag 的內容抓出來
  print('---title.parent.name---')
  print(soup.title.parent.name) # title tag 的上一層 tag
  print('---a---')
  print(soup.a) # 把第一個 <a></a> 抓出來
  print('---all a---')
  print(soup.find_all('a')) # 把所有的 <a></a> 抓出來
  print('---all div---')
  print(soup.find_all('div')) # 把所有的 <a></a> 抓出來
  '''

  divs = soup.find_all('span', 'fz-24 fw-500 c-black lh-24')
  print('搜尋英文字 :')
  #print(divs)
  for div in divs:
      #print(div)
      for di in div:
          print(di.text.replace('\n', ''))

  print('主解釋 :')
  #divs = soup.find_all('div', 'fz-16 fl-l dictionaryExplanation')
  divs = soup.find_all('div', 'compList mb-25 p-rel') #如此可以框選較大範圍之資料 找到較大的區塊包含所有資料
  #print(divs)
  for div in divs:
      #print(div)
      for di in div:
          #print(di)
          print(di.text.replace('\n', ''))    #只是刪除換行符號, 或許不一定有


  print('釋義 :')        
  #divs = soup.find_all('span', 'fz-14')
  divs = soup.find_all('span', 'd-i fz-14 lh-20')
  #print(divs)
  i = 1
  for div in divs:
      for di in div:
          print(i)
          print(di.text.replace('\n', ''))
          i = i + 1





  
search_word = 'oat'
#search_word = '英國'

searchdic()
