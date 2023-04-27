# python import module : re

# _*_ coding: utf-8 _*_
# 程式 6-3.py (Python 3.x version)
# 計算單字在文章中出現的頻率
# 只列出出現超過一次以上的單字

import re

fp = open("data\article.txt", "r")
article = fp.read()
new_article = re.sub("[^a-zA-Z\s]", "", article)
words = new_article.split()
word_counts = {}
for word in words:
    if word.upper() in word_counts:
        word_counts[word.upper()] = word_counts[word.upper()] + 1
    else:
        word_counts[word.upper()] = 1

key_list = list(word_counts.keys())
key_list.sort()
for key in key_list:
    if word_counts[key] > 1:
        print("{}:{}".format(key, word_counts[key]))



# Python 新進測試 15



import re
pat = re.compile('[a-z]+')
m = pat.findall('tem12po')
print(m)  # ['tem', 'po']


import re
pat =r'.*'
s="Do your best,\nGo Go Go!"
m = re.search(pat,s)
print(m.group()) # Do your best,
m2 = re.search(r'.*',s,re.DOTALL)
print(m2.group()) # Do your best,\nGo Go Go!

import re
reobj = re.compile(r'[a-z]+')
m = reobj.findall('3tem12po')
print(m) # ['tem', 'po']



import re
pat =r'[0-9+]+'
s="Amy was 18 year old,she likes Python and C++."
m = re.findall(pat,s)
print(m) # ['18', '++']




import re
pat = re.compile(r'[a-z]+')

m = pat.match('tem12po')
print(m) # <re.Match object; span=(0, 3), match='tem'>
if not m==None:
    print(m.group()) #tem
    print(m.start()) #0
    print(m.end())   #3
    print(m.span())  #(0,3)
import re
pat =r'PYTHON|ANDROID'
s="I like Python and Android!"
m = re.findall(pat,s,re.I)
print(m) #['Python', 'Android']





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
    
    



import re
phoneList=["0412345678","(04)12345678","(04)-12345678","(049)2987654","0937-998877"]
pat = r'''
 \(\d{2,4}\)-?\d{6,8} #(04)12345678、(04)-12345678、(049)2987654 等電話格式
|\d{9,10}             #0412345678 等含 9~10 位數字
|\d{4}-\d{6,8}        #0937-998877 等手機格式
'''

for phone in phoneList:
    phoneNum = re.search(pat,phone,re.VERBOSE)
    if not phoneNum==None:
        print(phoneNum.group())
        
        
import re
pat = '[a-z]+'
m = re.search(pat,'3tem12po')
print(m) # <re.Match object; span=(1, 4), match='tem'>

import re
pat = r'[a-z]+'
m = re.match(pat,'tem12po')
print(m) # <re.Match object; span=(0, 3), match='tem'>

import re
m = re.findall(r'[a-z]+','tem12po')
print(m)  # ['tem', 'po']

import re
pat = re.compile('[a-z]+')

m = pat.search('3tem12po')
print(m) # <re.Match object; span=(1, 4), match='tem'>
if not m==None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())    # 4
    print(m.span())   # (1,4)
    
    
import re
pat =r'.o'
s="Do your best!"
m = re.findall(pat,s)
print(m) # ['Do', 'yo']
m2 = re.findall(r'.*o',s)
print(m2) # ['Do yo']

import re
pat=r"\d+"
substr="*"
s="Password:1234,ID:5678"
result = re.sub(pat,substr,s)
print(result) # Password:*,ID:*


import re

def multiply(m):
    v = int(m.group())
    return str(v * 2)

result = re.sub("\d+", multiply, "10 20 30 40 50",3)
print(result) # 20 40 60 40 50

import re
pat = re.compile(r'[aeiou]*')
s="John is my best friend."
m = re.findall(pat,s)
print(m) 


import re
pat = re.compile(r'[aeiou]+')
s="John is my best friend."
m = re.findall(pat,s)
print(m) #['o', 'i', 'e', 'ie']


def isTaiwanPhone(str):
    if len(str) != 11:       # 如果長度不是11
        return False         # 傳回非手機號碼格式
    #檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):    
        if i==4:
            if str[4] != '-':        # 如果第5個字元不是'-'字元
                return False         # 傳回非手機號碼格式
        else: # 如果前4個字或最後6個字出現非數字字元
            if str[i].isdecimal() == False:
                return False     # 傳回非手機號碼格式
    return True                  # 傳回是正確手機號碼格式        

print("0937-123456 是台灣手機號碼：", isTaiwanPhone('0937-123456'))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone('02-12345678'))


import re
pat =r'[^a-z. ]+'
s="John was 18 year old."
m = re.findall(pat,s)
print(m) #['J', '18']


import re
pat =r'^\d+'
s="2020 is coming soon"
m = re.findall(pat,s)
print(m) #['2020']
m2 = re.findall(r'\w+$',s)
print(m2) #['soon']


import re
numStr="tel:04-12345678"
pat = r'(\d{2})-(\d{8})'

phone = re.search(pat,numStr)
if not phone==None:
    print(phone.group())  #04-12345678
    print(phone.group(0)) #04-12345678
    print(phone.group(1)) #04
    print(phone.group(2)) #12345678   
    
    
import re
numStr="tel:(04)12345678"
pat = r'(\(\d{2}\))(\d{8})'

phone = re.search(pat,numStr)
if not phone==None:
    print(phone.group())  #(04)12345678
    print(phone.group(1)) #(04)
    print(phone.group(2)) #12345678

    
import re
phoneList=["(04)12345678","(04)-12345678"]
pat = r'(\(\d{2}\))-?(\d{8})'

for phone in phoneList:
    phoneNum = re.search(pat,phone)
    if not phoneNum==None:
        print(phoneNum.group())
        
        

import re
phoneList=["0412345678","(04)12345678","(04)-12345678","(049)2987654","0937-998877"]
pat = r'\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}'
for phone in phoneList:
    phoneNum = re.search(pat,phone)
    if not phoneNum==None:
        print(phoneNum.group())
        

import re
pat = re.compile('[a-z]+')
m = pat.findall('tem12po')
print(m)  # ['tem', 'po']


reobj = re.compile(r'[a-z]+')
m = reobj.findall('3tem12po')
print(m) # ['tem', 'po']


m = re.findall(r'[a-z]+','3tem12po')
print(m) # ['tem', 'po']



string1 = '123abcd456efghijk789123'
string2 = 'abcd456efghijk789123abc'

#match 找出從頭出現的英文字字串

m = re.match(r'[a-z]+', string1)
print('match')
print(m)
if not m == None:
    print(m.group()) #tem
    print(m.start()) #0
    print(m.end())   #3
    print(m.span())  #(0, 3)
else:
    print('找不到')

m = re.match(r'[a-z]+', string2)
print('match')
print(m)
if not m == None:
    print(m.group()) #tem
    print(m.start()) #0
    print(m.end())   #3
    print(m.span())  #(0, 3)
else:
    print('找不到')


#search 找出最早出現的英文字字串

m = re.search(r'[a-z]+', string1)
print('search')
print(m)
if not m == None:
    print(m.group())  # abcd
    print(m.start())  # 3
    print(m.end())    # 7
    print(m.span())   # (3, 7)
else:
    print('找不到')

  



import re

regex = "\d{3}-\d{2}-\d{4}"
text = '543-87-3388'
match1 = re.search(regex, text)

if match1 != None:
    print(text, " contains a SSN")
    print("start position of the matched text is " + str(match1.start()))
    print("start and end position of the matched text is " + str(match1.span()))
else:
    print(text, " does not contain a SSN")







