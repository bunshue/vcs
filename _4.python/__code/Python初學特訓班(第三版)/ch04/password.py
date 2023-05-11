import ast
data = dict()
with open('password.txt','r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   data = ast.literal_eval(filedata)
print(type(data),data)