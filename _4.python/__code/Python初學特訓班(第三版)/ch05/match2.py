import re
m = re.match(r'[a-z]+','tem12po')
print(m) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())