import re
pat = r'[a-z]+'
m = re.match(pat,'tem12po')
print(m) # <re.Match object; span=(0, 3), match='tem'>