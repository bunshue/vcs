# ch3_12_1.py
import requests

url = 'https://www.kingstone.com.tw/new/basic/2013120504769?zone=book&lid=search&actid=WISE'
htmlfile = requests.get(url)
htmlfile.raise_for_status()



