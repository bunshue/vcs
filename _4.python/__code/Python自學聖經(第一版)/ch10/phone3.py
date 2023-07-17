import re
phoneList=["(04)12345678","(04)-12345678"]
pat = r'(\(\d{2}\))-?(\d{8})'

for phone in phoneList:
    phoneNum = re.search(pat,phone)
    if not phoneNum==None:
        print(phoneNum.group())