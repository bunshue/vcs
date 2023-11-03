import requests

url = "http://httpbin.org/user-agent"

r = requests.get(url)
print(r.text)
print("----------------------")

url_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
r = requests.get(url, headers=url_headers)
print(r.text)
