# ch21_6.py
import json

dictObj = {'b':80, 'a':25, 'c':60}      
fn = 'out21_6.json'
with open(fn, 'w') as fnObj:
    json.dump(dictObj, fnObj)








