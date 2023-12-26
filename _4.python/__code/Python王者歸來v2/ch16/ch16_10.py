# ch16_10.py
import re

msg = 'Please call my secretary using 02-26669999'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.search(pattern, msg)      # 傳回搜尋結果
areaNum, localNum = phoneNum.groups()   # 留意是groups()
print(f"區域號碼是: {areaNum}")         # 顯示區域號碼
print(f"電話號碼是: {localNum}")        # 顯示電話號碼



