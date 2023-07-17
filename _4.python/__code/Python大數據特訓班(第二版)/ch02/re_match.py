import re
m = re.match(r'[a-z]+','abc123xyz')
print(m) 
if m != None:
    print(m.group())    #abc
    print(m.start())    #0
    print(m.end())      #3
    print(m.span())     #(0, 3)