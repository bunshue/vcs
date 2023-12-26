# ch21_7.py
import json
      
fn = 'out21_6.json'
with open(fn, 'r') as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))








