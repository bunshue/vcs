import re
m = re.search(r'[a-z]+', 'abc123xyz')
print(m)    # <re.Match object; span=(0, 3), match='abc'>
if m != None:
    print(m.group())  # abc
    print(m.start())  # 0
    print(m.end())    # 3
    print(m.span())   # (0,3)