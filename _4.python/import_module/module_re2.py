print('------------------------------------------------------------')	#60個

import re

regex = "\d{3}-\d{2}-\d{4}"
ssn = '543-87-3388'
match1 = re.match(regex, ssn)

if match1 != None:
    print(ssn, " is a valid SSN")
    print("start position of the matched text is " + 
        str(match1.start()))
    print("start and end position of the matched text is " +
        str(match1.span()))
else:
    print(ssn, " is not a valid SSN")
    

print('------------------------------------------------------------')	#60個

print('拆解e-mail')
import re
import requests
regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://csharphelper.com/blog/'
html_data = requests.get(url).text

emails = re.findall(regex, html_data)
for email in emails:
    print(email)

print('------------------------------------------------------------')	#60個
print('拆解e-mail')
import re
import requests

regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url = 'https://auth.cht.com.tw/ldaps/'
html = requests.get(url)
emails = regex.findall(html.text)

for email in emails:
    print(email)


print('------------------------------------------------------------')	#60個

import re
pat = re.compile('[a-z]+')

m = pat.match('tem12po')
print(m) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

print('------------------------------------------------------------')	#60個

import re

m = re.match(r'[a-z]+','tem12po')
print(m) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

print('------------------------------------------------------------')	#60個

import re

pat = re.compile('[a-z]+')

m = pat.search('3tem12po')
print(m) # <_sre.SRE_Match object; span=(1, 4), match='tem'>

if not m==None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())    # 4
    print(m.span())   # (1,4)

print('------------------------------------------------------------')	#60個


import re

msg1 = 'Please call me using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加晚餐'
msg3 = '請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.search(pattern, string)
    if phoneNum != None:    # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum.group()}")
    else:
        print(f"{string} 字串不含電話號碼")

parseString(msg1)
parseString(msg2)
parseString(msg3)


print('------------------------------------------------------------')	#60個


import re

msg1 = 'Please call me using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加晚餐'
msg3 = '請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d\d\d\d-\d\d\d-\d\d\d'
    phoneNum = re.findall(pattern, string)
    if phoneNum != None:    # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum}")
    else:
        print(f"{string} 字串不含電話號碼")

parseString(msg1)
parseString(msg2)
parseString(msg3)

print('------------------------------------------------------------')	#60個

import re

msg1 = 'Please call me using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加晚餐'
msg3 = '請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我'

def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r'\d{4}-\d{3}-\d{3}'
    phoneNum = re.findall(pattern, string)   # 用串列傳回搜尋結果
    print(f"電話號碼是: {phoneNum}")         # 串列方式顯示電話號碼

parseString(msg1)
parseString(msg2)
parseString(msg3)


print('------------------------------------------------------------')	#60個


import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)           # 傳回搜尋結果

print(f"完整號碼是: {phoneNum.group()}")     # 顯示完整號碼
print(f"完整號碼是: {phoneNum.group(0)}")    # 顯示完整號碼
print(f"區域號碼是: {phoneNum.group(1)}")    # 顯示區域號碼
print(f"電話號碼是: {phoneNum.group(2)}")    # 顯示電話號碼

print('------------------------------------------------------------')	#60個

import re

msg = 'Please call my secretary using 02-26669999 or 02-11112222'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.findall(pattern, msg)           # 傳回搜尋結果
print(phoneNum)

print('------------------------------------------------------------')	#60個

import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)      # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()   # 留意是groups()
print(f"區域號碼是: {areaNum}")         # 顯示區域號碼
print(f"電話號碼是: {localNum}")        # 顯示電話號碼

print('------------------------------------------------------------')	#60個

import re

msg = 'Please call my secretary using (02)-26669999'
pattern = r'(\(\d{2}\))-(\d{8})'
phoneNum = re.search(pattern, msg)       # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()    # 留意是groups()
print(f"區域號碼是: {areaNum}")          # 顯示區域號碼
print(f"電話號碼是: {localNum}")         # 顯示電話號碼

print('------------------------------------------------------------')	#60個

msg = 'John and Tom will attend my party tonight. John is my best friend.'
pattern = 'John|Tom'                # 搜尋John和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)
pattern = 'Mary|Tom'                # 搜尋Mary和Tom
txt = re.findall(pattern, msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

msg = 'john and TOM will attend my party tonight. JOHN is my best friend.'
pattern = 'John|Tom'                        # 搜尋John和Tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)
pattern = 'Mary|tom'                        # 搜尋Mary和tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)


print('------------------------------------------------------------')	#60個

import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg1 = 'son'
msg2 = 'sonson'
msg3 = 'sonsonson'
msg4 = 'sonsonsonson'
msg5 = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern,msg1)
searchStr(pattern,msg2)
searchStr(pattern,msg3)
searchStr(pattern,msg4)
searchStr(pattern,msg5)

print('------------------------------------------------------------')	#60個

import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}'
searchStr(pattern,msg)

print('------------------------------------------------------------')	#60個

import re

def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:         # 搜尋失敗
        print("搜尋失敗 ",txt)
    else:                   # 搜尋成功
        print("搜尋成功 ",txt.group())

msg = 'sonsonsonsonson'
pattern = '(son){3,5}?'     # 非貪婪模式
searchStr(pattern,msg)

print('------------------------------------------------------------')	#60個

import re

# 測試1將字串從句子分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '\w+'                    # 不限長度的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2將John開始的字串分離
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John\w*'                # John開頭的單字
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

msg = '1 cat, 2 dogs, 3 pigs, 4 swans'
pattern = '\d+\s\w+'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

# 測試1搜尋[aeiouAEIOU]字元
msg = 'John, Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = '[aeiouAEIOU]'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋[2-5.]字元
msg = '1. cat, 2. dogs, 3. pigs, 4. swans'
pattern = '[2-5.]'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

# 測試1搜尋不在[aeiouAEIOU]的字元
msg = 'A party tonight.'
pattern = '[^aeiouAEIOU]'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋不在[2-5.]的字元
msg = '2 dogs,3 pigs'
pattern = '[^2-5.]'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

# 測試1搜尋John字串在最前面
msg = 'John will attend my party tonight.'
pattern = '^John'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋John字串不是在最前面
msg = 'My best friend is John'
pattern = '^John'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

# 測試1搜尋最後字元是非英文字母數字和底線字元
msg = 'John will attend my party 28 tonight.'
pattern = '\W$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋最後字元是非英文字母數字和底線字元
msg = 'I am 28'
pattern = '\W$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試3搜尋最後字元是數字
msg = 'I am 28'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試4搜尋最後字元是數字
msg = 'I am 28 year old.'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

# 測試1搜尋開始到結尾皆是數字的字串
msg = '09282028222'
pattern = '^\d+$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋開始到結尾皆是數字的字串
msg = '0928tuyr990'
pattern = '^\d+$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

msg = 'cat hat sat at matter flat'
pattern = '.at'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)

print('------------------------------------------------------------')	#60個

import re

msg = 'Name: Jiin-Kwei Hung Address: 8F, Nan-Jing E. Rd, Taipei'
pattern = 'Name: (.*) Address: (.*)'
txt = re.search(pattern,msg)      # 傳回搜尋結果
Name, Address = txt.groups()
print("Name:    ", Name)
print("Address: ", Address)

print('------------------------------------------------------------')	#60個

import re

#測試1搜尋除了換列字元以外字元
msg = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
txt = re.search(pattern,msg)           # 傳回搜尋不含換列字元結果
print("測試1輸出: ", txt.group())
#測試2搜尋包括換列字元
msg = 'Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei'
pattern = '.*'
txt = re.search(pattern,msg,re.DOTALL) # 傳回搜尋含換列字元結果
print("測試2輸出: ", txt.group())

print('------------------------------------------------------------')	#60個

import re

#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  # John是第一個字串
pattern = 'John'
txt = re.match(pattern,msg)                 # 傳回搜尋結果
if txt != None:
    print("測試1輸出: ", txt.group())
else:
    print("測試1搜尋失敗")
#測試2搜尋使用re.match()
msg = 'My best friend is John.'             # John不是第一個字串
txt = re.match(pattern,msg,re.DOTALL)       # 傳回搜尋結果
if txt != None:
    print("測試2輸出: ", txt.group())
else:
    print("測試2搜尋失敗")
print('------------------------------------------------------------')	#60個

import re

#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("使用re.match()輸出MatchObject物件:  ", txt)
else:
    print("測試1搜尋失敗")
#測試1搜尋使用re.search()
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("使用re.search()輸出MatchObject物件: ", txt)
else:
    print("測試1搜尋失敗")
    
print('------------------------------------------------------------')	#60個

import re

#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  
pattern = 'John'
txt = re.match(pattern,msg)                 # re.match()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())
#測試2搜尋使用re.search()
msg = 'My best friend is John.'  
txt = re.search(pattern,msg)                # re.search()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())

print('------------------------------------------------------------')	#60個

import re

#測試1取代使用re.sub()結果成功
msg = 'Eli Nan will attend my party tonight. My best friend is Eli Nan'  
pattern = 'Eli Nan'                 # 欲搜尋字串        
newstr = 'Kevin Thomson'            # 新字串
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果
#測試2取代使用re.sub()結果失敗  
pattern = 'Eli Thomson'             # 欲搜尋字串        
txt = re.sub(pattern,newstr,msg)    # 如果找到則取代           
if txt != msg:                      # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)        # 列出成功取代結果
else:
    print("取代失敗: ", txt)        # 列出失敗取代結果
    
print('------------------------------------------------------------')	#60個

import re

# 使用隱藏文字執行取代
msg = 'CIA Mark told CIA Linda that secret USB had given to CIA Peter.'
pattern = r'CIA (\w)\w*'            # 欲搜尋CIA + 空一格後的名字        
newstr = r'\1***'                   # 新字串使用隱藏文字
txt = re.sub(pattern,newstr,msg)    # 執行取代
print("取代成功: ", txt)            # 列出取代結果

print('------------------------------------------------------------')	#60個

import re

msg = '''txt@deepmind.com.tw
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
eMail = re.findall(pattern, msg, re.VERBOSE)     # 傳回搜尋結果
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])
   

print('------------------------------------------------------------')	#60個


import re

pat = re.compile('[a-z]+')

m = pat.findall('tem12po')
print(m)  # ['tem', 'po']




print('------------------------------------------------------------')	#60個

import re

ispythonprog = re.compile('^[a-zA-Z0-9_]+\.py$')
def ispython(name):
    return bool(ispythonprog.match(name))


short_filename = 'picture1.jpg'
status = ispython(short_filename)
print(status)

short_filename = 'test10_new02.py'
status = ispython(short_filename)
print(status)



print('------------------------------------------------------------')	#60個


pat = r'[0-9+]+'
s = "Amy was 18 year old,she likes Python and C++."
m = re.findall(pat,s)
print(m) # ['18', '++']

print('------------------------------------------------------------')	#60個

pat = r'PYTHON|ANDROID'
s = "I like Python and Android!"
m = re.findall(pat,s,re.I)
print(m) #['Python', 'Android']

print('------------------------------------------------------------')	#60個

pat = r'.*'
s = "Do your best,\nGo Go Go!"
m = re.search(pat,s)
print(m.group()) # Do your best,
m2 = re.search(r'.*',s,re.DOTALL)
print(m2.group()) # Do your best,\nGo Go Go!

print('------------------------------------------------------------')	#60個

reobj = re.compile(r'[a-z]+')
m = reobj.findall('3tem12po')
print(m) # ['tem', 'po']

print('------------------------------------------------------------')	#60個

pat = re.compile('[a-z]+')
m = pat.findall('tem12po')
print(m)  # ['tem', 'po']

print('------------------------------------------------------------')	#60個

m = re.findall(r'[a-z]+', 'abc123xyz')
print(m)    # ['abc', 'xyz']

print('------------------------------------------------------------')	#60個

result = re.sub(r"\d+", "*", "Password:1234,ID:5678")
print(result) # Password:*,ID:*

print('------------------------------------------------------------')	#60個

m = re.search(r'[a-z]+', 'abc123xyz')
print(m)    # <re.Match object; span=(0, 3), match='abc'>
if m != None:
    print(m.group())  # abc
    print(m.start())  # 0
    print(m.end())    # 3
    print(m.span())   # (0,3)

print('------------------------------------------------------------')	#60個


m = re.match(r'[a-z]+','abc123xyz')
print(m) 
if m != None:
    print(m.group())    #abc
    print(m.start())    #0
    print(m.end())      #3
    print(m.span())     #(0, 3)



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



