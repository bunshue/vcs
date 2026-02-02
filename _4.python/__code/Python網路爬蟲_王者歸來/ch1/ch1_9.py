# ch1_9.py
import json

obj = {"Asia":
        [{"Japan":"Tokyo"},
         {"China":"Beijing"}]
      }
fn = 'out1_9.json'
with open(fn, 'w') as fnObj:
    json.dump(obj, fnObj)




     
    





