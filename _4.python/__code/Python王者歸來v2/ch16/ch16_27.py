# ch16_27.py
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


