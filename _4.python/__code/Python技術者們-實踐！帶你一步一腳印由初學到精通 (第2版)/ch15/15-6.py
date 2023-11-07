from bs4 import BeautifulSoup
import requests

def bot_get_wiki(keyword):
    response = requests.get('https://zh.wikipedia.org/zh-tw/' + keyword)
    bs = BeautifulSoup(response.text, 'lxml')
    p_list = bs.find_all('p')
    for p in p_list:
        if keyword in p.text[0:10]:
            return p.text
#---------------------------------------#
content = bot_get_wiki('愛因斯坦')
print(content)