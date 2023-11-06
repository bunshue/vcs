import re

str1 = """Joe's email is joe@gmail.com,  
Tom's email is tom@yahoo.com"""
pattern = re.compile(r"[\w.-]+@[A-Za-z0-9_.-]+")
match = re.search(pattern, str1)
if match:
    print(match.group())
else:
    print("沒有找到符合的字串!")
    

