# _*_ coding: utf-8 _*_
# 程式 9-10 (Python 3 version)

from bs4 import BeautifulSoup
import requests
import sys, os
from urllib.parse import urlparse
from urllib.request import urlopen

post_html = '''
</body>
</html>
'''

if len(sys.argv) < 2:
    print("用法：python 9-10.py <<target url>>")
    exit(1)  

url = sys.argv[1]
domain = "{}://{}".format(urlparse(url).scheme, urlparse(url).hostname)
html = requests.get(url).text
sp = BeautifulSoup(html, 'html.parser')

pre_html = """
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<title>網頁搜集來的資料</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>
  <style>
  .carousel-inner > .item > img,
  .carousel-inner > .item > a > img {
      border: 5px solid white;
      width: 50%;
      box-shadow: 10px 10px 5px #888888;
      margin: auto;
  }
  </style>

</head>
<body>
<center><h3>以下是從網頁搜集來的圖片跑馬燈</h3></center>
"""

all_links = sp.find_all(['a','img'])

carousel_part1 = ""
carousel_part2 = ""
picno = 0

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

            if picno==0:
                carousel_part1 += "<li data-target='#myC' data-slide-to='{}' class='active'></li>".format(picno)
                carousel_part2 += """
                    <div class='item active'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(filename, filename)

            else:
                carousel_part1 += "<li data-target='#myC' data-slide-to='{}'></li>".format(picno)
                carousel_part2 += """
                    <div class='item'>
                        <img src='{}' alt='{}'>  
                    </div>""".format(filename, filename)
            picno += 1

            html_body = """
            <div id='myC' class='carousel slide' data-ride='carousel'>
                <ol class='carousel-indicators'>
                {}
                </ol>
                <div class='carousel-inner' role='listbox'>
                {}
                </div>
                <a class="left carousel-control" href="#myC" role="button" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                    <span class="sr-only">前一張</span>
                </a>
                <a class="right carousel-control" href="#myC" role="button" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                    <span class="sr-only">後一張</span>
                </a>
            </div>
            """.format(carousel_part1, carousel_part2)

fp = open(os.path.join(image_dir,'index.html'), 'w')
fp.write(pre_html+html_body+post_html)
fp.close()            

