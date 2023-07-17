import re
pat =r'^\d+'
s="2020 is coming soon"
m = re.findall(pat,s)
print(m) #['2020']
m2 = re.findall(r'\w+$',s)
print(m2) #['soon']