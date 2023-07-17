import re
phoneList=["0412345678","(04)12345678","(04)-12345678","(049)2987654","0937-998877"]
pat = r'\(\d{2,4}\)-?\d{6,8}|\d{9,10}|\d{4}-\d{6,8}'
for phone in phoneList:
    phoneNum = re.search(pat,phone)
    if not phoneNum==None:
        print(phoneNum.group())