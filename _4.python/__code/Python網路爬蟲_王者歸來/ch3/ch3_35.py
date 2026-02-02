# ch3_35.py
import requests

url = 'https://www.httpbin.org/get'
r = requests.get(url)
print(r.status_code)
print(r.reason)











