import re
m = re.match(r'[a-z]+','tem123po')
print(m)

if not m==None:
    print(m.group()) #tem
    print(m.start()) #0
    print(m.end())   #3
    print(m.span())  #(0, 3)