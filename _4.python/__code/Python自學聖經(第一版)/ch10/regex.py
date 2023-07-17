html = """
<div class="content">
    E-Mail：<a href="mailto:mail@test.com.tw">mail</a><br>
    E-Mail2：<a href="mailto:mail2@test.com.tw">mail2</a><br>
    <ul class="price">定價：360元 </ul>
    <img src="http://test.com.tw/p1.jpg">
    <img src="http://test.com.tw/p2.jpg">
    <img src="http://test.com.tw/p3.png">
    電話：(04)-76543210、0937-123456
</div>
"""

import re

emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',html)
for email in emails: #顯示 email
    print(email)

price=re.findall(r'[\d]+元',html)[0].split('元')[0] #價格
print(price) #顯示定價金額

imglist = re.findall(r'[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+',html)
for img in imglist: #
    print(img) #顯示圖片網址
    
phonelist = re.findall(r'\(?\d{2,4}\)?\-\d{6,8}',html)
for phone in phonelist:
    print(phone) #顯示電話號碼 