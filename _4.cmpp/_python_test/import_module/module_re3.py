import re
pat = re.compile('[a-z]+')
m = pat.findall('tem12po')
print(m)  # ['tem', 'po']


reobj = re.compile(r'[a-z]+')
m = reobj.findall('3tem12po')
print(m) # ['tem', 'po']


m = re.findall(r'[a-z]+','3tem12po')
print(m) # ['tem', 'po']



string1 = '123abcd456efghijk789123'
string2 = 'abcd456efghijk789123abc'

#match 找出從頭出現的英文字字串

m = re.match(r'[a-z]+', string1)
print('match')
print(m)
if not m == None:
    print(m.group()) #tem
    print(m.start()) #0
    print(m.end())   #3
    print(m.span())  #(0, 3)
else:
    print('找不到')

m = re.match(r'[a-z]+', string2)
print('match')
print(m)
if not m == None:
    print(m.group()) #tem
    print(m.start()) #0
    print(m.end())   #3
    print(m.span())  #(0, 3)
else:
    print('找不到')


#search 找出最早出現的英文字字串

m = re.search(r'[a-z]+', string1)
print('search')
print(m)
if not m == None:
    print(m.group())  # abcd
    print(m.start())  # 3
    print(m.end())    # 7
    print(m.span())   # (3, 7)
else:
    print('找不到')

  



import re

regex = "\d{3}-\d{2}-\d{4}"
text = '543-87-3388'
match1 = re.search(regex, text)

if match1 != None:
    print(text, " contains a SSN")
    print("start position of the matched text is " + str(match1.start()))
    print("start and end position of the matched text is " + str(match1.span()))
else:
    print(text, " does not contain a SSN")




