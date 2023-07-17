import re

def multiply(m):
    v = int(m.group())
    return str(v * 2)

result = re.sub("\d+", multiply, "10 20 30 40 50",3)
print(result) # 20 40 60 40 50