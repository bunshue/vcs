# ch3_38.py
import requests

url = 'https://www.httpbin.org/image/jpeg'
r = requests.get(url)
img = r.content

fn = 'out3_38.jpg'
with open(fn, 'wb') as fout:
    fout.write(img)













