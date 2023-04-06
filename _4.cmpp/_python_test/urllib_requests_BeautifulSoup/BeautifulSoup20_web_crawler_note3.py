import requests
import re
import json
from bs4 import BeautifulSoup

def get_web_page(url):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Invalid url: ', resp.url)
        return None
    else:
        return resp.text

url = 'https://www.google.com.tw/'
page = get_web_page(url)
if page:
    print('取得網頁資料')
else:
    print('無法取得網頁資料')

