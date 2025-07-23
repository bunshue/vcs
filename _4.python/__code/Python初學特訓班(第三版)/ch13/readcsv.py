def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==datas[key]["eword"]: # 讀取鍵名稱
                key_id = key 
                break
    return key_id
        
### 主程式從這裡開始 ###
 
from firebase import firebase

url = 'https://chiouapp01-a6172.firebaseio.com/English'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get(url, None)

with open('eword.csv','r', encoding = 'UTF-8-sig') as f:
    for line in f:
        eword,cword = line.rstrip('\n').split(',')
        word={'eword':eword,'cword':cword}
        if CkeckKey(eword) == "":      # 判斷鍵是否存在
            fb.post(url, word)  
            print(word)
    print("\n轉換完畢!")         