import re

ptn = re.compile(r'[0-9]+')
print(ptn.search('a1b23c456d').group())
print(ptn.findall('a1b23c456d'))
print(ptn.sub('#', 'a1b23c456d'))