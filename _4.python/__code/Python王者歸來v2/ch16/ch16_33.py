# ch16_33.py
import re
#測試1搜尋使用re.match()
msg = 'John will attend my party tonight.'  # John是第一個字串
pattern = 'John'
txt = re.match(pattern,msg)                 # 傳回搜尋結果
if txt != None:
    print("測試1輸出: ", txt.group())
else:
    print("測試1搜尋失敗")
#測試2搜尋使用re.match()
msg = 'My best friend is John.'             # John不是第一個字串
txt = re.match(pattern,msg,re.DOTALL)       # 傳回搜尋結果
if txt != None:
    print("測試2輸出: ", txt.group())
else:
    print("測試2搜尋失敗")






