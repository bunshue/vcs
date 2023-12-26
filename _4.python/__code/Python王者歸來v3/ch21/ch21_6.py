# ch21_6.py
import json

obj = {"Asia":\
        [{"Japan":"Tokyo"},\
         {"China":"Beijing"}]\
      }
fn = 'out21_6.json'
with open(fn, 'w') as fnObj:
    json.dump(obj, fnObj)








