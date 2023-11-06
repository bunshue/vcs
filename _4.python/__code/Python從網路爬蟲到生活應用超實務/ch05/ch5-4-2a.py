import requests

proxy = {'http': 'http://109.161.48.141:3128',
         'https': 'https://109.161.48.141:3128'}
r = requests.get("http://httpbin.org/ip", proxies=proxy)
print(r.status_code)
print(r.text)
