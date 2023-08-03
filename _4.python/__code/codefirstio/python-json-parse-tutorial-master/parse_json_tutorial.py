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

#load JSON data into a dict
data_dict=json.loads(data)

#verify dict class
print(type(data_dict))

#print the loaded data_dict
print(data_dict)

#verify list class
print(type(data_dict['items']['item']))

#print list
print(data_dict['items']['item'])

#print first item in the list
print(data_dict['items']['item'][0])

#print length of this list
print(len(data_dict['items']['item']))

#access word 'Maple'
print(data_dict['items']['item'][0]["topping"][6]["type"])
