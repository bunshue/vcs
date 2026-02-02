# ch3_13_2.py
import requests

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                          'AppleWebKit/537.36 (KHTML, like Gecko)'
                          'Chrome/75.0.3770.142 Safari/537.36', }
url = 'https://www.kingstone.com.tw/new/basic/2013120504769?zone=book&lid=search&actid=WISE'
htmlfile = requests.get(url, headers=headers)
htmlfile.raise_for_status()
print("偽裝瀏覽器擷取網路資料成功")


