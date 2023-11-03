import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mydb          # 選擇mydb資料庫
collection = db.students  # 選擇students

std = {
    'name': 'mary wang',
    'dob': '11/05/1978',
    'gender': 'f',
    'favorite_color': 'red',
    'nationality': 'taiwan'
}

result = collection.insert_one(std)
print("新增1筆: {0}".format(result.inserted_id))
