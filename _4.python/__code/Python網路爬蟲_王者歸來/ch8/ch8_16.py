# ch8_16.py
import requests, bs4

url_ppt = 'https://www.ptt.cc'
beauty = '/bbs/beauty/index.html'

ptthtml = requests.get(url_ppt+beauty, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

pttdivs = objSoup.find_all('div', 'r-ent')
href = pttdivs[0].find('a')['href']                                 # 文章超連結

print('目前連線網址 : ', url_ppt+href)
beauty_html = requests.get(url_ppt+href, cookies={'over18':'1'})    # 進入超連結
beauty_soup = bs4.BeautifulSoup(beauty_html.text, 'lxml')   

beauty_divs = beauty_soup.find('div', id='main-content')
items = beauty_divs.find_all('div', 'push')
print('評論如下:')
for item in items:
    topiclist = list(item)
    push = topiclist[0]
    push_id = topiclist[1]
    push_content = topiclist[2]
    push_time = topiclist[3]
    print('推      :', push.text)
    print('作者    :', push_id.text)
    print('內文   ', push_content.text)
    print('時間    :', push_time.text.strip())














