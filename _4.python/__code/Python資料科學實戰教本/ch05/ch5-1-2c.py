import re

str1 = "上映日期: 2021-04-21"
match = re.findall(r"[0-9]{4}\-[0-9]{2}\-[0-9]{2}", str1)
if match:
    print(match[0])
else:
    print("沒有找到符合的字串!")


