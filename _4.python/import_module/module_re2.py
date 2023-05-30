import re

regex = "\d{3}-\d{2}-\d{4}"
ssn = '543-87-3388'
match1 = re.match(regex, ssn)

if match1 != None:
    print(ssn, " is a valid SSN")
    print("start position of the matched text is " + 
        str(match1.start()))
    print("start and end position of the matched text is " +
        str(match1.span()))
else:
    print(ssn, " is not a valid SSN")
    


print('拆解e-mail')
import re
import requests
regex = r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
url = 'http://csharphelper.com/blog/'
html_data = requests.get(url).text

emails = re.findall(regex, html_data)
for email in emails:
    print(email)

print('拆解e-mail')
import re
import requests

regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
url = 'https://auth.cht.com.tw/ldaps/'
html = requests.get(url)
emails = regex.findall(html.text)

for email in emails:
    print(email)



import re
pat = re.compile('[a-z]+')

m = pat.match('tem12po')
print(m) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())



import re
m = re.match(r'[a-z]+','tem12po')
print(m) # <_sre.SRE_Match object; span=(0, 3), match='tem'>

if not m==None:
    print(m.group())
    print(m.start())
    print(m.end())
    print(m.span())

    
import re
pat = re.compile('[a-z]+')

m = pat.search('3tem12po')
print(m) # <_sre.SRE_Match object; span=(1, 4), match='tem'>

if not m==None:
    print(m.group())  # tem
    print(m.start())  # 1
    print(m.end())    # 4
    print(m.span())   # (1,4)

