import json

jsonfile = "Student.json"
with open(jsonfile, 'r') as fp:
    data = json.load(fp)
json_str = json.dumps(data)
print(json_str)  



