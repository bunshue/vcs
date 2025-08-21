from firebase import firebase

students = [{'no':1 ,'name':'李天龍'},
{'no':2,'name':'高一人'},
{'no':3,'name':'洪大同'}]

url = 'https://chiouapp01-a6172.firebaseio.com/'
fb = firebase.FirebaseApplication(url, None)

for student in students:
    fb.post('/students', student)
    print("{} 儲存完畢".format(student))  