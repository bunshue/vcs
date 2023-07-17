import re
pat =r'.*'
s="Do your best,\nGo Go Go!"
m = re.search(pat,s)
print(m.group()) # Do your best,
m2 = re.search(r'.*',s,re.DOTALL)
print(m2.group()) # Do your best,\nGo Go Go!