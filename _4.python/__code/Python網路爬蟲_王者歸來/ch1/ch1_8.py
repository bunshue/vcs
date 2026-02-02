# ch1_8.py
import json

dictObj = {'b':80, 'a':25, 'c':60}      
fn = 'out1_8.json'
with open(fn, 'w') as fnObj:
    json.dump(dictObj, fnObj)








