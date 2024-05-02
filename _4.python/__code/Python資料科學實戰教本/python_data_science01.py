"""
Python資料科學實戰教本



"""


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

a = True
b = False
print(type(a)) # 顯示 "<class 'bool'>"
print(a and b) # 邏輯AND: 顯示 "False"
print(a or b)  # 邏輯OR: 顯示"True"
print(not a)   # 邏輯NOT: 顯示 "False"

print("------------------------------------------------------------")  # 60個

s = "hello"
print(s.capitalize())  # 第1個字元大寫: 顯示 "Hello"
print(s.upper())       # 轉成大寫: 顯示 "HELLO"
print(s.rjust(7))      # 右邊填空白字元: 顯示 "  hello"
print(s.center(7))     # 置中顯示: 顯示 " hello "
print(s.replace('l', 'L'))  # 取代字串: 顯示 "heLLo"
print('  python '.strip())  # 刪除空白字元: 顯示 "python"

print("------------------------------------------------------------")  # 60個

# 擁有1個參數的range()函數
for i in range(5):
    print("range(5)的值 = " + str(i))
for i in range(10):
    print("range(10)的值 = " + str(i))
for i in range(11):
    print("range(11)的值 = " + str(i))
# 擁有2個參數的range()函數
for i in range(1, 5):
    print("range(1,5)的值 = " + str(i))
for i in range(1, 10):
    print("range(1,10)的值 = " + str(i))
for i in range(1, 11):
    print("range(1,11)的值 = " + str(i))
# 擁有3個參數的range()函數
for i in range(1, 11, 2):
    print("range(1,11,2)的值 = " + str(i))
for i in range(1, 11, 3):
    print("range(1,11,3)的值 = " + str(i))
for i in range(1, 11, 4):
    print("range(1,11,4)的值 = " + str(i))
for i in range(0, -10, -1):
    print("range(0,-10,-1)的值 = " + str(i))
for i in range(0, -10, -2):
    print("range(0,-10,-2)的值 = " + str(i))
    
print("------------------------------------------------------------")  # 60個

# 定義函數
def print_msg():
    print("歡迎學習Python程式設計!")

def is_valid_num(no):
    if no >= 0 and no <= 200.0:
        return True
    else:
        return False

def convert_to_f(c):
    f = (9.0 * c) / 5.0 + 32.0
    return f
# 函數呼叫
print_msg()
c = 100
f = convert_to_f(c)
print("華氏: " + str(f))
if is_valid_num(c):
    print("合法!")
else:
    print("不合法")

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)

print("------------------------------------------------------------")  # 60個

try: 
    fp = open("myfile.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("錯誤: myfile.txt檔案不存在!")


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1.py

ls = [6, 4, 5]    # 建立清單
print(ls, ls[2])  # 顯示 "[6, 4, 5] 5"
print(ls[-1])     # 負索引從最後開始: 顯示 "5"
ls[2] = "py"      # 指定字串型態的項目
print(ls)         # 顯示 "[6, 4, 'py']"
ls.append("bar")  # 新增項目
print(ls)         # 顯示 "[6, 4, 'py', 'bar']"
ele = ls.pop()    # 取出最後項目
print(ele, ls)    # 顯示 "bar [6, 4, 'py']"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1a.py

nums = list(range(5))  # 建立一序列的整數清單
print(nums)            # 顯示 "[0, 1, 2, 3, 4]"
print(nums[2:4])       # 切割索引2~4(不含4): 顯示 "[2, 3]"
print(nums[2:])        # 切割索引從2至最後: 顯示 "[2, 3, 4]"
print(nums[:2])        # 切割從開始至索引2(不含2): 顯示 "[0, 1]"
print(nums[:])         # 切割整個清單: 顯示 "[0, 1, 2, 3, 4]"
print(nums[:-1])       # 使用負索引切割: 顯示 "[0, 1, 2, 3]"
nums[2:4] = [7, 8]     # 使用切割來指定子清單
print(nums)            # 顯示 "[0, 1, 8, 9, 4]"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1b.py

print("走訪顯示串列的每一個項目...")
animals = ['cat', 'dog', 'bat']
for animal in animals:
    print(animal)

print("走訪顯示串列的每一個項目和索引值...")
animals = ['cat', 'dog', 'bat']
for index, animal in enumerate(animals):
    print(index, animal)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-1c.py

list1 = [x for x in range(10)]
print("[x for x in range(10)]")
print(str(list1))
list2 = [x+1 for x in range(10)]
print("[x+1 for x in range(10)]")
print(str(list2))
list3 = [x for x in range(10) if x % 2 == 0]
print("[x for x in range(10) if x%2==0]")
print(str(list3))
list4 = [x*2 for x in range(10) if x % 2 == 0]
print("[x*2 for x in range(10) if x%2==0]")
print(str(list4))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-2.py

d = {"cat": "white", "dog": "black"}  # 建立字典
print(d["cat"])       # 使用Key取得項目: 顯示 "white"
print("cat" in d)     # 是否有Key: 顯示 "True"
d["pig"] = "pink"     # 新增項目
print(d["pig"])       # 顯示 "pink"
print(d.get("monkey", "N/A"))  # 取出項目+預設值: 顯示 "N/A"
print(d.get("pig", "N/A"))     # 取出項目+預設值: 顯示 "pink"
del d["pig"]          # 使用Key刪除項目
print(d.get("pig", "N/A"))     # "pig"不存在: 顯示 "N/A"


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-2a.py

print("以鍵來走訪字典...")
d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal in d:
    legs = d[animal]
    print(animal, legs)
print("走訪字典的鍵和值...")
d = {"chicken": 2, "dog": 4, "cat": 4, "spider": 8}
for animal, legs in d.items():
    print("動物: %s 有 %d 隻腳" % (animal, legs))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-2b.py

d1 = {x:x*x for x in range(10)}
print("{x:x*x for x in range(10)}")
print(str(d1))
d2 = {x:x*x for x in range(10) if x % 2 == 1}
print("{x:x*x for x in range(11) if x%2==1}")
print(str(d2))



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-3.py

animals = {"cat", "dog", "pig"} # 建立集合
print("cat" in animals)   # 檢查是否有此元素: 顯示 "True"
print("fish" in animals)  # 顯示 "False"
animals.add("fish")       # 新增集合元素
print("fish" in animals)  # 顯示 "True"
print(len(animals))       # 元素數: 顯示 "4"
animals.add("cat")        # 新增存在的元素
print(len(animals))       # 顯示 "4"
animals.remove('cat')     # 刪除集合元素
print(len(animals))       # 顯示 "3"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-3a.py

animals = {"cat", "dog", "pig", "fish"} # 建立集合
for index, animal in enumerate(animals):
    print('#%d: %s' % (index + 1, animal))




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-3b.py

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("A = " + str(A))
print("B = " + str(B))
# 交集
C = A & B
print("A & B = " + str(C))
C = A.intersection(B)
print("A.intersection(B) = " + str(C))
# 聯集
C = A | B
print("A | B = " + str(C))
C = A.union(B)
print("A.union(B) = " + str(C))
# 差集
C = A - B
print("A - B = " + str(C))
C = A.difference(B)
print("A.difference(B) = " + str(C))
# 對稱差集
C = A ^ B
print("A ^ B = " + str(C))
C = A.symmetric_difference(B)
print("A.symmetric_difference(B) = " + str(C))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-5-4.py

t = (5, 6, 7, 8)  # 建立元組
print(type(t))    # 顯示 "<class 'tuple'>"
print(t)          # 顯示 "(5, 6, 7, 8)"
print(t[0])       # 顯示 "5"
print(t[1])       # 顯示 "6"
print(t[-1])      # 顯示 "8"
print(t[-2])      # 顯示 "7"
for ele in t:     # 走訪項目
    print(ele, end=" ")  # 顯示 "5, 6, 7, 8"



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-6-1.py

# 定義Student類別
class Student:
    # 建構子
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    # 方法
    def displayStudent(self):
        print("姓名 = " + self.name)
        print("成績 = " + str(self.grade))
        
    def whoami(self):
        return self.name

# 使用類別建立物件
s1 = Student("陳會安", 85)
s1.displayStudent()  # 呼叫方法
print("s1.whoami() = " + s1.whoami())
# 存取資料欄位
print("s1.name = " + s1.name)
print("s1.grade = " + str(s1.grade))

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch02\ch2-6-2.py

# 定義Student類別
class Student:
    # 建構子
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    # 方法
    def displayStudent(self):
        print("姓名 = " + self.name)
        print("成績 = " + str(self.__getGrade()))
        
    def __getGrade(self):
        return self.__grade

# 使用類別建立物件
s1 = Student("陳會安", 85)
s1.displayStudent()  # 呼叫方法
# print("s1.__getGrade() = " + str(s1.__getGrade()))
# 存取資料欄位
print("s1.name = " + s1.name)
# print(s1.__grade)

print("------------------------------------------------------------")  # 60個

import requests

r = requests.get("http://www.google.com")
print(r.status_code)

print("------------------------------------------------------------")  # 60個

r = requests.get("http://www.google.com")
if r.status_code == 200:
    print("請求成功...")
else:
    print("請求失敗...")
     

print("------------------------------------------------------------")  # 60個

url_params = {'name': '陳會安', 'score': 95}
r = requests.get("http://httpbin.org/get", params=url_params)
print(r.url)

print("------------------------------------------------------------")  # 60個

""" fail
from urlencode import urlencode 

url_params = {'name': '陳會安', 'score': 95}
print(urlencode(url_params))
"""
print("------------------------------------------------------------")  # 60個

data = {'name': '陳會安', 'score': 95}
r = requests.get("http://httpbin.org/get", params=data)
print(r.text)

print("------------------------------------------------------------")  # 60個

post_data = {'name': '陳會安', 'score': 95}
r = requests.post("http://httpbin.org/post", data=post_data)
print(r.text)

print("------------------------------------------------------------")  # 60個

url = "https://www.googleapis.com/books/v1/volumes"

data = {'q': 'Python',
        'maxResults': 5, 
        'projection': 'lite'}
r = requests.get(url, params=data)
print(r.json())

print("------------------------------------------------------------")  # 60個

r = requests.get("https://fchart.github.io/test.html")
print(r.text)
print(r.encoding)

print("------------------------------------------------------------")  # 60個

r = requests.get("https://fchart.github.io/test.html")
print(r.text)
print("----------------------")

r = requests.get("https://fchart.github.io/test.html")
print(r.content)
print("----------------------")

r = requests.get("https://fchart.github.io/test.html", stream=True)
print(r.raw)
print(r.raw.read(15))

print("------------------------------------------------------------")  # 60個

r = requests.get("https://fchart.github.io/json/Example.json")
print(r.text)
print(type(r.text))
print("----------------------")
print(r.json())
print(type(r.json()))

print("------------------------------------------------------------")  # 60個

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.ok)

r = requests.get("http://www.google.com/404")
print(r.status_code)
print(r.status_code == requests.codes.ok)

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.status_code == requests.codes.all_good)

print("------------------------------------------------------------")  # 60個
""" request fail
import requests

r = requests.get("http://www.google.com/404")
print(r.status_code)
print(r.status_code == requests.codes.ok)

print(r.raise_for_status())
"""
print("------------------------------------------------------------")  # 60個

import requests 

r = requests.get("http://www.google.com")

print(r.headers['Content-Type'])
print(r.headers['Content-Length'])
print(r.headers['Date'])
print(r.headers['Server'])

print("------------------------------------------------------------")  # 60個

import requests 

r = requests.get("http://www.google.com")

print(r.headers.get('Content-Type'))
print(r.headers.get('Content-Length'))
print(r.headers.get('Date'))
print(r.headers.get('Server'))

print("------------------------------------------------------------")  # 60個

import requests

url = "http://httpbin.org/cookies"

cookies = dict(name='Joe Chen')
r = requests.get(url, cookies=cookies)
print(r.text)

print("------------------------------------------------------------")  # 60個

import requests

session = requests.Session()
response = session.get("http://www.google.com")
v = session.cookies.get_dict()
print(v)

print("------------------------------------------------------------")  # 60個

import requests

url = "http://httpbin.org/user-agent"

r = requests.get(url)
print(r.text)
print("----------------------")

url_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
r = requests.get(url, headers=url_headers)
print(r.text)

print("------------------------------------------------------------")  # 60個

import requests

url = "https://www.googleapis.com/books/v1/volumes"

url_params = {'q': 'Python',
              'maxResults': 3, 
              'projection': 'lite'}
r = requests.get(url, params=url_params)
print(r.json())

print("------------------------------------------------------------")  # 60個

import requests

try: 
    r = requests.get("http://www.google.com", timeout=0.03)
    print(r.text)
except requests.exceptions.Timeout as ex:
    print("錯誤: HTTP請求已經超過時間...\n" + str(ex))
    

print("------------------------------------------------------------")  # 60個

import requests 

url = 'http://www.google.com/404'

try:
    r = requests.get(url, timeout=3)
    r.raise_for_status()
except requests.exceptions.RequestException as ex1:
    print("Http請求錯誤: " + str(ex1))
except requests.exceptions.HTTPError as ex2:
    print("Http回應錯誤: " + str(ex2))
except requests.exceptions.ConnectionError as ex3:
    print("網路連線錯誤: " + str(ex3))
except requests.exceptions.Timeout as ex4:
    print("Timeout錯誤: " + str(ex4))     

print("------------------------------------------------------------")  # 60個

""" webdriver skip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print("-----------------------------")
print(driver.title)
driver.quit()

print("------------------------------------------------------------")  # 60個

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
cookie = {"name": "over18", "value": "1"}
driver.get("https://www.ptt.cc/bbs/Gossiping/index.html")
driver.add_cookie(cookie)
print("-----------------------------")
print(driver.title)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

import requests   

url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
cookies = { "over18": "1" }
r = requests.get(url, cookies=cookies, headers=headers)
print(r.text)


print("------------------------------------------------------------")  # 60個

""" webdriver skip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                          options=options)
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/test.html")
print("-----------------------------")
print(driver.title)
html = driver.page_source
print(html)
driver.quit()
"""
print("------------------------------------------------------------")  # 60個

#
# Extracted from: https://github.com/micropython/micropython-lib/blob/master/collections.defaultdict/collections/defaultdict.py
# Extracted from: https://github.com/micropython/micropython-lib/blob/master/urllib.parse/urllib/parse.py
#

_safe_quoters = {}
_ALWAYS_SAFE = frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                         b'abcdefghijklmnopqrstuvwxyz'
                         b'0123456789'
                         b'_.-')
_ALWAYS_SAFE_BYTES = bytes(_ALWAYS_SAFE)

class defaultdict:

    @staticmethod
    def __new__(cls, default_factory=None, **kwargs):
        # Some code (e.g. urllib.urlparse) expects that basic defaultdict
        # functionality will be available to subclasses without them
        # calling __init__().
        self = super(defaultdict, cls).__new__(cls)
        self.d = {}
        return self

    def __init__(self, default_factory=None, **kwargs):
        self.d = kwargs
        self.default_factory = default_factory

    def __getitem__(self, key):
        try:
            return self.d[key]
        except KeyError:
            v = self.__missing__(key)
            self.d[key] = v
            return v

    def __setitem__(self, key, v):
        self.d[key] = v

    def __delitem__(self, key):
        del self.d[key]

    def __contains__(self, key):
        return key in self.d

    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        return self.default_factory()
        
class Quoter(defaultdict):
    """A mapping from bytes (in range(0,256)) to strings.

    String values are percent-encoded byte values, unless the key < 128, and
    in the "safe" set (either the specified safe set, or default set).
    """
    # Keeps a cache internally, using defaultdict, for efficiency (lookups
    # of cached keys don't call Python code at all).
    def __init__(self, safe):
        """safe: bytes object."""
        self.safe = _ALWAYS_SAFE.union(safe)

    def __repr__(self):
        # Without this, will just display as a defaultdict
        return "<Quoter %r>" % dict(self)

    def __missing__(self, b):
        # Handle a cache miss. Store quoted string in cache and return.
        res = chr(b) if b in self.safe else '%{:02X}'.format(b)
        self[b] = res
        return res


def clear_cache():
    """Clear the quoters cache."""
    _safe_quoters.clear()


def quote(string, safe='/', encoding=None, errors=None):
    """quote('abc def') -> 'abc%20def'

    Each part of a URL, e.g. the path info, the query, etc., has a
    different set of reserved characters that must be quoted.

    RFC 2396 Uniform Resource Identifiers (URI): Generic Syntax lists
    the following reserved characters.

    reserved    = ";" | "/" | "?" | ":" | "@" | "&" | "=" | "+" |
                  "$" | ","

    Each of these characters is reserved in some component of a URL,
    but not necessarily in all of them.

    By default, the quote function is intended for quoting the path
    section of a URL.  Thus, it will not encode '/'.  This character
    is reserved, but in typical usage the quote function is being
    called on a path where the existing slash characters are used as
    reserved characters.

    string and safe may be either str or bytes objects. encoding must
    not be specified if string is a str.

    The optional encoding and errors parameters specify how to deal with
    non-ASCII characters, as accepted by the str.encode method.
    By default, encoding='utf-8' (characters are encoded with UTF-8), and
    errors='strict' (unsupported characters raise a UnicodeEncodeError).
    """
    if isinstance(string, str):
        if not string:
            return string
        if encoding is None:
            encoding = 'utf-8'
        if errors is None:
            errors = 'strict'
        string = string.encode(encoding, errors)
    else:
        if encoding is not None:
            raise TypeError("quote() doesn't support 'encoding' for bytes")
        if errors is not None:
            raise TypeError("quote() doesn't support 'errors' for bytes")

    return quote_from_bytes(string, safe)


def quote_plus(string, safe='', encoding=None, errors=None):
    """Like quote(), but also replace ' ' with '+', as required for quoting
    HTML form values. Plus signs in the original string are escaped unless
    they are included in safe. It also does not have safe default to '/'.
    """
    # Check if ' ' in string, where string may either be a str or bytes.  If
    # there are no spaces, the regular quote will produce the right answer.
    if ((isinstance(string, str) and ' ' not in string) or
            (isinstance(string, bytes) and b' ' not in string)):
        return quote(string, safe, encoding, errors)

    if isinstance(safe, str):
        space = ' '
    else:
        space = b' '

    string = quote(string, safe + space, encoding, errors)
    return string.replace(' ', '+')


def quote_from_bytes(bs, safe='/'):
    """Like quote(), but accepts a bytes object rather than a str, and does
    not perform string-to-bytes encoding.  It always returns an ASCII string.
    quote_from_bytes(b'abc def\x3f') -> 'abc%20def%3f'
    """
    if not isinstance(bs, (bytes, bytearray)):
        raise TypeError("quote_from_bytes() expected bytes")

    if not bs:
        return ''

    if isinstance(safe, str):
        # Normalize 'safe' by converting to bytes and removing non-ASCII chars
        safe = safe.encode('ascii', 'ignore')
    else:
        safe = bytes([c for c in safe if c < 128])

    if not bs.rstrip(_ALWAYS_SAFE_BYTES + safe):
        return bs.decode()

    try:
        quoter = _safe_quoters[safe]
    except KeyError:
        _safe_quoters[safe] = quoter = Quoter(safe).__getitem__

    return ''.join([quoter(char) for char in bs])


def urlencode(query, doseq=False, safe='', encoding=None, errors=None):
    """Encode a dict or sequence of two-element tuples into a URL query string.

    If any values in the query arg are sequences and doseq is true, each
    sequence element is converted to a separate parameter.

    If the query arg is a sequence of two-element tuples, the order of the
    parameters in the output will match the order of parameters in the
    input.

    The components of a query arg may each be either a string or a bytes type.
    When a component is a string, the safe, encoding and error parameters are
    sent to the quote_plus function for encoding.
    """

    if hasattr(query, "items"):
        query = query.items()
    else:
        # It's a bother at times that strings and string-like objects are
        # sequences.
        try:
            # non-sequence items should not work with len()
            # non-empty strings will fail this
            if len(query) and not isinstance(query[0], tuple):
                raise TypeError
            # Zero-length sequences of all types will get here and succeed,
            # but that's a minor nit.  Since the original implementation
            # allowed empty dicts that type of behavior probably should be
            # preserved for consistency
        except TypeError:
            # ty, va, tb = sys.exc_info()
            raise TypeError("not a valid non-string sequence "
                            "or mapping object")  # .with_traceback(tb)

    l = []
    if not doseq:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
            else:
                v = quote_plus(str(v), safe, encoding, errors)

            l.append(k + '=' + v)
    else:
        for k, v in query:
            if isinstance(k, bytes):
                k = quote_plus(k, safe)
            else:
                k = quote_plus(str(k), safe, encoding, errors)

            if isinstance(v, bytes):
                v = quote_plus(v, safe)
                l.append(k + '=' + v)
            elif isinstance(v, str):
                v = quote_plus(v, safe, encoding, errors)
                l.append(k + '=' + v)
            else:
                try:
                    # Is this a sufficient test for sequence-ness?
                    _ = len(v)  # noqa
                except TypeError:
                    # not a sequence
                    v = quote_plus(str(v), safe, encoding, errors)
                    l.append(k + '=' + v)
                else:
                    # loop over the sequence
                    for elt in v:
                        if isinstance(elt, bytes):
                            elt = quote_plus(elt, safe)
                        else:
                            elt = quote_plus(str(elt), safe, encoding, errors)

                        l.append(k + '=' + elt)

    return '&'.join(l)

print("------------------------------------------------------------")  # 60個




"""
Python資料科學實戰教本



"""


import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup 

html_str = "<p>Hello World!</p>"
soup = BeautifulSoup(html_str, "lxml")
print(soup)


print("------------------------------------------------------------")  # 60個

import requests
from bs4 import BeautifulSoup

r = requests.get("https://fchart.github.io/ML/Surveys.html")
r.encoding = "utf8"
soup = BeautifulSoup(r.text, "lxml")
print(soup)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-2-1b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
    print(soup)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

tags = soup("a")
tag = tags[1]
print("標籤名稱: ", tag.name)
print("標籤內容: ", tag.text)
print("標籤內容: ", tag.string)
print("標籤內容: ", tag.b.string)
print("URL網址: ", tag.get("href", None))
print("target屬性: ", tag["target"])




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-2-2a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

tags = soup("img")
tag = tags[0]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-2-3.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 走訪下一層HTML標籤
print(soup.html.body.div.div.p.a.text)
print("----------------------")
# 走訪上一層HTML標籤
tag_div = soup.select_one("#q1") # 找到第1題的<div>標籤
tag_li = tag_div.ul.li    # 走訪到之下的<ul>
print(tag_li.text)
# 使用parent屬性取得父標籤
print(tag_li.parent.parent.p.a.text)
print("----------------------")
tag_div = soup.select_one("#q2") # 找到第2題的<div>標籤
print(tag_div.find_previous_sibling().p.a.text)
print(tag_div.find_next_sibling().p.a.text)

print("------------------------------------------------------------")  # 60個

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<a>標籤
tag_a = soup.find("a") 
print(tag_a.text)
# 呼叫多次find()方法
tag_p = soup.find(name="p")
tag_a = tag_p.find(name="a")
print(tag_p.a.text)
print(tag_a.text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用id屬性搜尋<div>標籤
tag_div = soup.find(id="q2")
tag_a = tag_div.find("a") 
print(tag_a.text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  
    
# 使用class屬性搜尋<span>標籤
tag_span = soup.find(attrs={"class": "score"})
print(tag_span.text)
# 搜尋第2題的第1個<span>標籤
tag_div = soup.find(id="q2")
tag_span = tag_div.find(class_="score")
print(tag_span.text)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1c.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用HTML5的data-屬性搜尋<div>標籤
tag_div = soup.find(attrs={"data-custom": "important"})
print(tag_div.text)



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1d.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")

# 使用文字內容來搜尋標籤
tag_str = soup.find(text="請問你的")
print(tag_str)
tag_str = soup.find(text="10")
print(tag_str)
print(type(tag_str))        # NavigableString型態
print(tag_str.parent.name)  # 父標籤名稱
tag_str = soup.find(text="男 - ")
print(tag_str)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1e.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")   
    
# 測試取出<li>標籤的內容
tag_str = soup.find(text="女 - ")
print(tag_str)
tag_li = soup.find(class_="response")
print(tag_li.text)
print(tag_li.string)
print(tag_li.span.string)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1f.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 使用多條件來搜尋HTML標籤
tag_div = soup.find("div", class_="question")
print(tag_div.prettify())
tag_p = soup.find("p", class_="question")
print(tag_p.prettify())


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-1g.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  
    
# 使用函數建立搜尋條件
def is_secondary_question(tag):
    return tag.has_attr("href") and \
           tag.get("href") == "http://example.com/q2"

tag_a = soup.find(is_secondary_question)
print(tag_a.prettify())



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 找出所有問卷的題目串列
tag_list = soup.find_all("p", class_="question")
print(tag_list[0].prettify())

for question in tag_list:
    print(question.a.text)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")     
    
# 找出前2個問卷的題目串列
tag_list = soup.find_all("p", class_="question", limit=2)
print(len(tag_list))

for question in tag_list:
    print(question.a.text)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有標籤串列
tag_all = tag_div.find_all(True)
for tag in tag_all:
    print(tag.name)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2c.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有文字內容串列
tag_str_list = tag_div.find_all(text=True)
print(tag_str_list)
# 找出指定的文字內容串列
tag_str_list = tag_div.find_all(text=["20", "40"])
print(tag_str_list)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2d.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有<p>和<span>標籤
tag_list = tag_div.find_all(["p", "span"])
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))
print("-------------")
# 找出class屬性值question或selected的所有標籤
tag_list = tag_div.find_all(class_=["question", "selected"])
for tag in tag_list:
    print(tag.name, tag.text.replace("\n", ""))


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-3-2e.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

tag_div = soup.find("div", id="q2")
# 找出所有<li>子孫標籤
tag_list = tag_div.find_all("li")
for tag in tag_list:
    print(tag.text.replace("\n", ""))
# 沒有使用遞迴來找出所有<li>標籤
tag_list = tag_div.find_all("li", recursive=False)
print(tag_list)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<title>標籤和第3個<div>標籤
tag_title = soup.select("title")
print(tag_title[0].text)
tag_first_div = soup.find("div")
tag_div = tag_first_div.select("div:nth-of-type(3)")
print(tag_div[0].prettify())



print("------------------------------------------------------------")  # 60個




#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2a.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋class和id屬性值的標籤
tag_div = soup.select("#q1")
print(tag_div[0].p.a.text)
tag_span = soup.select("span#email")
print(tag_span[0].text)
tag_div = soup.select("#q1, #q2")  # 多個id屬性
for item in tag_div:
    print(item.p.a.text)
print("-----------")
tag_div = soup.find("div")  # 第1個<div>標籤
tag_p = tag_div.select(".question")   
for item in tag_p:
    print(item.a["href"])
tag_span = soup.select("[class~=selected]")
for item in tag_span:
    print(item.text)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2b.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋特定屬性值的標籤
def print_a(tag_a):
    for tag in tag_a:
        print(tag["href"])
    print("-----------")    
tag_a = soup.select("a[href]")
print_a(tag_a)
tag_a = soup.select("a[href='http://example.com/q2']")
print_a(tag_a)
tag_a = soup.select("a[href^='http://example.com']")
print_a(tag_a)
tag_a = soup.select("a[href$='q3']")
print_a(tag_a)
tag_a = soup.select("a[href*='q']")
print_a(tag_a)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2c.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋<title>標籤, 和<div>標籤下的所有<a>標籤
tag_title = soup.select("html head title")
print(tag_title[0].text)    
tag_a = soup.select("body div a")
for tag in tag_a:
    print(tag["href"])




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2d.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋指定標籤下的直接子標籤
tag_a = soup.select("p > a")
for tag in tag_a:
    print(tag["href"])
tag_li = soup.select("ul > li:nth-of-type(2)")
for tag in tag_li:
    print(tag.text.replace("\n", ""))
tag_span = soup.select("div > #email")
for tag in tag_span:
    print(tag.prettify())  



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-2e.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋兄弟標籤
tag_div = soup.find(id="q1")
print(tag_div.p.a.text)
print("-----------")
tag_div = soup.select("#q1 ~ .survey")
for item in tag_div:            
    print(item.p.a.text)  
print("-----------")
tag_div = soup.select("#q1 + .survey")
for item in tag_div:            
    print(item.p.a.text)   



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-4-3.py

from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用select_one()方法搜尋標籤
tag_a = soup.select_one("a[href]")
print(tag_a.prettify())

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-5-2.py

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋文字內容
tag_str = soup.find(text="男 -")
print(tag_str)
regexp = re.compile("男 -")
tag_str = soup.find(text=regexp)
print(tag_str)
print("---------------------")
regexp = re.compile("\w+ -")
tag_list = soup.find_all(text=regexp)
print(tag_list)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-5-2a.py

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋電子郵件地址
email_regexp = re.compile("\w+@\w+\.\w+")
tag_str = soup.find(text=email_regexp)
print(tag_str)
print("---------------------")
tag_list = soup.find_all(text=email_regexp)
print(tag_list)

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-5-2b.py

import re
from bs4 import BeautifulSoup

with open("data/Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用正規表達式搜尋URL網址
url_regexp = re.compile("^http:")
tag = soup.find(href=url_regexp)
print(tag["href"], tag.text)
print("---------------------")
tag_list = soup.find_all(href=url_regexp)
for tag in tag_list:
    print(tag["href"], tag.text)

print("------------------------------------------------------------")  # 60個

"""webdriver skip
#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-1.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-1_edge.py

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
print(driver.title)
soup = BeautifulSoup(driver.page_source, "lxml")
tag_ol = soup.find("ol", {"id":"list"})
tags_li = tag_ol.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2.py

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('//*[@id="list"]')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2_edge.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, '//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2a.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements(By.XPATH, '//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2a_edge.py

from selenium import webdriver

driver = webdriver.Edge("./msedgedriver")
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/Example.html")
tag_ol = driver.find_element_by_xpath('/html/body/ol')
print(tag_ol.tag_name)
tags_li = tag_ol.find_elements_by_xpath('//li')
for tag in tags_li:
    print(tag.text, tag.get_attribute("class"))
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2b.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python資料科學實戰教本\ch04\ch4-6-2b_edge.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://fchart.github.io/ML/Example.html")
tag_ol = driver.find_element(By.XPATH, '//*[@id="list"]')
print(tag_ol.tag_name)
print(tag_ol.get_attribute('innerHTML'))
soup = BeautifulSoup(tag_ol.get_attribute('innerHTML'), "lxml")
tags_li = soup.find_all("li", class_="line")
for tag in tags_li:
    print(tag.text)
driver.quit()
"""

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

