# ch16_16.py
import re

# 測試1
msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d\d-)?(\d{8})'                 # 增加?號
phoneNum = re.search(pattern, msg)           # 傳回搜尋結果
print(f"完整號碼是: {phoneNum.group()}")     # 顯示完整號碼

# 測試2
msg = 'Please call my secretary using 26669999'
pattern = r'(\d\d-)?(\d{8})'                 # 增加?號
phoneNum = re.search(pattern, msg)           # 傳回搜尋結果
print(f"完整號碼是: {phoneNum.group()}")     # 顯示完整號碼

