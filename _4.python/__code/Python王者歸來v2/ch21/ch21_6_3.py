# ch21_6_3.py
import json

objlist = [{"日本":"Japan", "首都":"Tykyo"},
           {"美州":"USA", "首都":"Washington"}]

fn = 'out21_6_3.json'
with open(fn, 'w', encoding='utf-8') as fnObj:
    json.dump(objlist, fnObj, indent=2, ensure_ascii=False)




     
    





