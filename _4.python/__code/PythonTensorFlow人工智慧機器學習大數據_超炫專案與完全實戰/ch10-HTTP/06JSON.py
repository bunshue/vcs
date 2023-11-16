#!/usr/bin/env python
# coding=utf8
import json

data = {
    'name' : 'Powen Ko',
    'shares' : 100,
    'price' : 542.23
}

json_str = json.dumps(data)
print(json_str)
data = json.loads(json_str)
print(data)
print(data['name'])

with open('data.json', 'w') as f:
    json.dump(data, f)

# Reading data back
with open('data.json', 'r') as f:
    data = json.load(f)

