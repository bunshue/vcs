"""
Firebase 即時資料庫
即時資料庫並進行 CRUD (Create, Retrieve, Update, Delete) 操作

sugar/kilo 安裝 pip install pyrebase==3.0.10

"""

import sys
import pyrebase

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("pyrebase 01")

# 註冊與登入
# Enter email: david@lion.mouse.com
# Enter password: abc123

"""
Keep track of the application's current user.
追蹤應用程式的目前使用者。
"""

# Configure and Connext to Firebase

firebaseConfig = {
    "apiKey": "AIzaSyDm2HeGl3bApix5KsbhI8NOjdwXkhNTaJM",
    "authDomain": "trialauth-7eea1.firebaseapp.com",
    "databaseURL": "https://trialauth-7eea1.firebaseio.com",
    "projectId": "trialauth-7eea1",
    "storageBucket": "trialauth-7eea1.appspot.com",
    "messagingSenderId": "441088628124",
    "appId": "1:441088628124:web:59f51ba5b6a475032f2459",
    "measurementId": "G-TNR2V3DEQD",
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def signup():
    print("註冊")
    email = "david@lion.mouse.com"
    password = "abc123"
    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("Email已存在")
    return


def login():
    print("登入")
    email = "david@lion.mouse.com"
    password = "abc123"
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("登入成功")
        print("取得資料 :", auth.get_account_info(login["idToken"]))
        email = auth.get_account_info(login["idToken"])["users"][0]["email"]
        print("取得email :", email)
    except:
        print("登入失敗")
    return


print("註冊")
# signup()

print("登入")
login()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("pyrebase 02 createdata")

"""
1.
Create a Firebase project
建立 Firebase 專案
2.
Initialize a Firebase app with Python
使用 Python 初始化 Firebase 應用程式
3.
Use the Pyrebase library
使用 Pyrebase 程式庫
4.
Insert data into the Realtime Database
將資料插入即時資料庫
5.
Update data in the Realtime Database
更新即時資料庫中的資料
6.
Delete data from the Realtime Database
從即時資料庫刪除資料
7.
Query the Realtime Database
查詢即時資料庫
"""

# Initialize Firebase
firebaseConfig = {
    "apiKey": "AIzaSyDm2HeGl3bApix5KsbhI8NOjdwXkhNTaJM",
    "authDomain": "trialauth-7eea1.firebaseapp.com",
    "databaseURL": "https://trialauth-7eea1.firebaseio.com",
    "projectId": "trialauth-7eea1",
    "storageBucket": "trialauth-7eea1.appspot.com",
    "messagingSenderId": "441088628124",
    "appId": "1:441088628124:web:6fc6142f0e28275e2f2459",
    "measurementId": "G-NKL8XN36NX",
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

# Push Data
data = {"age": 20, "address": ["new york", "los angeles"]}
print(db.push(data))  # unique key is generated

# Create paths using child
# data={"name":"Jane", "age":20}
# db.child("Branch").child("Employees").push(data)

# Create your own key
data = {"age": 20, "address": ["new york", "los angeles"]}
db.child("John").set(data)

# Create your own key + paths with child
data = {"name": "John", "age": 20, "address": ["new york", "los angeles"]}
db.child("Branch").child("Employee").child("male employees").child("John's info").set(
    data
)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("pyrebase 03 deletedata")

firebaseConfig = {
    "apiKey": "AIzaSyBPhwfUTQqOwKq2xH9087gHEslqEQTSNro",
    "authDomain": "pyrebaserealtimedbdemo.firebaseapp.com",
    "databaseURL": "https://pyrebaserealtimedbdemo.firebaseio.com",
    "projectId": "pyrebaserealtimedbdemo",
    "storageBucket": "pyrebaserealtimedbdemo.appspot.com",
    "messagingSenderId": "843349173643",
    "appId": "1:843349173643:web:90ff345ff844aa89d5fb8e",
    "measurementId": "G-DT093HRL5R",
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
""" NG
# Delete item with known key
db.child("todolistA").child("wednesday").child("volunteer").child("deadline").remove()

# Delete entire node and its children
db.child("todolistA").child("tuesday").remove()

# Delete item with unkown generated key
monday_tasks = db.child("todolistB").child("monday").get()

for task in monday_tasks.each():
    if task.val()["name"] == "paper":
        key = task.key()

db.child("todolistB").child("monday").child(key).child("deadline").remove()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("pyrebase 04 updatedata")

firebaseConfig = {
    "apiKey": "AIzaSyBPhwfUTQqOwKq2xH9087gHEslqEQTSNro",
    "authDomain": "pyrebaserealtimedbdemo.firebaseapp.com",
    "databaseURL": "https://pyrebaserealtimedbdemo.firebaseio.com",
    "projectId": "pyrebaserealtimedbdemo",
    "storageBucket": "pyrebaserealtimedbdemo.appspot.com",
    "messagingSenderId": "843349173643",
    "appId": "1:843349173643:web:90ff345ff844aa89d5fb8e",
    "measurementId": "G-DT093HRL5R",
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
""" NG
# Update data with known path
db.child("todolistA").child("monday").child("paper").update({"deadline": "1pm"})

# Multi-location update data
data = {
    "todolistA/monday/paper": {"details": "v2"},
    "todolistA/tuesday/filmvideo": {"deadline": "7pm"},
}
db.update(data)

# Update data with unknown key
monday_tasks = db.child("todolistB").child("monday").get()
for task in monday_tasks.each():
    if task.val()["name"] == "paper":
        key = task.key()
db.child("todolistB").child("monday").child(key).update({"deadline": "1pm"})
"""

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
