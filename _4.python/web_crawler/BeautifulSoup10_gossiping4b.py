import requests
import time
import json
import re
from bs4 import BeautifulSoup

PTT_URL = 'https://www.ptt.cc'
FREEGEOIP_API = 'http://freegeoip.net/json/'

def get_web_page(url):
    resp = requests.get(url=url, cookies={'over18': '1'})
    if resp.status_code != 200:
        print('Invalid url: ', resp.url)
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

def get_ip(dom):
    # e.g., ※ 發信站: 批踢踢實業坊(ptt.cc), 來自: 27.52.6.175
    pattern = '來自: \d+\.\d+\.\d+\.\d+'
    match = re.search(pattern, dom)
    if match:
        return match.group(0).replace('來自: ', '')
    else:
        return None

def main():
    print('取得今日文章列表:')
    current_page = get_web_page(PTT_URL + '/bbs/Gossiping/index.html')
    if current_page:
        articles = []
        today = time.strftime('%m/%d').lstrip('0')
        current_articles, prev_url = get_articles(current_page, today)
        while current_articles:
            articles += current_articles
            current_page = get_web_page(PTT_URL + prev_url)
            current_articles, prev_url = get_articles(current_page, today)

        length = len(articles)
        print('共 %d 篇文章' % length)

        for i in range(0,10):
            print(articles[i])

        print()
        print()
        print('取得前10篇文章的資料')
        for article in articles[:10]:
            print(article['title'])
            

        print('取得前10篇文章的IP:')
        country_to_count = dict()
        for article in articles[:10]:
            print('查詢 IP:', article['title'])
            print('111')
            page = get_web_page(PTT_URL + article['href'])
            print('222')
            if page:
                ip = get_ip(page)
                print(ip)


if __name__ == "__main__":
    main()
