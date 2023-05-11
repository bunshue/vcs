import time  
from firebase import firebase
url = 'https://chiouapp01-a6172.firebaseio.com/'
fb = firebase.FirebaseApplication(url, None)
students = fb.get('/students', None)
for key,value in students.items():
    print("id={}\tno={}\tname={}".format(key,value["no"],value["name"]))  
    time.sleep(1)