"""
re.compile 函数
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
语法格式为：
re.compile(pattern[, flags])

特殊字元表
\d  0~9之間的整數字元
\D  除了 0~9之間的整數字元 以外的其他字元
\s  空白、定位、Tab、換行、換頁字元
\S  除了 空白、定位、Tab、換行、換頁字元 以外的其他字元
\w  數字、字母、底線[A-Za-z0-9]
\W  除了 數字、字母、底線[A-Za-z0-9] 以外的其他字元

+  左邊或是括號的字元 重複
*  左邊或是括號的字元 重複
?  左邊或是括號的字元 可有可無

re.search()
re.compile() + .findall()
re.findall
re.split

# re.search()
# re.compile() + .findall()
# re.match()
# re.sub() 取代功能

# re.I  # 傳回搜尋忽略大小寫的結果
# re.VERBOSE  # 傳回搜尋結果

"""

import sys
import re

print("------------------------------------------------------------")  # 60個
# re.search() ST
print("------------------------------------------------------------")  # 60個

# search 找出最早出現的英文字字串
print("找出第一群符合全英文的字串")
text = "123abc456def789ghi"
pattern = r"[a-z]+"
txt = re.search(pattern, text)
print(txt)  # <re.Match object; span=(3, 6), match='abc'>
if txt != None:
    print(txt.group())  # abc
    print(txt.start())  # 3
    print(txt.end())  # 6
    print(txt.span())  # (3, 6)
else:
    print("找不到")

print("------------------------------------------------------------")  # 60個

text = "Do your best,\nGo Go Go!"
pattern = r".*"

print("無re.DOTALL")
txt = re.search(pattern, text)
print(txt.group())  # Do your best,

print("傳回搜尋含換列字元結果, re.DOTALL")
pattern = r".*"
txt = re.search(pattern, text, re.DOTALL)
print(txt.group())  # Do your best,\nGo Go Go!

print("------------------------------------------------------------")  # 60個


def searchStr(pattern, text):
    txt = re.search(pattern, text)
    if txt != None:
        print("搜尋成功 ", txt.group())
    else:
        print("搜尋失敗 ", txt)


text1 = "son"
text2 = "sonson"
text3 = "sonsonson"
text4 = "sonsonsonson"
text5 = "sonsonsonsonson"
pattern = "(son){3,5}"
searchStr(pattern, text1)
searchStr(pattern, text2)
searchStr(pattern, text3)
searchStr(pattern, text4)
searchStr(pattern, text5)

print("------------------------------------------------------------")  # 60個

text = "sonsonsonsonson"
pattern = "(son){3,5}"
txt = re.search(pattern, text)
if txt != None:
    print("搜尋成功 ", txt.group())
else:
    print("搜尋失敗 ", txt)

print("------------------------------------------------------------")  # 60個

text = "sonsonsonsonson"
pattern = "(son){3,5}?"  # 非貪婪模式, 多了一個?
txt = re.search(pattern, text)
if txt != None:
    print("搜尋成功 ", txt.group())
else:
    print("搜尋失敗 ", txt)

print("------------------------------------------------------------")  # 60個

text = "Name: Jiin-Kwei Hung Address: 8F, Nan-Jing E. Rd, Taipei"
pattern = "Name: (.*) Address: (.*)"
txt = re.search(pattern, text)  # 傳回搜尋結果
Name, Address = txt.groups()
print("Name:    ", Name)
print("Address: ", Address)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋除了換列字元以外字元
text = "Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei"
pattern = ".*"
txt = re.search(pattern, text)  # 傳回搜尋不含換列字元結果
print("測試1輸出: ", txt.group())

# 測試2搜尋包括換列字元
text = "Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei"
pattern = ".*"
print("傳回搜尋含換列字元結果, re.DOTALL")
txt = re.search(pattern, text, re.DOTALL)
print("測試2輸出: ", txt.group())


print("------------------------------------------------------------")  # 60個
# re.compile() + .findall() ST
print("------------------------------------------------------------")  # 60個

print("以下搜尋所有英文字母")
text = "tem12po"
pattern = r"[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt)  # ['tem', 'po']

text = "3tem12po"
pattern = r"[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt)  # ['tem', 'po']

text = "3tem12po"
pattern = r"[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt)  # ['tem', 'po']

text = "3tem12po"
pattern = r"[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則
txt = reobj.findall(text)
print(txt)  # ['tem', 'po']

print("------a")

text = "3tem12po"
pattern = r"[a-z]+"
txt = re.findall(pattern, text)
print(txt)  # ['tem', 'po']

text = "tem12po"
pattern = r"[a-z]+"
txt = re.findall(pattern, text)
print(txt)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個
# re.match() ST
print("------------------------------------------------------------")  # 60個

text = "tem12po"
pattern = r"[a-z]+"
txt = re.match(pattern, text)
print(txt)  # <re.Match object; span=(0, 3), match='tem'>

print("------------------------------------------------------------")  # 60個

text = "tem12po"
pattern = r"[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則
txt = reobj.match(text)

print(txt)  # <re.Match object; span=(0, 3), match='tem'>
if txt != None:
    print(txt.group())  # tem
    print(txt.start())  # 0
    print(txt.end())  # 3
    print(txt.span())  # (0,3)


print("------------------------------------------------------------")  # 60個

pattern = r"[a-z]+"
txt = re.match(pattern, "abc123xyz")
print(txt)
if txt != None:
    print(txt.group())  # abc
    print(txt.start())  # 0
    print(txt.end())  # 3
    print(txt.span())  # (0, 3)

print("------------------------------------------------------------")  # 60個

text1 = "123abcd456efghijk789123"
text2 = "abcd456efghijk789123abc"

print("match 找出從頭出現的英文字字串")
pattern = r"[a-z]+"
txt = re.match(pattern, text1)
print(txt)
if txt != None:
    print(txt.group())  # tem
    print(txt.start())  # 0
    print(txt.end())  # 3
    print(txt.span())  # (0, 3)
else:
    print("找不到")

pattern = r"[a-z]+"
txt = re.match(pattern, text2)
print(txt)
if txt != None:
    print(txt.group())  # tem
    print(txt.start())  # 0
    print(txt.end())  # 3
    print(txt.span())  # (0, 3)
else:
    print("找不到")

print("------------------------------------------------------------")  # 60個

# 測試1搜尋使用re.match()
text = "John will attend my party tonight."  # John是第一個字串
pattern = "John"
txt = re.match(pattern, text)  # 傳回搜尋結果
if txt != None:
    print("測試1輸出: ", txt.group())
else:
    print("測試1搜尋失敗")

# 測試2搜尋使用re.match()
text = "My best friend is John."  # John不是第一個字串
print("傳回搜尋含換列字元結果, re.DOTALL")
txt = re.match(pattern, text, re.DOTALL)  # 傳回搜尋結果
if txt != None:
    print("測試2輸出: ", txt.group())
else:
    print("測試2搜尋失敗")

print("------------------------------------------------------------")  # 60個

text = "tem12po"
pattern = "[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則

txt = reobj.match(text)
print(txt)  # <_sre.SRE_Match object; span=(0, 3), match='tem'>
if txt != None:
    print(txt.group())
    print(txt.start())
    print(txt.end())
    print(txt.span())

print("------------------------------------------------------------")  # 60個

text = "tem12po"
pattern = r"[a-z]+"
txt = re.match(pattern, text)

print(txt)  # <_sre.SRE_Match object; span=(0, 3), match='tem'>
if txt != None:
    print(txt.group())
    print(txt.start())
    print(txt.end())
    print(txt.span())

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# re.sub() 取代功能 ST
print("------------------------------------------------------------")  # 60個

text = "Password:1234,ID:5678"
pattern = r"\d+"
substr = "*"
txt = re.sub(pattern, substr, text)
print(txt)  # Password:*,ID:*
print("取代功能")
print("舊字串 :", text)
print("新字串 :", txt)

print("------------------------------------------------------------")  # 60個


def multiply(m):
    v = int(m.group())
    return str(v * 3)


print("只取代前5項")
text = "1 2 3 4 5 6 7 8 9 10"
txt = re.sub("\d+", multiply, text, 5)
print("取代功能")
print("舊字串 :", text)
print("新字串 :", txt)

print("------------------------------------------------------------")  # 60個

# 測試取代功能, 取代成功
text = "Python is good! I like Python."
pattern = "Python"  # 欲搜尋字串
newstr = "Java"  # 新字串
txt = re.sub(pattern, newstr, text)  # 如果找到則取代
if txt != text:  # 如果txt與text內容不同表示取代成功
    print("取代成功")
    print("舊字串 :", text)
    print("新字串 :", txt)
else:
    print("取代失敗: ", txt)  # 列出失敗取代結果

# 測試取代功能, 取代失敗
text = "Python is good! I like Python."
pattern = "C++"  # 欲搜尋字串
newstr = "Java"  # 新字串
txt = re.sub(pattern, newstr, text)  # 如果找到則取代
if txt != text:  # 如果txt與text內容不同表示取代成功
    print("取代成功")
    print("舊字串 :", text)
    print("新字串 :", txt)
else:
    print("取代失敗: ", txt)  # 列出失敗取代結果

print("------------------------------------------------------------")  # 60個

# 使用隱藏文字執行取代
text = "CIA Mark told CIA Linda that secret USB had given to CIA Peter."
pattern = r"CIA (\w)\w*"  # 欲搜尋CIA + 空一格後的名字
newstr = r"\1***"  # 新字串使用隱藏文字
txt = re.sub(pattern, newstr, text)  # 執行取代

print("取代功能")
print("舊字串 :", text)
print("新字串 :", txt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

text = "3tem12po"
pattern = "[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則

txt = reobj.search(text)

print(txt)  # <re.Match object; span=(1, 4), match='tem'>
if txt != None:
    print(txt.group())  # tem
    print(txt.start())  # 1
    print(txt.end())  # 4
    print(txt.span())  # (1,4)

print("------------------------------------------------------------")  # 60個

text = "3tem12po"
pattern = "[a-z]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則

txt = reobj.search(text)
print(txt)  # <_sre.SRE_Match object; span=(1, 4), match='tem'>
if txt != None:
    print(txt.group())  # tem
    print(txt.start())  # 1
    print(txt.end())  # 4
    print(txt.span())  # (1,4)

print("------------------------------------------------------------")  # 60個

text = "abc123xyz"
pattern = r"[a-z]+"
txt = re.findall(pattern, text)
print(txt)  # ['abc', 'xyz']
print("text :", text)
print("pattern :", pattern)
print("result :", txt)

print("------------------------------------------------------------")  # 60個

text = "Amy was 18 year old,she likes Python and C++."
pattern = r"[0-9+]+"
txt = re.findall(pattern, text)
print(txt)  # ['18', '++']
print("text :", text)
print("pattern :", pattern)
print("result :", txt)

print("------------------------------------------------------------")  # 60個

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
print("尋找 email")
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
for email in emails:
    print(email)

print("尋找 定價金額")
price = re.findall(r"[\d]+元", html)[0].split("元")[0]  # 價格
print(price)

print("尋找 圖片網址")
imglist = re.findall(r"[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+", html)
for img in imglist:  #
    print(img)

print("尋找 電話號碼")
texts = re.findall(r"\(?\d{2,4}\)?\-\d{6,8}", html)
for text in texts:
    print(text)

print("------------------------------------------------------------")  # 60個

text = "Do your best!"
pattern = r".o"

txt = re.findall(pattern, text)
print(txt)  # ['Do', 'yo']

txt = re.findall(r".*o", text)
print(txt)  # ['Do yo']

print("------------------------------------------------------------")  # 60個

text = "John is my best friend."
pattern = r"[aeiou]*"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則
txt = re.findall(reobj, text)
print(txt)

text = "John is my best friend."
pattern = r"[aeiou]+"
reobj = re.compile(pattern)  # compile() 建立一個正規表達式的規則
txt = re.findall(reobj, text)
print(txt)  # ['o', 'i', 'e', 'ie']

print("------------------------------------------------------------")  # 60個

text = "John was 18 year old."
pattern = r"[^a-z. ]+"
txt = re.findall(pattern, text)
print(txt)  # ['J', '18']

print("------------------------------------------------------------")  # 60個

text = "2020 is coming soon"
pattern = r"^\d+"

txt = re.findall(pattern, text)
print(txt)  # ['2020']

txt = re.findall(r"\w+$", text)
print(txt)  # ['soon']

print("------------------------------------------------------------")  # 60個

"""
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
"""
print("------------------------------------------------------------")  # 60個

text = "John and Tom will attend my party tonight. John is my best friend."

print("搜尋John或Tom")
pattern = "John|Tom"  # 搜尋John和Tom
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("搜尋Mary或Tom")
pattern = "Mary|Tom"  # 搜尋Mary和Tom
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

text = "john and TOM will attend my party tonight. JOHN is my best friend."

print("搜尋John或Tom, 忽略大小寫")
pattern = "John|Tom"  # 搜尋John和Tom
txt = re.findall(pattern, text, re.I)  # 傳回搜尋忽略大小寫的結果
print(txt)

print("搜尋Mary或Tom, 忽略大小寫")
pattern = "Mary|tom"  # 搜尋Mary和tom
txt = re.findall(pattern, text, re.I)  # 傳回搜尋忽略大小寫的結果
print(txt)

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 測試1將字串從句子分離
text = "John, Johnson, Johnnason and Johnnathan will attend my party tonight."
pattern = "\w+"  # 不限長度的單字
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試2將John開始的字串分離
text = "John, Johnson, Johnnason and Johnnathan will attend my party tonight."
pattern = "John\w*"  # John開頭的單字
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

text = "1 cat, 2 dogs, 3 pigs, 4 swans"
pattern = "\d+\s\w+"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋[aeiouAEIOU]字元
text = "John, Johnson, Johnnason and Johnnathan will attend my party tonight."
pattern = "[aeiouAEIOU]"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試2搜尋[2-5.]字元
text = "1. cat, 2. dogs, 3. pigs, 4. swans"
pattern = "[2-5.]"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋不在[aeiouAEIOU]的字元
text = "A party tonight."
pattern = "[^aeiouAEIOU]"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試2搜尋不在[2-5.]的字元
text = "2 dogs,3 pigs"
pattern = "[^2-5.]"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋John字串在最前面
text = "John will attend my party tonight."
pattern = "^John"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試2搜尋John字串不是在最前面
text = "My best friend is John"
pattern = "^John"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋最後字元是非英文字母數字和底線字元
text = "John will attend my party 28 tonight."
pattern = "\W$"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試2搜尋最後字元是非英文字母數字和底線字元
text = "I am 28"
pattern = "\W$"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試3搜尋最後字元是數字
text = "I am 28"
pattern = "\d$"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試4搜尋最後字元是數字
text = "I am 28 year old."
pattern = "\d$"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋開始到結尾皆是數字的字串
text = "09282028222"
pattern = "^\d+$"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

# 測試2搜尋開始到結尾皆是數字的字串
text = "0928tuyr990"
pattern = "^\d+$"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

text = "cat hat sat at matter flat"
pattern = ".at"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋使用re.match()
text = "John will attend my party tonight."
pattern = "John"
txt = re.match(pattern, text)  # re.match()
if txt != None:
    print("使用re.match()輸出MatchObject物件:  ", txt)
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())
else:
    print("測試1搜尋失敗")

# 測試2搜尋使用re.search()
text = "My best friend is John."
txt = re.search(pattern, text)  # re.search()
if txt != None:
    print("使用re.search()輸出MatchObject物件: ", txt)
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())
else:
    print("測試1搜尋失敗")

print("------------------------------------------------------------")  # 60個

text = """txt@deepmind.com.tw
         kkk@gmail.com,
         abc@aa
         abcdefg"""
pattern = r"""(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}                   # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4})?                # 國別
    )"""

print("有VERBOSE搜尋")
eMail = re.findall(pattern, text, re.VERBOSE)  # 傳回搜尋結果
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])

print("------------------------------------------------------------")  # 60個

print("檢查是否為合法的python檔案名")
ispythonprog = re.compile("^[a-zA-Z0-9_]+\.py$")  # compile() 建立一個正規表達式的規則


def ispython(name):
    return bool(ispythonprog.match(name))


short_filename = "picture1.jpg"
status = ispython(short_filename)
print("檔案名 :", short_filename, " ", status)

short_filename = "test10_new02.py"
status = ispython(short_filename)
print("檔案名 :", short_filename, " ", status)

print("------------------------------------------------------------")  # 60個

text = "Amy was 18 year old, she likes Python and C++."
pattern = r"[0-9+]+"
txt = re.findall(pattern, text)
print(txt)  # ['18', '++']

print("------------------------------------------------------------")  # 60個

print("搜尋, 忽略大小寫")
text = "I like Python and Android!"
pattern = r"PYTHON|ANDROID"
txt = re.findall(pattern, text, re.I)
print(txt)  # ['Python', 'Android']

print("------------------------------------------------------------")  # 60個

print("搜尋, 忽略大小寫")
text = "I like Python and Android!"
pattern = r"PYTHON|ANDROID"
txt = re.findall(pattern, text, re.I)
print(txt)  # ['Python', 'Android']
print("text :", text)
print("pattern :", pattern)
print("result :", txt)

print("------------------------------------------------------------")  # 60個


# 計算單字在文章中出現的頻率
# 只列出出現超過一次以上的單字

"""
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
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("找電話號碼")

texts = ["0412345678", "(04)12345678", "(04)-12345678", "(049)2987654", "0937-998877"]
pattern = r"""
 \(\d{2,4}\)-?\d{6,8} #(04)12345678、(04)-12345678、(049)2987654 等電話格式
|\d{9,10}             #0412345678 等含 9~10 位數字
|\d{4}-\d{6,8}        #0937-998877 等手機格式
"""

print("無VERBOSE搜尋")
for text in texts:
    txt = re.search(pattern, text)
    if txt != None:
        print(txt.group())

print("有VERBOSE搜尋")
for text in texts:
    txt = re.search(pattern, text, re.VERBOSE)
    if txt != None:
        print(txt.group())

print("------------------------------------------------------------")  # 60個


def isTaiwanPhone(str):
    if len(str) != 11:  # 如果長度不是11
        return False  # 傳回非手機號碼格式
    # 檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i == 4:
            if str[4] != "-":  # 如果第5個字元不是'-'字元
                return False  # 傳回非手機號碼格式
        else:  # 如果前4個字或最後6個字出現非數字字元
            if str[i].isdecimal() == False:
                return False  # 傳回非手機號碼格式
    return True  # 傳回是正確手機號碼格式


print("0937-123456 是台灣手機號碼：", isTaiwanPhone("0937-123456"))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone("02-12345678"))

print("------------------------------------------------------------")  # 60個

text = "tel:04-12345678"
pattern = r"(\d{2})-(\d{8})"

txt = re.search(pattern, text)
if txt != None:
    print(txt.group())  # 04-12345678
    print(txt.group(0))  # 04-12345678
    print(txt.group(1))  # 04
    print(txt.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

text = "tel:(04)12345678"
pattern = r"(\(\d{2}\))(\d{8})"

txt = re.search(pattern, text)
if txt != None:
    print(txt.group())  # (04)12345678
    print(txt.group(1))  # (04)
    print(txt.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

texts = ["(04)12345678", "(04)-12345678"]
pattern = r"(\(\d{2}\))-?(\d{8})"

for text in texts:
    txt = re.search(pattern, text)
    if txt != None:
        print(txt.group())

print("------------------------------------------------------------")  # 60個

texts = ["0412345678", "(04)12345678", "(04)-12345678", "(049)2987654", "0937-998877"]
pattern = r"\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}"

for text in texts:
    txt = re.search(pattern, text)
    if txt != None:
        print(txt.group())

print("------------------------------------------------------------")  # 60個

text = "543-87-3388"
pattern = "\d{3}-\d{2}-\d{4}"

txt = re.search(pattern, text)

if txt != None:
    print(text, " contains a SSN")
    print("start position of the matched text is " + str(txt.start()))
    print("start and end position of the matched text is " + str(txt.span()))
else:
    print(text, " does not contain a SSN")

print("------------------------------------------------------------")  # 60個

text = "543-87-3388"
pattern = "\d{3}-\d{2}-\d{4}"
txt = re.match(pattern, text)

if txt != None:
    print(text, " is a valid SSN")
    print("start position of the matched text is " + str(txt.start()))
    print("start and end position of the matched text is " + str(txt.span()))
else:
    print(text, " is not a valid SSN")

print("------------------------------------------------------------")  # 60個

text1 = "Please call me using 0930-919-919 or 0952-001-001"
text2 = "請明天17:30和我一起參加晚餐"
text3 = "請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我"


def parseText(text):
    """解析字串是否含有電話號碼"""
    pattern = r"\d\d\d\d-\d\d\d-\d\d\d"
    txt = re.search(pattern, text)
    if txt != None:  # 如果txt不是None表示取得號碼
        print(f"電話號碼是: {txt.group()}")
    else:
        print(f"{text} 字串不含電話號碼")


parseText(text1)
parseText(text2)
parseText(text3)

print("------------------------------------------------------------")  # 60個

text1 = "Please call me using 0930-919-919 or 0952-001-001"
text2 = "請明天17:30和我一起參加晚餐"
text3 = "請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我"


def parseText(text):
    """解析字串是否含有電話號碼"""
    pattern = r"\d\d\d\d-\d\d\d-\d\d\d"
    txt = re.findall(pattern, text)
    if txt != None:  # 如果txt不是None表示取得號碼
        print(f"電話號碼是: {txt}")
    else:
        print(f"{text} 字串不含電話號碼")


parseText(text1)
parseText(text2)
parseText(text3)

print("------------------------------------------------------------")  # 60個

text1 = "Please call me using 0930-919-919 or 0952-001-001"
text2 = "請明天17:30和我一起參加晚餐"
text3 = "請明天17:30和我一起參加晚餐, 可用0933-080-080聯絡我"


def parseText(text):
    """解析字串是否含有電話號碼"""
    pattern = r"\d{4}-\d{3}-\d{3}"
    txt = re.findall(pattern, text)  # 用串列傳回搜尋結果
    print(f"電話號碼是: {txt}")  # 串列方式顯示電話號碼


parseText(text1)
parseText(text2)
parseText(text3)

print("------------------------------------------------------------")  # 60個

text = "Please call my secretary using 02-26669999"
pattern = r"(\d{2})-(\d{8})"
txt = re.search(pattern, text)  # 傳回搜尋結果

print(f"完整號碼是: {txt.group()}")  # 顯示完整號碼
print(f"完整號碼是: {txt.group(0)}")  # 顯示完整號碼
print(f"區域號碼是: {txt.group(1)}")  # 顯示區域號碼
print(f"電話號碼是: {txt.group(2)}")  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個

text = "Please call my secretary using 02-26669999 or 02-11112222"
pattern = r"(\d{2})-(\d{8})"
txt = re.findall(pattern, text)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

text = "Please call my secretary using 02-26669999"
pattern = r"(\d{2})-(\d{8})"
txt = re.search(pattern, text)  # 傳回搜尋結果
areaNum, localNum = txt.groups()  # 留意是groups()
print(f"區域號碼是: {areaNum}")  # 顯示區域號碼
print(f"電話號碼是: {localNum}")  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個

text = "Please call my secretary using (02)-26669999"
pattern = r"(\(\d{2}\))-(\d{8})"
txt = re.search(pattern, text)  # 傳回搜尋結果
areaNum, localNum = txt.groups()  # 留意是groups()
print(f"區域號碼是: {areaNum}")  # 顯示區域號碼
print(f"電話號碼是: {localNum}")  # 顯示電話號碼


print("------------------------------------------------------------")  # 60個

msg = """txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         hung@gmail.com
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         service@deepwidsom.com
         mymail@yahoo.com
         de1988@kkk
         abcdefg"""
pattern = r"""(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )"""
eMail = re.findall(pattern, msg, re.VERBOSE)  # 傳回搜尋結果
for mail in eMail:
    print(mail[0])

print("------------------------------------------------------------")  # 60個

# 取出一段文字中的阿拉伯數字
a = "123 + 456"
b = re.findall(r"\d+", a.replace(" ", ""))
print(b)

# 取出一段文字中的「非」阿拉伯數字
c = "hello 123 !!!"
d = re.findall(r"\D+", c.replace(" ", ""))
print(d)

# 取出每個非空白字元
msg1 = "hello world!!"
msg1r = re.findall(r"\S", msg1)
print(msg1r)

# 替換指定區間文字
msg2 = "hello {name}, {age}"
msg2r = re.findall(r"\{.+?\}", msg2)
print(msg2r)
text = {"name": "oxxo", "age": "18"}
for i in range(0, len(msg2r)):
    o = re.sub(r"\{|\}", "", msg2r[i])
    msg2 = re.sub(msg2r[i], text[o], msg2)

print(msg2)

aa = "abc"
aa = aa + "def"
print(aa)

print("------------------------------------------------------------")  # 60個

"""
驗證輸入用戶名和QQ號是否有效并給出對應的提示信息
要求：
用戶名必須由字母、數字或下劃線構成且長度在6~20個字符之間
QQ號是5~12的數字且首位不能為0
"""
# username = input('請輸入用戶名: ')
username = "lion_mouse"
m1 = re.match(r"^[0-9a-zA-Z_]{6,20}$", username)
if not m1:
    print("請輸入有效的用戶名.")

# qq = input('請輸入QQ號: ')
qq = "12345678"
m2 = re.match(r"^[1-9]\d{4,11}$", qq)
if not m2:
    print("請輸入有效的QQ號.")
if m1 and m2:
    print("你輸入的信息是有效的!")


print("------------------------------------------------------------")  # 60個

# 用字串正規化分割字串為 list

sentence = "This,is a,test.sentence"
time_data = "2020/05/20_12:30:45"

print(re.split("[,. ]", sentence))  # 用逗點、句點和空格來分割字串
print(re.split("[/_:]", time_data))

print("------------------------------------------------------------")  # 60個


"""
def multiply(m):
    v = int(m.group())
    return str(v * 2)

def getVid(url):
    string strRegex = "(?<=id_)(\\w+)";
    Regex reg = new Regex(strRegex);
    Match match = reg.Match(url);
    return match.ToString();


print("正規表示式的使用")
url = "http://v.youku.com/v_show/id_XNzk2NTI0MzMy.html";
vid = getVid(url);
print("vid : " + vid)


print("取得email帳號")

#取得email帳號

senderEmail = @"david@insighteyes.com";
string[] sendFromUser = senderEmail.Split('@');
int len = sendFromUser.Length;
print("len = " + len.ToString())
int i;
for (i = 0; i < len; i++)
{
print("i = " + i.ToString() + "\t" + sendFromUser[i])
}


print("用Regular Expression拆解e-mail帳號")

List<string> emailList = new List<string>();
email = "xue@163.,xue@163.com12,2707@qq.com,,xue@yahoo.com.cn,xue@163.com,xue@163.com12";
#  Regex reg2 = new Regex(@"^\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,}$");驗證email的正則表達式  

Regex reg = new Regex(@"(?<email>[\da-zA-Z_]+@([-\dA-Za-z]+\.)+[a-zA-Z]{2,})");
Match m = reg.Match(email);
foreach (Match item in reg.Matches(email))
{
emailList.Add(item.Groups["email"].Value);
}
len = emailList.Count;
print("共取得 : " + len.ToString() + " 個帳號")
for (i = 0; i < len; i++)
{
print("i = " + i.ToString() + "\t" + emailList[i])
}
"""

print("正規表示式的使用")

"""
text = 'tem12po'
pattern = r'[a-z]+'
txt = re.match(pattern, text)
print(txt.group()) # <re.Match object; span=(0, 3), match='tem'>
"""

# 正規表示式的使用

# 正規表示式

# 使用方法
# Regex.Match("String", @"正規表示式").ToString();

text = "USA stands for the United States of America with 50 states and 330 millions people."

# text = 'tem12po'
# pattern = r'[a-z]+'
# txt = re.match(pattern, text)
# print(txt) # <re.Match object; span=(0, 3), match='tem'>


# 只提出字串最前面或最後面的英文
pattern = r"[A-Z]+"
txt = re.match(pattern, text)
print("結果 : ", txt.group())

# 只提出字串最前面或最後面的數字
pattern = r"[\d_]+"
txt = re.match(pattern, text)
print("ddd結果 : ", txt)

# 其他規則
text = "123ABC456DEF"
pattern = r"[A-Z]+[0-9]+"
txt = re.match(pattern, text)  # Output:"ABC456"
print("ddd結果 : ", txt)

text = "123ABC456DeF"
pattern = r"[0-9A-Z]+"
txt = re.match(pattern, text)  # Output:"123ABC456D"
print("結果 : ", txt.group())

text = "123ABC456DeF"
pattern = r"[0-9A-Za-z]+"
txt = re.match(pattern, text)  # Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "ABC123D"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)  # Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "ABC123"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)  # Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "123ABC456DEF"
pattern = r"[A-Z]+[0-9]+"
txt = re.match(pattern, text)  # Output:"123ABC456DeF"
print("ddd結果 : ", txt)

text = "123ABC"
pattern = r"\d"
txt = re.match(pattern, text)  # Output:"123ABC456DeF"
print("結果 : ", txt.group(), "\t數字")

text = "ABC 123"
pattern = r"[A-Z]+"
txt = re.match(pattern, text)  # Output:"123ABC456DeF"
print("結果 : ", txt.group())

text = "123ABC456-DeF"
pattern = r"[0-9A-Za-z\-]+"
txt = re.match(pattern, text)  # Output:"123ABC456DeF"
print("結果 : ", txt.group())

print("------------------------------------------------------------")  # 60個

print("檢查台灣手機號碼")
"""
text = "0922123456";

print("Text = " + text)
bool match;
match = System.Text.RegularExpressions.Regex.IsMatch(text, @"^09[0-9]{8}$");
if (match == true)
{
print("OK")
}
else
{
print("NG")
}


print("檢查中國手機號碼")

text = "13987654321";

print("Text = " + text)

if (!IsHandset(text))
{
print("NG")
}
else
{
print("OK")
}

print("檢查是否為數值")

text = "0x1234";

print("Text = " + text)

if (Regex.IsMatch(text, @"^[\d,\.]+$"))
{
print("是數值")
}
else
{
print("不是數值")
}
"""

print("------------------------------------------------------------")  # 60個

msg = "John and Tom will attend my party tonight. John is my best friend."
pattern = "John|Tom"  # 搜尋John和Tom
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
pattern = "Mary|Tom"  # 搜尋Mary和Tom
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)


print("------------------------------------------------------------")  # 60個

msg = "john and TOM will attend my party tonight. JOHN is my best friend."
pattern = "John|Tom"  # 搜尋John和Tom
txt = re.findall(pattern, msg, re.I)  # 傳回搜尋忽略大小寫的結果
print(txt)
pattern = "Mary|tom"  # 搜尋Mary和tom
txt = re.findall(pattern, msg, re.I)  # 傳回搜尋忽略大小寫的結果
print(txt)

print("------------------------------------------------------------")  # 60個


def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:  # 搜尋失敗
        print("搜尋失敗 ", txt)
    else:  # 搜尋成功
        print("搜尋成功 ", txt.group())


msg1 = "son"
msg2 = "sonson"
msg3 = "sonsonson"
msg4 = "sonsonsonson"
msg5 = "sonsonsonsonson"
pattern = "(son){3,5}"
searchStr(pattern, msg1)
searchStr(pattern, msg2)
searchStr(pattern, msg3)
searchStr(pattern, msg4)
searchStr(pattern, msg5)

print("------------------------------------------------------------")  # 60個


def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:  # 搜尋失敗
        print("搜尋失敗 ", txt)
    else:  # 搜尋成功
        print("搜尋成功 ", txt.group())


msg = "sonsonsonsonson"
pattern = "(son){3,5}"
searchStr(pattern, msg)

print("------------------------------------------------------------")  # 60個


def searchStr(pattern, msg):
    txt = re.search(pattern, msg)
    if txt == None:  # 搜尋失敗
        print("搜尋失敗 ", txt)
    else:  # 搜尋成功
        print("搜尋成功 ", txt.group())


msg = "sonsonsonsonson"
pattern = "(son){3,5}?"  # 非貪婪模式
searchStr(pattern, msg)

print("------------------------------------------------------------")  # 60個

# 測試1將字串從句子分離
msg = "John, Johnson, Johnnason and Johnnathan will attend my party tonight."
pattern = "\w+"  # 不限長度的單字
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試2將John開始的字串分離
msg = "John, Johnson, Johnnason and Johnnathan will attend my party tonight."
pattern = "John\w*"  # John開頭的單字
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

msg = "1 cat, 2 dogs, 3 pigs, 4 swans"
pattern = "\d+\s\w+"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋[aeiouAEIOU]字元
msg = "John, Johnson, Johnnason and Johnnathan will attend my party tonight."
pattern = "[aeiouAEIOU]"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試2搜尋[2-5.]字元
msg = "1. cat, 2. dogs, 3. pigs, 4. swans"
pattern = "[2-5.]"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋不在[aeiouAEIOU]的字元
msg = "John, Johnson, Johnnason and Johnnathan will attend my party tonight."
pattern = "[^aeiouAEIOU]"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試2搜尋不在[2-5.]的字元
msg = "1. cat, 2. dogs, 3. pigs, 4. swans"
pattern = "[^2-5.]"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋John字串在最前面
msg = "John will attend my party tonight."
pattern = "^John"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試2搜尋John字串不是在最前面
msg = "My best friend is John"
pattern = "^John"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個


def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 12:  # 如果長度不是12
        return False  # 傳回非手機號碼格式

    for i in range(0, 4):  # 如果前4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格式

    if string[4] != "-":  # 如果不是'-'字元
        return False  # 傳回非手機號碼格式

    for i in range(5, 8):  # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格

    if string[8] != "-":  # 如果不是'-'字元
        return False  # 傳回非手機號碼格式

    for i in range(9, 12):  # 如果最後3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False  # 傳回非手機號碼格
    return True  # 通過以上測試


def parseString(string):
    """解析字串是否含有電話號碼"""
    notFoundSignal = True  # 註記沒有找到電話號碼為True
    for i in range(len(string)):  # 用迴圈逐步抽取12個字元做測試
        msg = string[i : i + 12]
        if taiwanPhoneNum(msg):
            print(f"電話號碼是: {msg}")
            notFoundSignal = False
    if notFoundSignal:  # 如果沒有找到電話號碼則列印
        print(f"{string} 字串不含電話號碼")


msg1 = "Please call my secretary using 0930-919-919 or 0952-001-001"
msg2 = "請明天17:30和我一起參加明志科大教師節晚餐"
msg3 = "請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我"
parseString(msg1)
parseString(msg2)
parseString(msg3)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋最後字元是非英文字母數字和底線字元
msg = "John will attend my party 28 tonight."
pattern = "\W$"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試2搜尋最後字元是非英文字母數字和底線字元
msg = "I am 28"
pattern = "\W$"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試3搜尋最後字元是數字
msg = "I am 28"
pattern = "\d$"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試4搜尋最後字元是數字
msg = "I am 28 year old."
pattern = "\d$"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋開始到結尾皆是數字的字串
msg = "09282028222"
pattern = "^\d+$"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)
# 測試2搜尋開始到結尾皆是數字的字串
msg = "0928tuyr990"
pattern = "^\d+$"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

msg = "cat hat sat at matter flat"
pattern = ".at"
txt = re.findall(pattern, msg)  # 傳回搜尋結果
print(txt)

print("------------------------------------------------------------")  # 60個

msg = "Name: Jiin-Kwei Hung Address: 8F, Nan-Jing E. Rd, Taipei"
pattern = "Name: (.*) Address: (.*)"
txt = re.search(pattern, msg)  # 傳回搜尋結果
Name, Address = txt.groups()
print("Name:    ", Name)
print("Address: ", Address)

print("------------------------------------------------------------")  # 60個

# 測試1搜尋除了換列字元以外字元
msg = "Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei"
pattern = ".*"
txt = re.search(pattern, msg)  # 傳回搜尋不含換列字元結果
print("測試1輸出: ", txt.group())
# 測試2搜尋包括換列字元
msg = "Name: Jiin-Kwei Hung \nAddress: 8F, Nan-Jing E. Rd, Taipei"
pattern = ".*"
txt = re.search(pattern, msg, re.DOTALL)  # 傳回搜尋含換列字元結果
print("測試2輸出: ", txt.group())

print("------------------------------------------------------------")  # 60個

# 測試1搜尋使用re.match()
msg = "John will attend my party tonight."  # John是第一個字串
pattern = "John"
txt = re.match(pattern, msg)  # 傳回搜尋結果
if txt != None:
    print("測試1輸出: ", txt.group())
else:
    print("測試1搜尋失敗")
# 測試2搜尋使用re.match()
msg = "My best friend is John."  # John不是第一個字串
txt = re.match(pattern, msg, re.DOTALL)  # 傳回搜尋結果
if txt != None:
    print("測試2輸出: ", txt.group())
else:
    print("測試2搜尋失敗")

print("------------------------------------------------------------")  # 60個

# 測試1搜尋使用re.match()
msg = "John will attend my party tonight."
pattern = "John"
txt = re.match(pattern, msg)  # re.match()
if txt != None:
    print("使用re.match()輸出MatchObject物件:  ", txt)
else:
    print("測試1搜尋失敗")
# 測試1搜尋使用re.search()
txt = re.search(pattern, msg)  # re.search()
if txt != None:
    print("使用re.search()輸出MatchObject物件: ", txt)
else:
    print("測試1搜尋失敗")

print("------------------------------------------------------------")  # 60個

# 測試1搜尋使用re.match()
msg = "John will attend my party tonight."
pattern = "John"
txt = re.match(pattern, msg)  # re.match()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())
# 測試2搜尋使用re.search()
msg = "My best friend is John."
txt = re.search(pattern, msg)  # re.search()
if txt != None:
    print("搜尋成功字串的起始索引位置 :  ", txt.start())
    print("搜尋成功字串的結束索引位置 :  ", txt.end())
    print("搜尋成功字串的結束索引位置 :  ", txt.span())

print("------------------------------------------------------------")  # 60個

# 測試1取代使用re.sub()結果成功
msg = "Eli Nan will attend my party tonight. My best friend is Eli Nan"
pattern = "Eli Nan"  # 欲搜尋字串
newstr = "Kevin Thomson"  # 新字串
txt = re.sub(pattern, newstr, msg)  # 如果找到則取代
if txt != msg:  # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)  # 列出成功取代結果
else:
    print("取代失敗: ", txt)  # 列出失敗取代結果
# 測試2取代使用re.sub()結果失敗
pattern = "Eli Thomson"  # 欲搜尋字串
txt = re.sub(pattern, newstr, msg)  # 如果找到則取代
if txt != msg:  # 如果txt與msg內容不同表示取代成功
    print("取代成功: ", txt)  # 列出成功取代結果
else:
    print("取代失敗: ", txt)  # 列出失敗取代結果

print("------------------------------------------------------------")  # 60個

# 使用隱藏文字執行取代
msg = "CIA Mark told CIA Linda that secret USB had given to CIA Peter."
pattern = r"CIA (\w)\w*"  # 欲搜尋CIA + 空一格後的名字
newstr = r"\1***"  # 新字串使用隱藏文字
txt = re.sub(pattern, newstr, msg)  # 執行取代
print("取代成功: ", txt)  # 列出取代結果

print("------------------------------------------------------------")  # 60個

msg1 = "Please call my secretary using 0930-919-919 or 0952-001-001"
msg2 = "請明天17:30和我一起參加明志科大教師節晚餐"
msg3 = "請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我"


def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r"\d\d\d\d-\d\d\d-\d\d\d"
    phoneNum = re.search(pattern, string)
    if phoneNum != None:  # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum.group()}")
    else:
        print(f"{string} 字串不含電話號碼")


parseString(msg1)
parseString(msg2)
parseString(msg3)

print("------------------------------------------------------------")  # 60個

msg = """02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        1234567899999,
        02 33887766 ext. 1234,
        02 33887799 ext. 12345,
        12345,
        123"""
pattern = r"""(
    (\d{2}|\(\d{2}\))?              # 區域號碼
    (\s|-)?                         # 區域號碼與電話號碼的分隔符號
    \d{8}                           # 電話號碼
    (\s*(ext|ext.)\s*\d{2,4})?      # 2-4位數的分機號碼
    )"""
phoneNum = re.findall(pattern, msg, re.VERBOSE)  # 傳回搜尋結果
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])

print("------------------------------------------------------------")  # 60個

msg = """02-88223349,
        (02)-26669999,
        02-29998888 ext 123,
        1234567899999,
        02 33887766 ext. 1234,
        02 33887799 ext. 12345,
        12345,
        123"""
pattern = r"""(
    (\d{2}|\(\d{2}\))?              # 區域號碼
    (\s|-)?                         # 區域號碼與電話號碼的分隔符號
    \b\d{8}\b                       # 電話號碼
    (\s*(ext|ext.)\s*\d{2,4}\b)?    # 2-4位數的分機號碼
    )"""
phoneNum = re.findall(pattern, msg, re.VERBOSE)  # 傳回搜尋結果
print("以下是符合的電話號碼")
for num in phoneNum:
    print(num[0])

print("------------------------------------------------------------")  # 60個

msg = """txt@deepwisdom.comyyy.twkkk,
         ser@deepmind.com.tw,
         aaa@gmail.comcomkk,
         kkk@gmail.com,
         abc@aa,
         abcdefg"""
pattern = r"""(
    [a-zA-Z0-9_.]+                  # 使用者帳號
    @                               # @符號
    [a-zA-Z0-9-.]+                  # 主機域名domain
    [\.]                            # .符號
    [a-zA-Z]{2,4}\b                 # 可能是com或edu或其它
    ([\.])?                         # .符號, 也可能無特別是美國
    ([a-zA-Z]{2,4}\b)?              # 國別
    )"""
eMail = re.findall(pattern, msg, re.VERBOSE)  # 傳回搜尋結果
print("以下是符合的電子郵件地址")
for mail in eMail:
    print(mail[0])

print("------------------------------------------------------------")  # 60個


# 定義一個函數用於重命名檔案串列
def rename_files(files):
    # 定義正則表達式模式匹配檔案名的一部分
    # (\w+)   匹配一個或多個單詞字元(字母、數字或底線)
    # (\d{4}) 匹配四位數字 (代表年份)
    # (\d{2}) 匹配兩位數字 (代表月份)
    pattern = r"(\w+)_(\d{4})_(\d{2})"
    for file in files:  # 遍歷檔案串列
        # 使用 sub() 函數替換匹配的名稱
        # \1, \2, \3 分別對應第一、第二、第三個捕獲組匹配的內容
        # 這裡將 底線( _ ) 替換為 ( - )
        new_name = re.sub(pattern, r"\1-\2-\3", file)
        print(f"Old : {file},   New: {new_name}")  # 輸出舊和新檔名


# 檔案名稱串列
files = ["report_2023_04.pdf", "report_2023_05.pdf", "summary_2023_04.docx"]

rename_files(files)  # 呼叫函數, 傳入檔案名稱串列

# 輸出
# Old: report_2023_04.pdf,  New: report-2023-04.pdf
# Old: report_2023_05.pdf,  New: report-2023-05.pdf
# Old: summary_2023_04.docx,  New: summary-2023-04.docx

print("------------------------------------------------------------")  # 60個


def validate_and_format_credit_card(number):
    # 定義Visa信用卡號碼的正則表達式, Visa卡號以4開頭, 並有16位數字
    pattern = r"^(?:4[0-9]{12}(?:[0-9]{3})?)$"

    # 使用match方法檢查提供的卡號是否符合正則表達式模式。
    match = re.match(pattern, number)
    if match:
        # 如果匹配成功，使用findall方法分組每四位數字
        # 然後用join方法將這些組用 "-" 連接成一個格式化的字串
        formatted = "-".join(re.findall(r"....", number))
        return True, formatted  # 返回一個元組和驗證成功格式化的卡號
    return False, None  # 如果匹配不成功, 返回False和None


# 測試卡號
card_number = "4111111111111111"
is_valid, formatted = validate_and_format_credit_card(card_number)
print(is_valid, formatted)  # 輸出結果應該為True和格式化後的卡號

print("------------------------------------------------------------")  # 60個


def clean_text(text):
    # 刪除不可列印字元和特殊符號, 只保留字母、數字和空格
    pattern = r"[^\w\s]"
    cleaned_text = re.sub(pattern, "", text)
    return cleaned_text


dirty_data = "Name: John Doe; Age: 30; %Salary: $5000"
print(clean_text(dirty_data))
# 輸出: Name John Doe Age 30 Salary 5000

print("------------------------------------------------------------")  # 60個

msg1 = "Please call my secretary using 0930-919-919 or 0952-001-001"
msg2 = "請明天17:30和我一起參加明志科大教師節晚餐"
msg3 = "請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我"


def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r"\d\d\d\d-\d\d\d-\d\d\d"
    phoneNum = re.findall(pattern, string)
    if phoneNum != None:  # 如果phoneNum不是None表示取得號碼
        print(f"電話號碼是: {phoneNum}")
    else:
        print(f"{string} 字串不含電話號碼")


parseString(msg1)
parseString(msg2)
parseString(msg3)

print("------------------------------------------------------------")  # 60個

msg1 = "Please call my secretary using 0930-919-919 or 0952-001-001"
msg2 = "請明天17:30和我一起參加明志科大教師節晚餐"
msg3 = "請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我"


def parseString(string):
    """解析字串是否含有電話號碼"""
    pattern = r"\d{4}-\d{3}-\d{3}"
    phoneNum = re.findall(pattern, string)  # 用串列傳回搜尋結果
    print(f"電話號碼是: {phoneNum}")  # 串列方式顯示電話號碼


parseString(msg1)
parseString(msg2)
parseString(msg3)

print("------------------------------------------------------------")  # 60個

msg = "Please call my secretary using 02-26669999"
pattern = r"(\d{2})-(\d{8})"
phoneNum = re.search(pattern, msg)  # 傳回搜尋結果

print(f"完整號碼是: {phoneNum.group()}")  # 顯示完整號碼
print(f"完整號碼是: {phoneNum.group(0)}")  # 顯示完整號碼
print(f"區域號碼是: {phoneNum.group(1)}")  # 顯示區域號碼
print(f"電話號碼是: {phoneNum.group(2)}")  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個

msg = "Please call my secretary using 02-26669999 or 02-11112222"
pattern = r"(\d{2})-(\d{8})"
phoneNum = re.findall(pattern, msg)  # 傳回搜尋結果
print(phoneNum)

print("------------------------------------------------------------")  # 60個

msg = "Please call my secretary using 02-26669999"
pattern = r"(\d{2})-(\d{8})"
phoneNum = re.search(pattern, msg)  # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()  # 留意是groups()
print(f"區域號碼是: {areaNum}")  # 顯示區域號碼
print(f"電話號碼是: {localNum}")  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個

msg = "Please call my secretary using (02)-26669999"
pattern = r"(\(\d{2}\))-(\d{8})"
phoneNum = re.search(pattern, msg)  # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()  # 留意是groups()
print(f"區域號碼是: {areaNum}")  # 顯示區域號碼
print(f"電話號碼是: {localNum}")  # 顯示電話號碼


print("------------------------------------------------------------")  # 60個

foldername = "data"
files = os.listdir(foldername)
txtList = []
# 測試1
pattern = "(.*).txt"
print("列印*.txt")
for filename in files:
    # print(filename)
    fnresult = re.search(pattern, filename)  # 傳回搜尋結果
    if fnresult != None:
        txtList.append(filename)
print(txtList)

pyList = []
# 測試2
print("列印ch14_10.py - ch14_19.py")
pattern = "(ch14_1(\d).py)"
for filename in files:
    fnresult = re.search(pattern, filename)  # 傳回搜尋結果
    if fnresult != None:
        pyList.append(filename)
print(pyList)

print("------------------------------------------------------------")  # 60個

text = "這個是、那個是、那個是、哪個是"
word1 = "這.是"
word2 = ".個是"

pattern = re.compile(word1)
count = len(re.findall(pattern, text))
print(word1, ":", count, "個")

pattern = re.compile(word2)
count = len(re.findall(pattern, text))
print(word2, ":", count, "個")

print("------------------------------------------------------------")  # 60個

text = "這個是測試資料。"
word1 = ".個是"
word2 = "那個是"

print("置換前 :", text)
pattern = re.compile(word1)
text = re.sub(pattern, word2, text)
print("置換後 :", text)


print("------------------------------------------------------------")  # 60個

# 要轉換的字串
text = """請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
"""

# 取得中文字和英文單字的正規表達式
# [a-zA-Z0-9]+ 表示開頭是英文字母後面連接一串字母或數字
regex = re.compile(r"[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+")

# 根據正規表達式，將每個中文字、標點符號和英文單字變成串列
arr = re.findall(regex, text)

# 使用空格合併串列
text = " ".join(arr)
print(text)

"""
請 求 您 幫 我 oxxo . studio 去 除 空 白 ok ？
但 是 要 保 留 換 行 可 以 嗎 ， ( 哈 哈 哈 ) ( 啊 哈 )
統 一 便 利 超 商 ( 711 ) 的 括 號 之 間 也 要 有 空 白 喔 ！
寫 作 規 範 就 是 這 麼 100 % 的 龜 毛 ～
"""

print("------------------------------------------------------------")  # 60個

# 輸入字符串
text = """請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
"""

regex = re.compile(r"[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+")
arr = re.findall(regex, text)
text = " ".join(arr)

regex = re.compile(r"(?<=[^a-zA-Z0-9\u0021-\u002E])(\x20)(?=[^a-zA-Z0-9\u0021-\u002E])")
text = re.sub(regex, "", text)

regex = re.compile(r"(\x20)(?=[\(\%\uFF00-\uFFFF])")
text = re.sub(regex, "", text)

text = text.replace(" . ", ".")
print(text)

print("------------------------------------------------------------")  # 60個

print(re.match(r"pyt", "python"))  # pyt 由開頭即符合, 因此成功
print(re.match(r"yth", "python"))  # yth 與開頭不符合, 因此失敗
print(re.search(r"yth", "python"))  # seach( ) 不限開頭, 因此成功

print("------------------------------------------------------------")  # 60個

m = re.search(r"p[a-z]+e", "apples")
print(m)  # 輸出 <_sre.SRE_Match object; span=(1, 5), match='pple'>
print(m.group())  # 輸出 pple
print(m.start())  # 輸出 1
print(m.end())  # 輸出 5 注意！pple 的位置是 1~4
print(m.span())  # 輸出 (1, 5)

print("------------------------------------------------------------")  # 60個

# bracket

pat = r"[0-9+]+"
s = "Amy was 18 year old,she likes Python and C++."
m = re.findall(pat, s)
print(m)  # ['18', '++']

print("------------------------------------------------------------")  # 60個

# compile

reobj = re.compile(r"[a-z]+")
m = reobj.findall("3tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# dotall

pat = r".*"
s = "Do your best,\nGo Go Go!"
m = re.search(pat, s)
print(m.group())  # Do your best,
m2 = re.search(r".*", s, re.DOTALL)
print(m2.group())  # Do your best,\nGo Go Go!

print("------------------------------------------------------------")  # 60個

# findall

pat = re.compile("[a-z]+")
m = pat.findall("tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# ignore

pat = r"PYTHON|ANDROID"
s = "I like Python and Android!"
m = re.findall(pat, s, re.I)
print(m)  # ['Python', 'Android']

print("------------------------------------------------------------")  # 60個

# match

pat = re.compile(r"[a-z]+")

m = pat.match("tem12po")
print(m)  # <re.Match object; span=(0, 3), match='tem'>
if not m == None:
    print(m.group())  # tem
    print(m.start())  # 0
    print(m.end())  # 3
    print(m.span())  # (0,3)

print("------------------------------------------------------------")  # 60個

# not1

pat = r"[^a-z. ]+"
s = "John was 18 year old."
m = re.findall(pat, s)
print(m)  # ['J', '18']

print("------------------------------------------------------------")  # 60個

# not2

pat = r"^\d+"
s = "2020 is coming soon"
m = re.findall(pat, s)
print(m)  # ['2020']
m2 = re.findall(r"\w+$", s)
print(m2)  # ['soon']

print("------------------------------------------------------------")  # 60個

# phone_check


def isTaiwanPhone(str):
    if len(str) != 11:  # 如果長度不是11
        return False  # 傳回非手機號碼格式
    # 檢查11個字元是否符合手機號碼格式
    for i in range(0, 11):
        if i == 4:
            if str[4] != "-":  # 如果第5個字元不是'-'字元
                return False  # 傳回非手機號碼格式
        else:  # 如果前4個字或最後6個字出現非數字字元
            if str[i].isdecimal() == False:
                return False  # 傳回非手機號碼格式
    return True  # 傳回是正確手機號碼格式


print("0937-123456 是台灣手機號碼：", isTaiwanPhone("0937-123456"))
print("02-12345678 是台灣手機號碼：", isTaiwanPhone("02-12345678"))

print("------------------------------------------------------------")  # 60個

# phone1

numStr = "tel:04-12345678"
pat = r"(\d{2})-(\d{8})"

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())  # 04-12345678
    print(phone.group(0))  # 04-12345678
    print(phone.group(1))  # 04
    print(phone.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

# phone2

numStr = "tel:(04)12345678"
pat = r"(\(\d{2}\))(\d{8})"

phone = re.search(pat, numStr)
if not phone == None:
    print(phone.group())  # (04)12345678
    print(phone.group(1))  # (04)
    print(phone.group(2))  # 12345678

print("------------------------------------------------------------")  # 60個

# phone3

phoneList = ["(04)12345678", "(04)-12345678"]
pat = r"(\(\d{2}\))-?(\d{8})"

for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# phone4

phoneList = [
    "0412345678",
    "(04)12345678",
    "(04)-12345678",
    "(049)2987654",
    "0937-998877",
]
pat = r"\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}"
for phone in phoneList:
    phoneNum = re.search(pat, phone)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# plus

pat = re.compile(r"[aeiou]+")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)  # ['o', 'i', 'e', 'ie']

print("------------------------------------------------------------")  # 60個

# re_findall

m = re.findall(r"[a-z]+", "tem12po")
print(m)  # ['tem', 'po']

print("------------------------------------------------------------")  # 60個

# re_match

pat = r"[a-z]+"
m = re.match(pat, "tem12po")
print(m)  # <re.Match object; span=(0, 3), match='tem'>

print("------------------------------------------------------------")  # 60個

# re_search

pat = "[a-z]+"
m = re.search(pat, "3tem12po")
print(m)  # <re.Match object; span=(1, 4), match='tem'>

print("------------------------------------------------------------")  # 60個

# re_verbose

phoneList = [
    "0412345678",
    "(04)12345678",
    "(04)-12345678",
    "(049)2987654",
    "0937-998877",
]
pat = r"""
 \(\d{2,4}\)-?\d{6,8} #(04)12345678、(04)-12345678、(049)2987654 等電話格式
|\d{9,10}             #0412345678 等含 9~10 位數字
|\d{4}-\d{6,8}        #0937-998877 等手機格式
"""

for phone in phoneList:
    phoneNum = re.search(pat, phone, re.VERBOSE)
    if not phoneNum == None:
        print(phoneNum.group())

print("------------------------------------------------------------")  # 60個

# regex

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

emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html)
for email in emails:  # 顯示 email
    print(email)

price = re.findall(r"[\d]+元", html)[0].split("元")[0]  # 價格
print(price)  # 顯示定價金額

imglist = re.findall(r"[http://]+[a-zA-Z0-9-/.]+\.[jpgpng]+", html)
for img in imglist:  #
    print(img)  # 顯示圖片網址

phonelist = re.findall(r"\(?\d{2,4}\)?\-\d{6,8}", html)
for phone in phonelist:
    print(phone)  # 顯示電話號碼

print("------------------------------------------------------------")  # 60個

# search

pat = re.compile("[a-z]+")

m = pat.search("3tem12po")
print(m)  # <re.Match object; span=(1, 4), match='tem'>
if not m == None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())  # 4
    print(m.span())  # (1,4)

print("------------------------------------------------------------")  # 60個

# star

pat = re.compile(r"[aeiou]*")
s = "John is my best friend."
m = re.findall(pat, s)
print(m)

print("------------------------------------------------------------")  # 60個

# sub1

pat = r"\d+"
substr = "*"
s = "Password:1234,ID:5678"
result = re.sub(pat, substr, s)
print(result)  # Password:*,ID:*

print("------------------------------------------------------------")  # 60個

# sub2


def multiply(m):
    v = int(m.group())
    return str(v * 2)


result = re.sub("\d+", multiply, "10 20 30 40 50", 3)
print(result)  # 20 40 60 40 50

print("------------------------------------------------------------")  # 60個

# wild

pat = r".o"
s = "Do your best!"
m = re.findall(pat, s)
print(m)  # ['Do', 'yo']
m2 = re.findall(r".*o", s)
print(m2)  # ['Do yo']

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
