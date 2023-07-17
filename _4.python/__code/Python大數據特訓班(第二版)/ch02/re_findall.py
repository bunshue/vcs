import re
m = re.findall(r'[a-z]+', 'abc123xyz')
print(m)    # ['abc', 'xyz']