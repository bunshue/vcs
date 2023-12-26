# ch21_5_1.py
import json

obj = '{"Asia":[{"Japan":"Tokyo"},{"China":"Beijing"}]}'
json_obj = json.loads(obj)
print(json_obj)
print(json_obj["Asia"])
print(json_obj["Asia"][0])
print(json_obj["Asia"][1])
print(json_obj["Asia"][0]["Japan"])
print(json_obj["Asia"][1]["China"])


       
    





