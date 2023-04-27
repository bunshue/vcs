html_data = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
</div>
"""

import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_data, 'html.parser')

emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html_data)
for email in emails:
    print(email)

price = re.findall(r"[\d]+", soup.select('.price')[0].text)[0] #價格
print(price)

regex = re.compile('.*\.jpg')
imglist = soup.find_all("img", {"src":regex})
for img in imglist:
    print(img["src"])



