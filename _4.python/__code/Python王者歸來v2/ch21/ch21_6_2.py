# ch21_6_2.py
import json

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

fn = 'out21_6_2.json'
with open(fn, 'w') as fnObj:
    json.dump(objlist, fnObj)




     
    





