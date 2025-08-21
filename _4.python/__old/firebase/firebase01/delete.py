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
url = 'https://chiouapp01-a6172.firebaseio.com/'
fb = firebase.FirebaseApplication(url, None)

while True:
    datas=fb.get('/students', None)
    no = input("請輸入座號(Enter==>停止輸入)")
    if no=="": break
    key_id = CkeckKey(int(no))   
    if key_id != "":    # 判斷鍵是否存在
        print("確定刪除{}的資料!：".format(datas[key_id]["name"]))
        yn=input("(Y/N)?")
        if (yn=="Y" or yn=="y"):
            fb.delete('/students/'+key_id,None)
        print("資料刪除完畢\n")         
    else:
        print("{} 未建立!\n".format(no)) 