# ch3_29.py
import requests

url = 'https://www.httpbin.org/get'
r = requests.get(url)
print(r.url)





