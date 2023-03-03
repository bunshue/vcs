# _*_ coding: utf-8 _*_
# 程式 9-7 (Python 3 version)

from bs4 import BeautifulSoup
import requests
import sys, os
from urllib.parse import urlparse
from urllib.request import urlopen

if len(sys.argv) < 2:
    print("用法：python 9-7.py <<target url>>")
    exit(1)  

url = sys.argv[1]
domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')
all_links = sp.find_all(['a','img'])

for link in all_links:
    src = link.get('src')
    href = link.get('href')
    targets = [src, href]
    for t in targets:
        if t != None and ('.jpg' in t or '.png' in t):
            if t.startswith('http'): full_path = t
            else:                    full_path = domain+t
            print(full_path)
            image_dir = url.split('/')[-1]
            if not os.path.exists(image_dir): os.mkdir(image_dir)
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext: filename = filename + '.jpg'
            else:            filename = filename + '.png'
            image = urlopen(full_path)
            fp = open(os.path.join(image_dir,filename),'wb')
            fp.write(image.read())
            fp.close()
