# ch16_18.py
import re
# 測試1
msg = 'Johnson will attend my party tonight.'
pattern = 'John((na)+son)'        # 字串na可以1到多次
txt = re.search(pattern,msg)      # 傳回搜尋結果
print(txt)                        # 請注意是直接列印物件
# 測試2
msg = 'Johnnason will attend my party tonight.'
pattern = 'John((na)+son)'        # 字串na可以1到多次
txt = re.search(pattern,msg)      # 傳回搜尋結果
print(txt.group())
# 測試3
msg = 'Johnnananason will attend my party tonight.'
pattern = 'John((na)+son)'        # 字串na可以1到多次
txt = re.search(pattern,msg)      # 傳回搜尋結果
print(txt.group())

    
