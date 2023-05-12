filename = 'C:/_git/vcs/_1.data/______test_files1/__RW\_txt/python_password2.txt'

import ast

data = dict()
with open(filename,'r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   data = ast.literal_eval(filedata)
print(type(data),data)








