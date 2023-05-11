def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==datas[key]["no"]: # 找到鍵名稱
                key_id = key
                break
    return key_id 

### 主程式從這裡開始 ###        
        
from firebase import firebase

students = [{'no':1 ,'name':'李天龍'},
{'no':2,'name':'高一人'},
{'no':3,'name':'洪大同'}]

url = 'https://chiouapp01-a6172.firebaseio.com/'
fb = firebase.FirebaseApplication(url, None)

datas=fb.get('/students', None)

for student in students:
    no=student["no"] # 讀取鍵名稱  
    if CkeckKey(no) == "":      # 判斷鍵是否存在
        fb.post('/students', student)
        print("{} 儲存完畢".format(student)) 