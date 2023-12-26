# ch21_7.py
import json

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

fn = 'out21_7.json'
with open(fn, 'w') as fnObj:
    json.dump(objlist, fnObj)




     
    





