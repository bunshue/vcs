# ch16_19.py
import re

msg = 'john and TOM will attend my party tonight. JOHN is my best friend.'
pattern = 'John|Tom'                        # 搜尋John和Tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)
pattern = 'Mary|tom'                        # 搜尋Mary和tom
txt = re.findall(pattern, msg, re.I)        # 傳回搜尋忽略大小寫的結果
print(txt)





