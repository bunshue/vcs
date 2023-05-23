import re
pat = re.compile('[a-z]+')

m = pat.match('tem12po')
print(m) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())



import re
m = re.match(r'[a-z]+','tem12po')
print(m) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

    
import re
pat = re.compile('[a-z]+')

m = pat.search('3tem12po')
print(m) # <_sre.SRE_Match object; span=(1, 4), match='tem'>

if not m==None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())    # 4
    print(m.span())   # (1,4)
