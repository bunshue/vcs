import re
pat=r"\d+"
substr="*"
s="Password:1234,ID:5678"
result = re.sub(pat,substr,s)
print(result) # Password:*,ID:*