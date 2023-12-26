# ch16_9.py
import re

msg = 'Please call my secretary using 02-26669999 or 02-11112222'
pattern = r'(\d{2})-(\d{8})'
phoneNum = re.findall(pattern, msg)           # 傳回搜尋結果
print(phoneNum)



