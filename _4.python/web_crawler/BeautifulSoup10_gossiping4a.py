import requests
from bs4 import BeautifulSoup

url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'

try:
    resp = requests.get(url)
except:
    resp = None

if resp and resp.status_code == 200:
    print(resp.status_code)
    print(resp.text)
    soup = BeautifulSoup(resp.text, 'html.parser')
    print(soup)
    try:
        h1 = soup.find('h1')
    except:
        h1 = None
    if h1:
        print(soup.find('h1'))
        print(soup.find('h1').text)
    try:
        h2 = soup.find('h2')
    except:
        h2 = None
    if h2:
        print(soup.find('h2').text)
    else:
        print('h2 tag not found!')


import requests
from bs4 import BeautifulSoup

def get_header_text(url, header_tag):
    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, 'html.parser')
            return soup.find(header_tag).text
    except Exception as exception:
        return None


url = 'http://blog.castman.net/web-crawler-tutorial/ch1/connect.html'

h1 = get_header_text(url, 'h1')
if h1:
    print('h1: ' + h1)

h2 = get_header_text(url, 'h2')
if h2:
    print('h2: ' + h2)

p = get_header_text(url, 'p')
if p:
    print('p: ' + p)


# PTT八卦版今日熱門文章

import requests
import time
import json
from bs4 import BeautifulSoup

PTT_URL = 'https://www.ptt.cc'


def get_web_page(url):
    resp = requests.get(url=url, cookies={'over18': '1'})
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text


def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html5lib')
    # Retrieve the link of previous page
    paging_div = soup.find('div', 'btn-group btn-group-paging')
    prev_url = paging_div.find_all('a')[1]['href']

    articles = []
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        # If post date matched:
        if d.find('div', 'date').text.strip() == date:
            # To retrieve the push count:
            push_count = 0
            push_str = d.find('div', 'nrec').text
            if push_str:
                try:
                    push_count = int(push_str)
                except ValueError:
                    # If transform failed, it might be '爆', 'X1', 'X2', etc.
                    if push_str == '爆':
                        push_count = 99
                    elif push_str.startswith('X'):
                        push_count = -10

            # To retrieve title and href of the article:
            if d.find('a'):
                href = d.find('a')['href']
                title = d.find('a').text
                author = d.find('div', 'author').text if d.find('div', 'author') else ''
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count,
                    'author': author
                })

    return articles, prev_url


def get_author_ids(posts, pattern):
    ids = set()
    for post in posts:
        if pattern in post['author']:
            ids.add(post['author'])
    return ids


def main():
    current_page = get_web_page(PTT_URL + '/bbs/Gossiping/index.html')
    if current_page:
        # To keep all of today's articles.
        articles = []
        # Today's date, here we remove the 0 at the head to match the format of PTT date.
        # API doc for strftime: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
        # API doc for lstrip: https://www.tutorialspoint.com/python/string_lstrip.htm
        today = time.strftime("%m/%d").lstrip('0')
        current_articles, prev_url = get_articles(current_page, today)

        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)

        print("Today's 5566:")
        print(get_author_ids(articles, '5566'))

        print('\nThere are ', len(articles), ' posts today.')
        threshold = 50
        print('Hot post(≥ %d push): ' % threshold)
        for article in articles:
            if int(article['push_count']) > threshold:
                print(article)
        # with as: https://openhome.cc/Gossip/Python/WithAs.html
        # json.dump: http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p02_read-write_json_data.html
        with open('gossiping.json', 'w', encoding='UTF-8') as file:
            json.dump(articles, file, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    main()



