import re
pat = re.compile('[a-z]+')
m = pat.findall('tem12po')
print(m)  # ['tem', 'po']