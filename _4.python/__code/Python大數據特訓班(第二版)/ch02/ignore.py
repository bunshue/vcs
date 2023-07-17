import re
pat =r'PYTHON|ANDROID'
s="I like Python and Android!"
m = re.findall(pat,s,re.I)
print(m) #['Python', 'Android']