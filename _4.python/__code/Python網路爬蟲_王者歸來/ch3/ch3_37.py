# ch3_37.py
import requests

url = 'https://www.httpbin.org/response-headers?freeform='
r = requests.get(url)
if r.status_code == 200:
    print(r.headers.get('content-type'))
    print('-'*70)
    print(r.json())












