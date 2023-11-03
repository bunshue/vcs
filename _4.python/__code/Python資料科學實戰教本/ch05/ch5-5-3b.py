import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mydb          # 選擇mydb資料庫
collection = db.students  # 選擇students

std1 = {
    'name': 'tom wang',
    'dob': '11/01/1988',
    'gender': 'm',
    'favorite_color': 'black',
    'nationality': 'taiwan'
}

std2 = {
    'name': 'john chen',
    'dob': '22/01/1989',
    'gender': 'm',
    'favorite_color': 'blue',
    'nationality': 'taiwan'
}
result = collection.insert_many([std1, std2])
print("新增2筆: {0}".format(result.inserted_ids))
