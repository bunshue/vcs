import re
pat =r'[^a-z. ]+'
s="John was 18 year old."
m = re.findall(pat,s)
print(m) #['J', '18']