"""
會用到 KEY 的
氣象署 / 環境部

"""

import sys
import json
import requests

print("------------------------------------------------------------")  # 60個

print("BeautifulSoup 測試 7")


def get_html_data1(url):
    print("取得網頁資料: ", url)
    resp = requests.get(url)
    # 檢查 HTTP 回應碼是否為 requests.codes.ok(200)
    if resp.status_code != requests.codes.ok:
        print("讀取網頁資料錯誤, url: ", resp.url)
        return None
    else:
        return resp


print("#抓中央氣象局的衛星雲圖")

url = "https://www.cwa.gov.tw/V8/C/W/OBS_Sat.html"

# TBD

"""
html_data = get_html_data1(url)
if html_data:
        soup = BeautifulSoup(html_data.text, 'html.parser')
        print("取得網頁標題", soup.title)
        print('搜尋網頁中的 jpg圖片連結')
        
        regex = re.compile('.*\.jpg')
        imglist = soup.find_all("img", {"src":regex})
        for img in imglist:
            print(img["src"])
        
else:
        print('無法取得網頁資料')
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
