"""
各種編碼相關

編碼: 字串轉拜列
解碼: 拜列轉字串

原始字串  original_string
編碼拜列  encoded_bytes
解碼字串  decoded_string

"""
import sys

print('------------------------------------------------------------')	#60個

print('顯示目前的Python系統編碼')
print(sys.getdefaultencoding())

import locale
print('取得目前Windows作業系統設定的編碼')
print(locale.getpreferredencoding())

print('------------------------------------------------------------')	#60個

original_string = '金詢初海花浪花情真'
print('原始字串 :', original_string)

print('用 big5 編碼')
encoded_bytes = original_string.encode(encoding='big5') # 有無encoding=皆可
print(encoded_bytes)

print('用 big5 解碼')
decoded_string = encoded_bytes.decode(encoding='big5')
print(decoded_string)

print('------------------------------')	#30個

print('用 gbk 編碼')
encoded_bytes = original_string.encode('gbk')
print(encoded_bytes)

print('用 gbk 解碼')
decoded_string = encoded_bytes.decode('gbk')
print(decoded_string)

print('------------------------------')	#30個

print('用 utf-8 編碼')
encoded_bytes = original_string.encode('utf-8')#有無-皆可, 大小寫皆可
print(encoded_bytes)

print('用 utf-8 解碼')
decoded_string = encoded_bytes.decode('UTF-8')
print(decoded_string)

print('------------------------------')	#30個

original_string = '金詢初海花浪花情真'
print('原始字串 :', original_string)

encoded_bytes = repr(original_string).encode('utf-8') + b'\0'
print(type(encoded_bytes))
print(encoded_bytes)

print('------------------------------------------------------------')	#60個

print('從 你好 變成 斕疑 的原因')

original_string = '你好'
print('原始字串 :', original_string)

print('用 簡中 編碼 ')
encoded_bytes = original_string.encode('gb2312')
print(encoded_bytes)

print('用 正中 解碼')
decoded_string = encoded_bytes.decode('big5')
print(decoded_string)

print('------------------------------------------------------------')	#60個

print('把怪怪的字解譯出來')

original_string = '扂砑腕善衄壽unicode腔垀衄砆牉訧蹋,掀:unicode 2.0 3.0 4.0 梗摯崋欴晤鎢.gb,big-5,gbk,脹脹.坳蠅眳潔腔梗摯薊炵..秪峈扂猁勤森輛俴惆豢,眕扂植懂羶衄勤晤鎢衄徹旃噶,腕悝.褫岆婓厙奻梑祥善涴笱砆牉腔恅梒..洷咡籵徹蠟夔腕善.郅郅!'
print('原始字串 :', original_string)

print('用 正中 編碼 ')
encoded_bytes = original_string.encode('big5')
print(encoded_bytes)

print('用 簡中 解碼')
decoded_string = encoded_bytes.decode('gb2312')
print(decoded_string)

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個

print('chr(x) 取得整數x的ASCII編碼值')
num = 0x41
print(chr(num)) # 輸出數值num的字元

for i in range(0x30, 120):
    c = chr(i)
    print(c, end = '')
print()

print('ord(x) 取得字元x的Unicode編碼值')

original_string = '你'
cc = ord(original_string)
print(cc)

original_string = '你'
print('Unicode編碼後(10進位) :', ord(original_string))
print('Unicode編碼後(16進位) :', hex(ord(original_string)))

print('------------------------------------------------------------')	#60個

_b85alphabet = (b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                b"abcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~")

_b85chars = [bytes((i,)) for i in _b85alphabet]
print(_b85chars)
print()

_b85chars2 = [(a + b) for a in _b85chars for b in _b85chars]
print(_b85chars2)

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


x1 = 97
x2 = chr(x1)
print(x2)  # 輸出數值97的字元
x3 = ord(x2)
print(x3)  # 輸出字元x3的Unicode(10進位)碼值
x4 = "魁"
print(hex(ord(x4)))  # 輸出字元'魁'的Unicode(16進位)碼值

print("------------------------------------------------------------")  # 60個

for x in range(0x2160, 0x216A):
    print(chr(x), end=" ")


print("------------------------------------------------------------")  # 60個

# ROT13 加密法

def rot13(word):
    output = []
    for c in word.lower():
        new_ord = ord(c) + 13
        if new_ord > ord("z"):
            new_ord -= 26
        output.append(chr(new_ord))
    return "".join(output)


print(rot13("apple"))



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

