# ch16_8.py
import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)           # 傳回搜尋結果

print(f"完整號碼是: {phoneNum.group()}")     # 顯示完整號碼
print(f"完整號碼是: {phoneNum.group(0)}")    # 顯示完整號碼
print(f"區域號碼是: {phoneNum.group(1)}")    # 顯示區域號碼
print(f"電話號碼是: {phoneNum.group(2)}")    # 顯示電話號碼



