import re
pat = '[a-z]+'
m = re.search(pat,'3tem12po')
print(m) # <re.Match object; span=(1, 4), match='tem'>