'''
re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
语法格式为：
re.compile(pattern[, flags])



'''


import sys

import re
# python import module : re


print('------------------------------------------------------------')	#60個

# 計算單字在文章中出現的頻率
# 只列出出現超過一次以上的單字

'''
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
'''

print('------------------------------------------------------------')	#60個

text = 'tem12po'
pattern = '[a-z]+'
reobj = re.compile(pattern)  #compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt)  # ['tem', 'po']

text = '3tem12po'
pattern = r'[a-z]+'
reobj = re.compile(pattern) #compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt) # ['tem', 'po']

text = '3tem12po'
pattern = r'[a-z]+'
reobj = re.compile(pattern) #compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt) # ['tem', 'po']

text = '3tem12po'
pattern = r'[a-z]+'
reobj = re.compile(pattern) #compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt) # ['tem', 'po']

print('------------------------------------------------------------')	#60個

text = '3tem12po'
pattern = r'[a-z]+'
txt = re.findall(pattern, text)
print(txt) # ['tem', 'po']

print('------------------------------------------------------------')	#60個

text = '3tem12po'
pattern = '[a-z]+'
txt = re.search(pattern, text)
print(txt) # <re.Match object; span=(1, 4), match='tem'>

print('------------------------------------------------------------')	#60個

text = 'tem12po'
pattern = r'[a-z]+'
txt = re.match(pattern, text)
print(txt) # <re.Match object; span=(0, 3), match='tem'>

print('------------------------------------------------------------')	#60個

text = 'tem12po'
pattern = r'[a-z]+'
txt = re.findall(pattern, text)
print(txt)  # ['tem', 'po']

print('------------------------------------------------------------')	#60個

text = '3tem12po'
pattern = '[a-z]+'
reobj = re.compile(pattern)  #compile() 建立一個正規表達式的規則

txt = reobj.search(text)

print(txt) # <re.Match object; span=(1, 4), match='tem'>
if not txt == None:
    print(txt.group())  # tem
    print(txt.start())  # 1
    print(txt.end())    # 4
    print(txt.span())   # (1,4)

print('------------------------------------------------------------')	#60個    

text = 'tem12po'
pattern = r'[a-z]+'
reobj = re.compile(pattern) #compile() 建立一個正規表達式的規則

txt = reobj.match(text)

print(txt) # <re.Match object; span=(0, 3), match='tem'>
if not txt == None:
    print(txt.group()) #tem
    print(txt.start()) #0
    print(txt.end())   #3
    print(txt.span())  #(0,3)

print('------------------------------------------------------------')	#60個

text = 'tem12po'
pattern = '[a-z]+'
reobj = re.compile(pattern)  #compile() 建立一個正規表達式的規則

txt = reobj.match(text)
print(txt) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not txt == None:
    print(txt.group())
    print(txt.start())
    print(txt.end())
    print(txt.span())

print('------------------------------------------------------------')	#60個

text = 'tem12po'
pattern = r'[a-z]+'
txt = re.match(pattern, text)

print(txt) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not txt == None:
    print(txt.group())
    print(txt.start())
    print(txt.end())
    print(txt.span())

print('------------------------------------------------------------')	#60個

text = '3tem12po'
pattern = '[a-z]+'
reobj = re.compile(pattern)  #compile() 建立一個正規表達式的規則

txt = reobj.search(text)
print(txt) # <_sre.SRE_Match object; span=(1, 4), match='tem'>

if not txt == None:
    print(txt.group())  # tem
    print(txt.start())  # 1
    print(txt.end())    # 4
    print(txt.span())   # (1,4)

print('------------------------------------------------------------')	#60個

text = "Amy was 18 year old,she likes Python and C++."
pattern = r'[0-9+]+'
txt = re.findall(pattern, text)
print(txt) # ['18', '++']
print('text :', text)
print('pattern :', pattern)
print('result :', txt)

print('------------------------------------------------------------')	#60個

text = 'abc123xyz'
pattern = r'[a-z]+'
txt = re.findall(pattern, text)
print(txt)    # ['abc', 'xyz']
print('text :', text)
print('pattern :', pattern)
print('result :', txt)

print('------------------------------------------------------------')	#60個

txt = re.sub(r"\d+", "*", "Password:1234,ID:5678")
print(txt) # Password:*,ID:*
print('text :', text)
print('pattern :', pattern)
print('result :', txt)

print('------------------------------------------------------------')	#60個

text = "Do your best,\nGo Go Go!"
pattern = r'.*'

txt = re.search(pattern, text)
print(txt.group()) # Do your best,

print('傳回搜尋含換列字元結果, re.DOTALL')
txt = re.search(r'.*', text, re.DOTALL)
print(txt.group()) # Do your best,\nGo Go Go!

print('------------------------------------------------------------')	#60個

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
print('尋找 email')
emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',html)
for email in emails:
    print(email)

print('尋找 定價金額')
price = re.findall(r'[\d]+元',html)[0].split('元')[0] #價格
print(price)

print('尋找 圖片網址')
imglist = re.findall(r'[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+',html)
for img in imglist: #
    print(img)

print('尋找 電話號碼')    
texts = re.findall(r'\(?\d{2,4}\)?\-\d{6,8}', html)
for text in texts:
    print(text)

print('------------------------------------------------------------')	#60個

text = "Do your best!"
pattern = r'.o'

txt = re.findall(pattern, text)
print(txt) # ['Do', 'yo']

txt = re.findall(r'.*o', text)
print(txt) # ['Do yo']

print('------------------------------------------------------------')	#60個

text = "Password:1234,ID:5678"
pattern = r"\d+"
substr = "*"
txt = re.sub(pattern, substr, text)
print(txt) # Password:*,ID:*

print('------------------------------------------------------------')	#60個

def multiply(m):
    v = int(m.group())
    return str(v * 2)

txt = re.sub("\d+", multiply, "10 20 30 40 50",3)
print(txt) # 20 40 60 40 50

print('------------------------------------------------------------')	#60個

text = "John is my best friend."
pattern = r'[aeiou]*'
reobj = re.compile(pattern)   #compile() 建立一個正規表達式的規則
txt = re.findall(reobj, text)
print(txt)

text = "John is my best friend."
pattern = r'[aeiou]+'
reobj = re.compile(pattern)   #compile() 建立一個正規表達式的規則
txt = re.findall(reobj, text)
print(txt) #['o', 'i', 'e', 'ie']

print('------------------------------------------------------------')	#60個

text = "John was 18 year old."
pattern = r'[^a-z. ]+'
txt = re.findall(pattern, text)
print(txt) #['J', '18']

print('------------------------------------------------------------')	#60個

text = "2020 is coming soon"
pattern =r'^\d+'

txt = re.findall(pattern, text)
print(txt) #['2020']

txt = re.findall(r'\w+$', text)
print(txt) #['soon']

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

text1 = '123abcd456efghijk789123'
text2 = 'abcd456efghijk789123abc'

#match 找出從頭出現的英文字字串
pattern = r'[a-z]+'
txt = re.match(pattern, text1)
print('match')
print(txt)
if not txt == None:
    print(txt.group()) #tem
    print(txt.start()) #0
    print(txt.end())   #3
    print(txt.span())  #(0, 3)
else:
    print('找不到')

pattern = r'[a-z]+'
txt = re.match(pattern, text2)
print('match')
print(txt)
if not txt == None:
    print(txt.group()) #tem
    print(txt.start()) #0
    print(txt.end())   #3
    print(txt.span())  #(0, 3)
else:
    print('找不到')

#search 找出最早出現的英文字字串
pattern = r'[a-z]+'
txt = re.search(pattern, text1)
print('search')
print(txt)
if not txt == None:
    print(txt.group())  # abcd
    print(txt.start())  # 3
    print(txt.end())    # 7
    print(txt.span())   # (3, 7)
else:
    print('找不到')
  
print('------------------------------------------------------------')	#60個

'''
print('拆解e-mail')
import requests
pattern = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://csharphelper.com/blog/'
html_data = requests.get(url).text

emails = re.findall(pattern, html_data)
for email in emails:
    print(email)

print('------------------------------------------------------------')	#60個
print('拆解e-mail')
import requests

pattern = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url = 'https://auth.cht.com.tw/ldaps/'
html = requests.get(url)
emails = pattern.findall(html.text)

for email in emails:
    print(email)
'''
print('------------------------------------------------------------')	#60個

text = 'John and Tom will attend my party tonight. John is my best friend.'

print('搜尋John或Tom')
pattern = 'John|Tom'                # 搜尋John和Tom
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('搜尋Mary或Tom')
pattern = 'Mary|Tom'                # 搜尋Mary和Tom
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

text = 'john and TOM will attend my party tonight. JOHN is my best friend.'

print('搜尋John或Tom, 忽略大小寫')
pattern = 'John|Tom'                        # 搜尋John和Tom
txt = re.findall(pattern, text, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)

print('搜尋Mary或Tom, 忽略大小寫')
pattern = 'Mary|tom'                        # 搜尋Mary和tom
txt = re.findall(pattern, text, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)

print('------------------------------------------------------------')	#60個

def searchStr(pattern, text):
    txt = re.search(pattern, text)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

text1 = 'son'
text2 = 'sonson'
text3 = 'sonsonson'
text4 = 'sonsonsonson'
text5 = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern, text1)
searchStr(pattern, text2)
searchStr(pattern, text3)
searchStr(pattern, text4)
searchStr(pattern, text5)

print('------------------------------------------------------------')	#60個

def searchStr(pattern, text):
    txt = re.search(pattern, text)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

text = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern, text)

print('------------------------------------------------------------')	#60個

def searchStr(pattern, text):
    txt = re.search(pattern, text)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

text = 'sonsonsonsonson'
pattern = '(son){3,5}?'     # 非貪婪模式
searchStr(pattern, text)

print('------------------------------------------------------------')	#60個

# 測試1將字串從句子分離
text = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '\w+'                    # 不限長度的單字
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試2將John開始的字串分離
text = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John\w*'                # John開頭的單字
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

text = '1 cat, 2 dogs, 3 pigs, 4 swans'
pattern = '\d+\s\w+'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

# 測試1搜尋[aeiouAEIOU]字元
text = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '[aeiouAEIOU]'           
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試2搜尋[2-5.]字元
text = '1. cat, 2. dogs, 3. pigs, 4. swans'
pattern = '[2-5.]'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

# 測試1搜尋不在[aeiouAEIOU]的字元
text = 'A party tonight.'
pattern = '[^aeiouAEIOU]'           
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試2搜尋不在[2-5.]的字元
text = '2 dogs,3 pigs'
pattern = '[^2-5.]'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

# 測試1搜尋John字串在最前面
text = 'John will attend my party tonight.'
pattern = '^John'           
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試2搜尋John字串不是在最前面
text = 'My best friend is John'
pattern = '^John'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

# 測試1搜尋最後字元是非英文字母數字和底線字元
text = 'John will attend my party 28 tonight.'
pattern = '\W$'           
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試2搜尋最後字元是非英文字母數字和底線字元
text = 'I am 28'
pattern = '\W$'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試3搜尋最後字元是數字
text = 'I am 28'
pattern = '\d$'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試4搜尋最後字元是數字
text = 'I am 28 year old.'
pattern = '\d$'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

# 測試1搜尋開始到結尾皆是數字的字串
text = '09282028222'
pattern = '^\d+$'           
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

# 測試2搜尋開始到結尾皆是數字的字串
text = '0928tuyr990'
pattern = '^\d+$'
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

text = 'cat hat sat at matter flat'
pattern = '.at'           
txt = re.findall(pattern, text)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

text = 'Name: Jiin-Kwei Hung Address: 8F, Nan-Jing E. Rd, Taipei'
pattern = 'Name: (.*) Address: (.*)'
txt = re.search(pattern, text)      # 傳回搜尋結果
Name, Address = txt.groups()
print("Name:    ", Name)
print("Address: ", Address)

print('------------------------------------------------------------')	#60個

#測試1搜尋除了換列字元以外字元
text = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
txt = re.search(pattern, text)           # 傳回搜尋不含換列字元結果
print("測試1輸出: ", txt.group())

#測試2搜尋包括換列字元
text = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
print('傳回搜尋含換列字元結果, re.DOTALL')
txt = re.search(pattern, text, re.DOTALL)
print("測試2輸出: ", txt.group())

print('------------------------------------------------------------')	#60個

#測試1搜尋使用re.match()
text = 'John will attend my party tonight.'  # John是第一個字串
pattern = 'John'
txt = re.match(pattern, text)                 # 傳回搜尋結果
if txt != None:
    print("測試1輸出: ", txt.group())
else:
    print("測試1搜尋失敗")

#測試2搜尋使用re.match()
text = 'My best friend is John.'             # John不是第一個字串
print('傳回搜尋含換列字元結果, re.DOTALL')
txt = re.match(pattern, text, re.DOTALL)       # 傳回搜尋結果
if txt != None:
    print("測試2輸出: ", txt.group())
else:
    print("測試2搜尋失敗")

print('------------------------------------------------------------')	#60個

#測試1搜尋使用re.match()
text = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern, text)                 # re.match()
if txt != None:
    print("使用re.match()輸出MatchObject物件:  ", txt)
else:
    print("測試1搜尋失敗")

#測試1搜尋使用re.search()
txt = re.search(pattern, text)                # re.search()
if txt != None:
    print("使用re.search()輸出MatchObject物件: ", txt)
else:
    print("測試1搜尋失敗")
    
print('------------------------------------------------------------')	#60個

#測試1搜尋使用re.match()
text = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern, text)                 # re.match()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())

#測試2搜尋使用re.search()
text = 'My best friend is John.'  
txt = re.search(pattern, text)                # re.search()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())

print('------------------------------------------------------------')	#60個

#測試1取代使用re.sub()結果成功
text = 'Eli Nan will attend my party tonight. My best friend is Eli Nan'  
pattern = 'Eli Nan'                 # 欲搜尋字串        
newstr = 'Kevin Thomson'            # 新字串
txt = re.sub(pattern,newstr, text)    # 如果找到則取代
if txt != text:                      # 如果txt與text內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果

#測試2取代使用re.sub()結果失敗  
pattern = 'Eli Thomson'             # 欲搜尋字串        
txt = re.sub(pattern,newstr, text)    # 如果找到則取代           
if txt != text:                      # 如果txt與text內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果
    
print('------------------------------------------------------------')	#60個

# 使用隱藏文字執行取代
text = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
pattern = r'CIA (\w)\w*'            # 欲搜尋CIA + 空一格後的名字        
newstr = r'\1***'                   # 新字串使用隱藏文字
txt = re.sub(pattern,newstr, text)    # 執行取代
print("取代成功: ", txt)            # 列出取代結果

print('------------------------------------------------------------')	#60個

text = '''txt@deepmind.com.tw
         kkk@gmail.com,
         abc@aa
         abcdefg'''
pattern = r'''(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}                   # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4})?                # 國別
    )'''

print('有VERBOSE搜尋')
eMail = re.findall(pattern, text, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])

print('------------------------------------------------------------')	#60個

print('檢查是否為合法的python檔案名')
ispythonprog = re.compile('^[a-zA-Z0-9_]+\.py$')    #compile() 建立一個正規表達式的規則
def ispython(name):
    return bool(ispythonprog.match(name))

short_filename = 'picture1.jpg'
status = ispython(short_filename)
print('檔案名 :', short_filename, ' ', status) 

short_filename = 'test10_new02.py'
status = ispython(short_filename)
print('檔案名 :', short_filename, ' ', status)

print('------------------------------------------------------------')	#60個

text = "Amy was 18 year old, she likes Python and C++."
pattern = r'[0-9+]+'
txt = re.findall(pattern, text)
print(txt) # ['18', '++']

print('------------------------------------------------------------')	#60個

print('搜尋, 忽略大小寫')
text = "I like Python and Android!"
pattern = r'PYTHON|ANDROID'
txt = re.findall(pattern, text, re.I)
print(txt) #['Python', 'Android']

print('------------------------------------------------------------')	#60個

print('搜尋, 忽略大小寫')
text = "I like Python and Android!"
pattern = r'PYTHON|ANDROID'
txt = re.findall(pattern, text, re.I)
print(txt) #['Python', 'Android']
print('text :', text)
print('pattern :', pattern)
print('result :', txt)

print('------------------------------------------------------------')	#60個

text = "Do your best,\nGo Go Go!"
pattern = r'.*'
txt = re.search(pattern, text)
print(txt.group()) # Do your best,

print('傳回搜尋含換列字元結果, re.DOTALL')
txt = re.search(r'.*', text, re.DOTALL)
print(txt.group()) # Do your best,\nGo Go Go!

print('------------------------------------------------------------')	#60個

pattern = r'[a-z]+'
txt = re.search(pattern, 'abc123xyz')
print(txt)    # <re.Match object; span=(0, 3), match='abc'>
if txt != None:
    print(txt.group())  # abc
    print(txt.start())  # 0
    print(txt.end())    # 3
    print(txt.span())   # (0,3)

print('------------------------------------------------------------')	#60個

pattern = r'[a-z]+'
txt = re.match(pattern, 'abc123xyz')
print(txt) 
if txt != None:
    print(txt.group())    #abc
    print(txt.start())    #0
    print(txt.end())      #3
    print(txt.span())     #(0, 3)

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('找電話號碼')

texts = ["0412345678","(04)12345678","(04)-12345678","(049)2987654","0937-998877"]
pattern = r'''
 \(\d{2,4}\)-?\d{6,8} #(04)12345678、(04)-12345678、(049)2987654 等電話格式
|\d{9,10}             #0412345678 等含 9~10 位數字
|\d{4}-\d{6,8}        #0937-998877 等手機格式
'''

print('無VERBOSE搜尋')
for text in texts:
    txt = re.search(pattern, text)
    if not txt == None:
        print(txt.group())

print('有VERBOSE搜尋')
for text in texts:
    txt = re.search(pattern, text, re.VERBOSE)
    if not txt == None:
        print(txt.group())

print('------------------------------------------------------------')	#60個

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

print('------------------------------------------------------------')	#60個

text = "tel:04-12345678"
pattern = r'(\d{2})-(\d{8})'

txt = re.search(pattern, text)
if not txt == None:
    print(txt.group())  #04-12345678
    print(txt.group(0)) #04-12345678
    print(txt.group(1)) #04
    print(txt.group(2)) #12345678   
    
print('------------------------------------------------------------')	#60個

text = "tel:(04)12345678"
pattern = r'(\(\d{2}\))(\d{8})'

txt = re.search(pattern, text)
if not txt == None:
    print(txt.group())  #(04)12345678
    print(txt.group(1)) #(04)
    print(txt.group(2)) #12345678

print('------------------------------------------------------------')	#60個

texts = ["(04)12345678","(04)-12345678"]
pattern = r'(\(\d{2}\))-?(\d{8})'

for text in texts:
    txt = re.search(pattern, text)
    if not txt == None:
        print(txt.group())
        
print('------------------------------------------------------------')	#60個        

texts = ["0412345678","(04)12345678","(04)-12345678","(049)2987654","0937-998877"]
pattern = r'\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}'

for text in texts:
    txt = re.search(pattern, text)
    if not txt == None:
        print(txt.group())
        
print('------------------------------------------------------------')	#60個

text = '543-87-3388'
pattern = "\d{3}-\d{2}-\d{4}"

txt = re.search(pattern, text)

if txt != None:
    print(text, " contains a SSN")
    print("start position of the matched text is " + str(txt.start()))
    print("start and end position of the matched text is " + str(txt.span()))
else:
    print(text, " does not contain a SSN")

print('------------------------------------------------------------')	#60個

text = '543-87-3388'
pattern = "\d{3}-\d{2}-\d{4}"
txt = re.match(pattern, text)

if txt != None:
    print(text, " is a valid SSN")
    print("start position of the matched text is " + 
        str(txt.start()))
    print("start and end position of the matched text is " +
        str(txt.span()))
else:
    print(text, " is not a valid SSN")
    
print('------------------------------------------------------------')	#60個

text1 = 'Please call me using 0930-919-919 or 0952-001-001'
text2 = '請明天17:30和我一起參加晚餐'
text3 = '請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我'

def parseText(text):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    txt = re.search(pattern, text)
    if txt != None:    # 如果txt不是None表示取得號碼
        print(f"電話號碼是: {txt.group()}")
    else:
        print(f"{text} 字串不含電話號碼")

parseText(text1)
parseText(text2)
parseText(text3)

print('------------------------------------------------------------')	#60個

text1 = 'Please call me using 0930-919-919 or 0952-001-001'
text2 = '請明天17:30和我一起參加晚餐'
text3 = '請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我'

def parseText(text):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    txt = re.findall(pattern, text)
    if txt != None:    # 如果txt不是None表示取得號碼
        print(f"電話號碼是: {txt}")
    else:
        print(f"{text} 字串不含電話號碼")

parseText(text1)
parseText(text2)
parseText(text3)

print('------------------------------------------------------------')	#60個

text1 = 'Please call me using 0930-919-919 or 0952-001-001'
text2 = '請明天17:30和我一起參加晚餐'
text3 = '請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我'

def parseText(text):
    """解析字串是否含有電話號碼"""
    pattern = r'\d{4}-\d{3}-\d{3}'
    txt = re.findall(pattern, text)   # 用串列傳回搜尋結果
    print(f"電話號碼是: {txt}")         # 串列方式顯示電話號碼

parseText(text1)
parseText(text2)
parseText(text3)

print('------------------------------------------------------------')	#60個

text = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
txt = re.search(pattern, text)           # 傳回搜尋結果

print(f"完整號碼是: {txt.group()}")     # 顯示完整號碼
print(f"完整號碼是: {txt.group(0)}")    # 顯示完整號碼
print(f"區域號碼是: {txt.group(1)}")    # 顯示區域號碼
print(f"電話號碼是: {txt.group(2)}")    # 顯示電話號碼

print('------------------------------------------------------------')	#60個

text = 'Please call my secretary using 02-26669999 or 02-11112222'
pattern = r'(\d{2})-(\d{8})'
txt = re.findall(pattern, text)           # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

text = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
txt = re.search(pattern, text)      # 傳回搜尋結果
areaNum, localNum = txt.groups()   # 留意是groups()
print(f"區域號碼是: {areaNum}")         # 顯示區域號碼
print(f"電話號碼是: {localNum}")        # 顯示電話號碼

print('------------------------------------------------------------')	#60個

text = 'Please call my secretary using (02)-26669999'
pattern = r'(\(\d{2}\))-(\d{8})'
txt = re.search(pattern, text)       # 傳回搜尋結果
areaNum, localNum = txt.groups()    # 留意是groups()
print(f"區域號碼是: {areaNum}")          # 顯示區域號碼
print(f"電話號碼是: {localNum}")         # 顯示電話號碼

