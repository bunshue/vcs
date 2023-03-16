# Python 新進測試 01


print('map 的用法')
def pick(x):
    fruits = ['Apple', 'Banana', 'Orange', 'Tomato', 'Pine Apple', 'Berry']
    return fruits[x]

alist = [1, 4, 2, 5, 0, 3, 4, 4, 2]
choices = map(pick, alist)
for choice in choices:
    print(choice)




from sympy import *
x,y,z=symbols('x y z')
init_printing()
Integral(sqrt(1/x),x)



# Python 新進測試 03

# _*_ coding: utf-8 _*_
# 程式 9-1  (Python 3 version)
from urllib.parse import urlparse

url = 'https://www.most.gov.tw/folksonomy/list?menu_id=ba3d22f3-96fd-4adf-a078-91a05b8f0166&filter_uid=none&listKeyword=&pageNum=2&pageSize=18&view_mode=listView&subSite=main&l=ch&tagUid='

uc = urlparse(url)
print("NetLoc:", uc.netloc)
print("Path:", uc.path)

q_cmds = uc.query.split('&')
print("Query Commands:")
for cmd in q_cmds:
    print(cmd)




