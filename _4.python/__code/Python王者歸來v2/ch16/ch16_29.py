# ch16_29.py
import re
# 測試1搜尋開始到結尾皆是數字的字串
msg = '09282028222'
pattern = '^\d+$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋開始到結尾皆是數字的字串
msg = '0928tuyr990'
pattern = '^\d+$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)




