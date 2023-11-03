import re

phone = "0938-111-4567 # Pyhone Number"

num = re.sub(r"#.*$", "", phone)
print(num)
num = re.sub(r"\D", "", phone)
print(num)
