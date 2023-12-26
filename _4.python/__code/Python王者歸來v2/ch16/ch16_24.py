# ch16_24.py
import re

msg = '1 cat, 2 dogs, 3 pigs, 4 swans'
pattern = '\d+\s\w+'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



