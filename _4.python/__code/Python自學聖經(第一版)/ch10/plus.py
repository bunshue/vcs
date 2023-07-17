import re
pat = re.compile(r'[aeiou]+')
s="John is my best friend."
m = re.findall(pat,s)
print(m) #['o', 'i', 'e', 'ie']