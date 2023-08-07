#built-in package JSON
import json

#json file
data = """{
"items":
{
"item":
[
{
"id": "0001",
"type": "donut",
"name": "Cake",
"ppu": 0.55,
"batters":
{
"batter":
[
{ "id": "1001", "type": "Regular" },
{ "id": "1002", "type": "Chocolate" },
{ "id": "1003", "type": "Blueberry" },
{ "id": "1004", "type": "Devil's Food" }
]
},
"topping":
[
{ "id": "5001", "type": "None" },
{ "id": "5002", "type": "Glazed" },
{ "id": "5005", "type": "Sugar" },
{ "id": "5007", "type": "Powdered Sugar" },
{ "id": "5006", "type": "Chocolate with Sprinkles" },
{ "id": "5003", "type": "Chocolate" },
{ "id": "5004", "type": "Maple" }
]
}
]
}
}"""

print(type(data))
#load JSON data into a dict
print('str 轉 json, str 變 dict')
data_dict = json.loads(data)

#verify dict class
print(type(data_dict))
print()
    
#print the loaded data_dict
print(data_dict)
print()

#verify list class
print(type(data_dict['items']['item']))
print()

#print list
print(data_dict['items']['item'])
print()

#print first item in the list
print(data_dict['items']['item'][0])
print()

#print length of this list
print(len(data_dict['items']['item']))
print()

#access word 'Maple'
print(data_dict['items']['item'][0]["topping"][6]["type"])

