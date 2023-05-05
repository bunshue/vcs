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




