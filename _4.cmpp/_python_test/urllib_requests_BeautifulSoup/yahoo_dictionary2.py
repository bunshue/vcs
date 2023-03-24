import requests
from bs4 import BeautifulSoup

def searchdic():
  print('searchdic')
  global search_word
  a = "https://tw.dictionary.search.yahoo.com/search;_ylt=AwrtXGvbWIJibWYAFCp9rolQ"
  b = ";_ylc=X1MDMTM1MTIwMDM4MQRfcgMyBGZyA3NmcARmcjIDc2ItdG9wBGdwcmlkAwRuX3JzbHQDMARuX3N1Z2cDMARvcmlnaW4DdHcuZGljdGlvbmFyeS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAM0BHF1ZXJ5A3RhcGUEdF9zdG1wAzE2NTI3MDk5NTM-?"
  c = "p="
  e = "&fr2=sb-top&fr=sfp"
  search = a + b + c + search_word + e
  print(search)

  resp = requests.get(search)
  soup = BeautifulSoup(resp.text, 'html.parser')
  #print(soup.find('','compList mb-25 p-rel'))

  #divs = soup.find_all('div', 'fz-16 fl-l dictionaryExplanation')
  if soup.find('div','fz-16 fl-l dictionaryExplanation') == None:
    print("Invalid query!")
  else:
    print('ddddddddd')
    print(soup.find('div','compList mb-25 p-rel').text)
    divs = soup.find_all('div', 'compList mb-25 p-rel')
    for div in divs:
      print(f"{[s for s in div.stripped_strings]}""\n")

    for div in divs:
        lis = div.find_all('li')
        for li in lis:
            print(li.text.replace('\n', ''))

def changechinesetourl():
  print('changechinesetourl')
  global search_word
  from urllib import parse
  str = search_word
  search_word = parse.quote(str)
  searchdic()

def is_contains_chinese():
    print('is_contains_chinese')
    global search_word
    for _char in search_word:
        if '\u4e00' <= _char <= '\u9fa5':
            print('True')
            return True
    print('False')
    return False


search_word = 'substitution'
#search_word = '英國'

is_contains_chinese()

if True:
  print('英翻中')
  changechinesetourl()
else:
  print('中翻英')
  searchdic()

