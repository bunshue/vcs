import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

api_key = 'C:/_git/vcs/_1.data/______test_files1/_key/david-firebase-proj-firebase-adminsdk.json'


cred = credentials.Certificate(api_key)
firebase_admin.initialize_app(cred)

'''
cred = credentials.Certificate(api_key)
default_app = firebase_admin.initialize_app(cred)
'''

db = firestore.client()

doc_ref = db.collection('Q1', 'DOC1', 'Q2').document('DOC2')

#Method 1
doc_ref.set({
    '姓名': '劉德華',
    '年紀': '23',
    '工作': '爆肝工程師',
})
#Method 2
data = {
    '姓名': '劉德華',
    '年紀': '23',
    '工作': '爆肝工程師',
}
doc_ref.set(data)

print('Done')

