import re
pat = re.compile('[a-z]+')

m = pat.search('3tem12po')
print(m) # <re.Match object; span=(1, 4), match='tem'>
if not m==None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())    # 4
    print(m.span())   # (1,4)