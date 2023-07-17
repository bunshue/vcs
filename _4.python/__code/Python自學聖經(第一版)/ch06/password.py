#import ast
import json
data = dict()
with open('password.txt','r', encoding = 'UTF-8-sig') as f:
   filedata = f.read()
   print(filedata)
#   filedata = filedata.replace("\'", "\"")
#   data = ast.literal_eval(filedata)
   data = json.loads(filedata)
print(type(data),data)


   