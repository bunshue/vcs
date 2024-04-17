"""
各種編碼相關

"""
import sys


print('------------------------------------------------------------')	#60個

print('顯示目前的系統編碼')
print(sys.getdefaultencoding())

print('------------------------------------------------------------')	#60個

string_data1 = '你好'

print('原字串 :', string_data1)
print('用 gb2312 編碼 ')
encode_data = string_data1.encode('gb2312')
print(encode_data)

print('再用 big5 解碼出來')
string_data2 = encode_data.decode('big5')
print(string_data2)

print('萬國碼 unicode, 我')
print('我'.encode('utf8'))

print('------------------------------------------------------------')	#60個

string_data1 = '扂砑腕善衄壽unicode腔垀衄砆牉訧蹋,掀:unicode 2.0 3.0 4.0 梗摯崋欴晤鎢.gb,big-5,gbk,脹脹.坳蠅眳潔腔梗摯薊炵..秪峈扂猁勤森輛俴惆豢,眕扂植懂羶衄勤晤鎢衄徹旃噶,腕悝.褫岆婓厙奻梑祥善涴笱砆牉腔恅梒..洷咡籵徹蠟夔腕善.郅郅!'

print('原字串 :', string_data1)
print('用 big5 編碼 ')
encode_data = string_data1.encode('big5')
print(encode_data)

print('再用 gb2312 解碼出來')
string_data2 = encode_data.decode('gb2312')
print(string_data2)

print('------------------------------------------------------------')	#60個

print('字元轉unicode')

text = '你'
print('原字串 :', text)
print('Unicode編碼後(10進位) :', ord(text))
print('Unicode編碼後(16進位) :', hex(ord(text)))

print('--------')
"""
#unicode() 不能用
text = '中文 test'
print('原字串 :', text)
print(text, len(text))
#utfstr = unicode(text, 'utf-8')
#-------------
text = 'abcdefg'
print('字串 轉 unicode')
ccc = unicode(text, 'utf-8')
print(ccc)
#-------------
print('unicode 轉 字串')
ddd = str(ccc)
print(ddd)
#-------------
text = "Hello!"
u = unicode(text, "utf-8")
print(u)
#-------------

text = '你好'
text_to_unicode = text.decode(encoding='utf-8')  # 要告訴decode原本的編碼是哪種
print(text_to_unicode)

#text = 'Ribeir\xc3\xa3o Preto'
#print(text.decode('cp1252').encode('utf-8'))

"""
print('--------')

num = 65
print(chr(num)) # 輸出數值num的字元

print('--------')
text = '你好'
print('原字串 :', text)
print('字串 轉 UTF-8 => UTF-8 拜列')
byte_array = text.encode('UTF-8')
print(type(byte_array))
print(byte_array)
print('UTF-8 拜列 轉 字串')
print(byte_array.decode('UTF-8'))
print('--------')
byte_array = b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(len(byte_array))
print(byte_array.decode('UTF-8'))

print('--------')
byte_array = b'\xe4\xbd\xa0\xe5\xa5\xbe'
print(len(byte_array))
print(byte_array.decode('UTF-8'))

print('--------')

"""
for i in range(128):
    c = chr(i)
    print(c, end = '')
"""


print('------------------------------------------------------------')	#60個

_b85alphabet = (b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                b"abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")

_b85chars = [bytes((i,)) for i in _b85alphabet]
print(_b85chars)
print()

_b85chars2 = [(a + b) for a in _b85chars for b in _b85chars]
print(_b85chars2)

print('------------------------------------------------------------')	#60個

print('字串轉拜列')
text = 'lion'
byte_array = repr(text).encode('utf-8') + b'\0'
print(type(byte_array))
print(byte_array)

print('------------------------------------------------------------')	#60個

command1 = 'abcde'
print(type(command1))
print(command1)

command2 = command1.encode()
print(type(command2))
print(command2)

print('------------------------------------------------------------')	#60個

""" many
import codecs
import contextlib
import io
import locale
import unittest
import warnings
import encodings

all_unicode_encodings = [
    "ascii",
    "big5",
    "big5hkscs",
    "charmap",
    "cp037",
    "cp1006",
    "cp1026",
    "cp1125",
    "cp1140",
    "cp1250",
    "cp1251",
    "cp1252",
    "cp1253",
    "cp1254",
    "cp1255",
    "cp1256",
    "cp1257",
    "cp1258",
    "cp424",
    "cp437",
    "cp500",
    "cp720",
    "cp737",
    "cp775",
    "cp850",
    "cp852",
    "cp855",
    "cp856",
    "cp857",
    "cp858",
    "cp860",
    "cp861",
    "cp862",
    "cp863",
    "cp864",
    "cp865",
    "cp866",
    "cp869",
    "cp874",
    "cp875",
    "cp932",
    "cp949",
    "cp950",
    "euc_jis_2004",
    "euc_jisx0213",
    "euc_jp",
    "euc_kr",
    "gb18030",
    "gb2312",
    "gbk",
    "hp_roman8",
    "hz",
    "idna",
    "iso2022_jp",
    "iso2022_jp_1",
    "iso2022_jp_2",
    "iso2022_jp_2004",
    "iso2022_jp_3",
    "iso2022_jp_ext",
    "iso2022_kr",
    "iso8859_1",
    "iso8859_10",
    "iso8859_11",
    "iso8859_13",
    "iso8859_14",
    "iso8859_15",
    "iso8859_16",
    "iso8859_2",
    "iso8859_3",
    "iso8859_4",
    "iso8859_5",
    "iso8859_6",
    "iso8859_7",
    "iso8859_8",
    "iso8859_9",
    "johab",
    "koi8_r",
    "koi8_u",
    "latin_1",
    "mac_cyrillic",
    "mac_greek",
    "mac_iceland",
    "mac_latin2",
    "mac_roman",
    "mac_turkish",
    "palmos",
    "ptcp154",
    "punycode",
    "raw_unicode_escape",
    "shift_jis",
    "shift_jis_2004",
    "shift_jisx0213",
    "tis_620",
    "unicode_escape",
    "utf_16",
    "utf_16_be",
    "utf_16_le",
    "utf_7",
    "utf_8",
]

print(type(all_unicode_encodings))
    
for encoding in all_unicode_encodings:
    name = codecs.lookup(encoding).name
    print(name)

for encoding in all_unicode_encodings:
    reader = codecs.getreader(encoding)
    print(reader)

for encoding in all_unicode_encodings:
    decoder = codecs.getdecoder(encoding)

for encoding in all_unicode_encodings:
    encoder = codecs.getencoder(encoding)

ALL_CJKENCODINGS = [
# _codecs_cn
    'gb2312', 'gbk', 'gb18030', 'hz',
# _codecs_hk
    'big5hkscs',
# _codecs_jp
    'cp932', 'shift_jis', 'euc_jp', 'euc_jisx0213', 'shift_jisx0213',
    'euc_jis_2004', 'shift_jis_2004',
# _codecs_kr
    'cp949', 'euc_kr', 'johab',
# _codecs_tw
    'big5', 'cp950',
# _codecs_iso2022
    'iso2022_jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_2004',
    'iso2022_jp_3', 'iso2022_jp_ext', 'iso2022_kr',
]

for enc in ALL_CJKENCODINGS:
    code = '# coding: {}\n'.format(enc)
    print(code)
"""
print('------------------------------------------------------------')	#60個

print('編碼: 字串轉拜列')
print('解碼: 拜列轉字串')

str1 = '金詢初海花浪花情真'

print('用 big5 編碼')
cc = str1.encode('big5')
print(cc)

print('用 gbk 編碼')
cc = str1.encode('gbk')
print(cc)

print('用 utf-8 編碼')
cc = str1.encode('utf-8')
print(cc)

data = b'\xB8\xAD'

print('用 big5 解碼')
cc = data.decode('big5')
print(cc)
# 將bytes轉為big5文字，'葉'

print('用 gbk 解碼')
cc = data.decode('gbk')
print(cc)
# 將bytes轉為gbk文字，'腑'

"""
print('用 utf-8 解碼')
cc = data.decode('utf-8')
print(cc)
# 將bytes轉為ytf-8文字，解碼規則無法解碼
"""



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

