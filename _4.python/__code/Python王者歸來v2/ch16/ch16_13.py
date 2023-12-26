# ch16_13.py
import re

msg = 'Johnson, Johnnason and Johnnathan will attend my party tonight.'
pattern = 'John(son|nason|nathan)'
txt = re.search(pattern,msg)    # 傳回搜尋結果
print(txt.group())              # 列印第一個搜尋結果
print(txt.group(1))             # 列印第一個分組

