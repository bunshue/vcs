"""
＊自架 Server
serviceAccountKey.json：透過 Google Cloud console，選擇服務帳戶－> 點擊新增金鑰－> 類型 JSON

"""


"""
1.
Create a Firebase project
建立 Firebase 專案
2.
Initialize a Firebase app with Python
使用 Python 初始化 Firebase 應用程式
3.
Use the Firebase Admin SDK
使用 Firebase 管理員 SDK
4.
Insert data into the Cloud Firestore
將資料插入 Cloud Firestore
5.
Update data in the Cloud Firestore
更新 Cloud Firestore 中的資料
6.
Delete data from the Cloud Firestore
從 Cloud Firestore 刪除資料
7.
Query the Cloud Firestore
查詢 Cloud Firestore
"""

import sys
import pyrebase

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

api_key = "C:/_git/vcs/_1.data/______test_files1/_key/david-firebase-proj-firebase-adminsdk.json"


cred = credentials.Certificate(api_key)
firebase_admin.initialize_app(cred)

"""
cred = credentials.Certificate(api_key)
default_app = firebase_admin.initialize_app(cred)
"""

db = firestore.client()

doc_ref = db.collection("Q1", "DOC1", "Q2").document("DOC2")

# Method 1
doc_ref.set(
    {
        "姓名": "劉德華",
        "年紀": "23",
        "工作": "爆肝工程師",
    }
)
# Method 2
data = {
    "姓名": "劉德華",
    "年紀": "23",
    "工作": "爆肝工程師",
}
doc_ref.set(data)

print("Done")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# create_data

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Using add to add documents with auto generated keys
db.collection("persons").add({"name": "John", "age": 40, "address": "New York"})
db.collection("persons").add({"name": "Jane", "age": 50, "address": "Los Angeles"})
db.collection("persons").add({"name": "Mark", "age": 40, "address": "Paris"})
db.collection("persons").add({"name": "Harry", "age": 40, "address": "London"})
db.collection("persons").add({"name": "Ron", "age": 40, "address": "Milan"})

# Create a reference for the document before setting
data = {"name": "Harry Potter", "address": "USA"}

# Add a new doc in collection 'persons' with ID 'HP'
db.collection("persons").document("HP").set(data)

# Merge new data with existing data for 'HP'
data = {"employed": True}
db.collection("persons").document("HP").set(data, merge=True)

# Using document() to get an auto generated ID with set()
data = {"name": "Iron Man", "address": "USA"}
document_reference = db.collection("heroes").document()
document_reference.set(data)

# Adding subcollections
document_reference.collection("movies").add({"name": "Avengers"})

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# read_data

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

api_key = "C:/_git/vcs/_1.data/______test_files1/_key/david-firebase-proj-firebase-adminsdk.json"

# Setup
cred = credentials.Certificate(api_key)
firebase_admin.initialize_app(cred)

db = firestore.client()

# Read data
# Get a document with known id
result = db.collection("persons").document("p1").get()
if result.exists:
    print(result.to_dict())

# Get all documents
docs = db.collection("persons").get()
for doc in docs:
    print(doc.to_dict())

# Query
# Equal
docs = db.collection("persons").where("age", "==", "52").get()
for doc in docs:
    print(doc.to_dict())

# Greater than
docs = db.collection("persons").where("age", ">", "22").get()
for doc in docs:
    print(doc.to_dict())

# Array contains
docs = db.collection("persons").where("socials", "array_contains", "facebook").get()
for doc in docs:
    print(doc.to_dict())

# In
docs = db.collection("persons").where("address", "in", ["Milan", "London"]).get()
for doc in docs:
    print(doc.to_dict())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# update_data

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Update data with known key
db.collection("persons").document("p1").update({"age": 50})  # field already exists
db.collection("persons").document("p1").update(
    {"age": firestore.Increment(2)}
)  # increment a field
db.collection("persons").document("p1").update(
    {"occupation": "engineer"}
)  # the field will be added
db.collection("persons").document("p1").update({"occupation": "engineer"})
db.collection("persons").document("p2").update(
    {"socials": firestore.ArrayRemove(["linkedin"])}
)
db.collection("persons").document("p1").update(
    {"socials": firestore.ArrayUnion(["linkedin"])}
)


# Update data with unknown key
docs = db.collection("persons").get()  # Get all data
for doc in docs:
    if doc.to_dict()["age"] >= 40:  # Check if age>=40
        key = doc.id
        db.collection("persons").document(key).update({"age_group": "middle age"})

# Update data with unknown key: second way
docs = (
    db.collection("persons").where("age", ">=", 40).get()
)  # Get all documents with age >=40
for doc in docs:
    key = doc.id
    db.collection("persons").document(key).update({"age_group": "middle age"})


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# delete_data

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

api_key = "C:/_git/vcs/_1.data/______test_files1/_key/david-firebase-proj-firebase-adminsdk.json"

# Setup
cred = credentials.Certificate(api_key)
firebase_admin.initialize_app(cred)

db = firestore.client()

# Delete a document - known ID
db.collection("persons").document("p1").delete()

# Delete a field - known ID
db.collection("persons").document("p2").update("age", firestore.DELETE_FIELD)

# Delete a document with a known ID
docs = (
    db.collection("persons").where("age", ">=", 50).get()
)  # Get all documents with age >=50
for doc in docs:
    key = doc.id
    db.collection("persons").document(key).delete()

# Delete a field - unknown ID
docs = (
    db.collection("persons").where("age", ">=", 40).get()
)  # Get all documents with age >=40
for doc in docs:
    key = doc.id
    db.collection("persons").document(key).update("age", firestore.DELETE_FIELD)

# Delete all documents in a collection
docs = db.collection("persons").get()  # Get all data
for doc in docs:
    db.collection("persons").document(key).delete()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
