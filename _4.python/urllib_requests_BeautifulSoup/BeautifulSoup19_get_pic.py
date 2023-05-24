import sys
import requests
import re
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

print('BeautifulSoup 測試 1')

#url = 'https://pornav.co/'
url = 'https://www.deviantart.com/'

html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, 'html.parser')
        #print(soup.prettify())  #prettify()這個函數可以將DOM tree以比較美觀的方式印出。

        print("取得網頁標題", soup.title)

        print('搜尋網頁中的 jpg圖片連結')
        regex = re.compile('.*\.jpg')
        imglist = soup.find_all("img", {"src":regex})
        for img in imglist:
            print(img["src"])
        
else:
        print('無法取得網頁資料')



print('BeautifulSoup 測試 作業完成')







