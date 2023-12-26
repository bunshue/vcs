# ch21_6_1.py
import json

obj = {"Asia":
        [{"Japan":"Tokyo"},
         {"China":"Beijing"}]
      }
fn = 'out21_6_1.json'
with open(fn, 'w') as fnObj:
    json.dump(obj, fnObj)




     
    





