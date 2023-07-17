import re
reobj = re.compile(r'[a-z]+')
m = reobj.findall('3tem12po')
print(m) # ['tem', 'po']