import requests
from bs4 import BeautifulSoup
from hanziconv import HanziConv

def bot_get_google(question):
    url = f'https://www.google.com.tw/search?q={question}+維基百科'
    # 以下是要在 get 的表頭加上瀏覽器的資訊, 以偽裝成瀏覽器
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                             ' AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/70.0.3538.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        bs = BeautifulSoup(response.text, 'lxml')
        wiki_url = bs.find('cite')
        # kwd = wiki_url.text.split('/')[-1]
        kwd = wiki_url.text.split('›')[-1].replace(' ','')      # 修正
        keyword_trad = HanziConv.toTraditional(kwd)
        return keyword_trad
    else:
        print('請求失敗')
#----------------------------------------#
keyword = bot_get_google('誰是愛因斯坦')
print(keyword)

