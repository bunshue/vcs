# ch3_39.py
import requests

url = 'http://httpbin.org/cookies'
cookies = dict(key1='value1')
r = requests.get(url, cookies=cookies)
print(r.text)















