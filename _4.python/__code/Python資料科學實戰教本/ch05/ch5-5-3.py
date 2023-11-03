import pymongo

client = pymongo.MongoClient("localhost", 27017)
db = client.mydb          # 選擇mydb資料庫
collection = db.students  # 選擇students
std = collection.find_one({"name": 'joe chen'})
print(std)
print("------------")
for item in collection.find({"gender":"f"}):
    print(item)
