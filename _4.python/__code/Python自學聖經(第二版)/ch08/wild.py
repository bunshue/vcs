import re
pat =r'.o'
s="Do your best!"
m = re.findall(pat,s)
print(m)  # ['Do', 'yo']
m2 = re.findall(r'.*o',s)
print(m2) # ['Do yo']