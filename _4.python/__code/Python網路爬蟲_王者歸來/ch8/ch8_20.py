# ch8_20.py
import requests, bs4, re

def get_ip(ipstr):
    ''' 由字串回傳IP地址 '''
    pattern = r'\d+.\d+.\d+.\d+'
    addr = re.search(pattern, ipstr)
    return addr

def get_city(ptturl):
    ''' 由IP地址回傳城市名稱 '''
    url_head = 'http://api.ipstack.com/'
    url_tail = '?access_key=Your API Key'
    url = url_head + ptturl + url_tail
    urlfile = requests.get(url.strip())
    ip_info = urlfile.json()
    return ip_info['city']

url_ptt = 'https://www.ptt.cc'
gossiping = '/bbs/gossiping/index.html'

ptthtml = requests.get(url_ptt+gossiping, cookies={'over18':'1'})
objSoup = bs4.BeautifulSoup(ptthtml.text, 'lxml')

pttdivs = objSoup.find_all('div', 'r-ent')
href = pttdivs[0].find('a')['href']                                 # 文章超連結
title = pttdivs[0].find('a').text

print('目前連線網址 : ', url_ptt+href)
print('目前文章標題 : ', title)
gossiping_html = requests.get(url_ptt+href, cookies={'over18':'1'}) # 進入超連結
gossiping_soup = bs4.BeautifulSoup(gossiping_html.text, 'lxml')   

gossiping_span = gossiping_soup.find('span', 'f2')                  # 爬取文章來源
if gossiping_span:
    print('文章來源 :')
    print(gossiping_span.text)
    ip_addr = get_ip(gossiping_span.text)
    print('IP地址 : ', ip_addr.group())
    ip_city = get_city(ip_addr.group())
    print('IP城市 : ', ip_city)
else:
    print('可能是廣告信件沒有發文IP')

















