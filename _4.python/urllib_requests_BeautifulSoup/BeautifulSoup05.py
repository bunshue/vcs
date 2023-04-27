import sys
import requests
from bs4 import BeautifulSoup

def get_html_data1(url):
    print('取得網頁資料: ', url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print('讀取網頁資料錯誤, url: ', resp.url)
        return None
    else:
        return resp

url = 'https://www.nkust.edu.tw/'
sel = '#sm_div_cmb_1_15062 > div > div > section'   #沒用到

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

print()
print('找第一個標籤p')
target = soup.p
print(target)
print()

print('找第一個標籤p')
target = soup.p
print(target)
print()









print('BeautifulSoup 測試 作業完成')

