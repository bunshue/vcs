# ch16_31.py
import re

msg = 'Name: Jiin-Kwei Hung Address: 8F, Nan-Jing E. Rd, Taipei'
pattern = 'Name: (.*) Address: (.*)'
txt = re.search(pattern,msg)      # 傳回搜尋結果
Name, Address = txt.groups()
print("Name:    ", Name)
print("Address: ", Address)



