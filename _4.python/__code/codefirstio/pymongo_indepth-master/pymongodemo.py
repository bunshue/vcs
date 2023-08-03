import pymongo
# Connect to MongoDB instance running on localhost
client = pymongo.MongoClient()

#Create a Database called mydatabase
mydb = client["mydatabase"]
#Print the list of databases
print(client.list_database_names())

#mydatabase will not appear in the list
#MongoDB waits until you have created a collection with
#at least one document (record) before it actually
#creates the database

#Create a collection
mycol = mydb["people"]

#Insert a document into the collection
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

#Print the _id of the inserted document
print(x.inserted_id)

#Insert many documents into the collection
mylist = [
  { "name": "Jane", "age":40},
  { "name": "Mark"}
  ]
x = mycol.insert_many(mylist)

#Print list of the _id values of the inserted documents:
print(x.inserted_ids)

#Print the list of databases again
print(client.list_database_names())

#Print the list of collections in the database
print(mydb.list_collection_names())

#Find the first document in the collection
print(mycol.find_one())

#Print all documents in the collection
for x in mycol.find():
  print(x)

#Print all documents excluding address
for x in mycol.find({},{ "address": 0 }):
  print(x)

#Print all documents with name Jane
for x in mycol.find({"name":"Jane"}):
  print(x)
