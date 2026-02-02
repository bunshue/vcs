# ch3_36.py
import requests

url = 'https://www.httpbin.org/html'
r = requests.get(url)
print(r.encoding)
print('-'*70)
print(r.text)












