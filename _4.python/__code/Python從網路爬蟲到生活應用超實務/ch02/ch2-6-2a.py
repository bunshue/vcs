import json

data = {
   "name": "Joe Chen", 
   "grade": 95, 
   "tel": "0933123456"
}

jsonfile = "Student.json"
with open(jsonfile, 'w') as fp:
    json.dump(data, fp)


