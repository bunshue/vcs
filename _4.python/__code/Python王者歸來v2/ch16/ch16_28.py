# ch16_28.py
import re
# 測試1搜尋最後字元是非英文字母數字和底線字元
msg = 'John will attend my party 28 tonight.'
pattern = '\W$'           
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試2搜尋最後字元是非英文字母數字和底線字元
msg = 'I am 28'
pattern = '\W$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試3搜尋最後字元是數字
msg = 'I am 28'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)
# 測試4搜尋最後字元是數字
msg = 'I am 28 year old.'
pattern = '\d$'
txt = re.findall(pattern,msg)      # 傳回搜尋結果
print(txt)



