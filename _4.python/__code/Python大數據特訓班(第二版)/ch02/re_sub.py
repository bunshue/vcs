import re
result = re.sub(r"\d+", "*", "Password:1234,ID:5678")
print(result) # Password:*,ID:*