# ch1_10.py
import json
      
fn = 'out1_9.json'
with open(fn, 'r') as fnObj:
    data = json.load(fnObj)

print(data)
print(type(data))








