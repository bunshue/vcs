# ch1_9_1.py
import json

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

fn = 'out1_9_1.json'
with open(fn, 'w') as fnObj:
    json.dump(objlist, fnObj)




     
    





