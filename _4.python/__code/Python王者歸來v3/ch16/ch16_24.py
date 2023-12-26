# ch16_24.py
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



