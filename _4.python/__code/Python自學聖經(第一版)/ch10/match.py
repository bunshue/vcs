import re
pat = re.compile(r'[a-z]+')

m = pat.match('tem12po')
print(m) # <re.Match object; span=(0, 3), match='tem'>
if not m==None:
    print(m.group()) #tem
    print(m.start()) #0
    print(m.end())   #3
    print(m.span())  #(0,3)