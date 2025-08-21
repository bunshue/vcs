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
