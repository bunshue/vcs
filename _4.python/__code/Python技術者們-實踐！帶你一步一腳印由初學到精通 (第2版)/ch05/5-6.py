import re

m = re.search(r'p[a-z]+e', 'apples')
print(m)   # 輸出 <_sre.SRE_Match object; span=(1, 5), match='pple'>
print(m.group())    # 輸出 pple
print(m.start())    # 輸出 1
print(m.end())    # 輸出 5 注意！pple 的位置是 1~4
print(m.span())    # 輸出 (1, 5)