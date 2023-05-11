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
import time

url = 'https://chiouapp01-a6172.firebaseio.com/'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get('/students', None)

while True:
    no = input("請輸入座號(Enter==>停止輸入)")
    if no=="": break
    key_id = CkeckKey(int(no))   
    if key_id != "":      # 判斷鍵是否存在
        print("原來姓名：{}".format(datas[key_id]["name"]))  
        name=input("請輸入姓名：")
        data = {"no":int(no),"name":name} 
        datas[key_id]=data 
        fb.put(url + '/students/', data=data, name=key_id)       
        time.sleep(2)
        print("{} 已修改完畢\n".format(data))         
    else:
        print("{} 未建立!\n".format(no)) 