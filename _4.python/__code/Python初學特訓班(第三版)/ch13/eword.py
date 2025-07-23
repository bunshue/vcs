def menu():
    os.system("cls")
    print("英 文 單 字 王")
    print("-------------------------")
    print("1. 查  詢  單  字")
    print("2. 新  增  單  字")
    print("3. 顯  示  單  字")
    print("4. 修  改  單  字")
    print("5. 刪  除  單  字")
    print("0. 結  束  程  式")
    print("-------------------------")
    
def CkeckKey(no):
    key_id=""
    if datas != None:
        for key in datas:
            if no==datas[key]["eword"]: # 讀取鍵名稱
                key_id = key 
                break
    return key_id   
    
def input_data(): 
    global datas       
    while True:
        eword =input("請輸入英文單字(Enter==>停止輸入)")
        if eword=="": break
        key_id = CkeckKey(eword)   
        if key_id != "":      # 判斷鍵是否存在
            print("{} 單字已存在!".format(datas[key_id]))
            continue
        cword=input("請輸入中文翻譯：")
        word={'eword':eword,'cword':cword}
        key_id=fb.post(url, word)["name"]
        time.sleep(2)
        if datas == None: datas = dict()
        datas[key_id]=word
        print("{}已被儲存完畢".format(word))
        
def disp_data():
    global datas
    datas=fb.get(url, None)
    if datas != None:
        n,page=0,15
        for key in datas:
            if n % page ==0:
                  print("單字\t中文翻譯")
                  print("======================")
            print("{}\t{}".format(datas[key]["eword"],datas[key]["cword"]))
            n+=1
            if n == page:
                c=input("請按 Enter 顯示下一頁，Q 鍵返回主選單") 
                if c.upper() == "Q":return
                n=0
        c=input("請按任意鍵返回主選單") 
        
def search_data():
    while True:
        eword =input("請輸入要查詢的英文單字(Enter==>停止輸入)")
        if eword=="": break
        key_id = CkeckKey(eword)
        if key_id != "":      # 判斷鍵是否存在
            print("中文翻譯：{}".format(datas[key_id]["cword"]))
        else:
            print("{} 未建立!\n".format(eword))  
        input("請按任意鍵繼續查詢…")    
        
def edit_data():
    while True:
        eword =input("請輸入要修改的英文單字(Enter==>停止輸入)")
        if eword=="": break
        key_id = CkeckKey(eword)
        if key_id != "":      # 判斷鍵是否存在
            print("原來中文翻譯：{}".format(datas[key_id]["cword"]))  
            cword=input("請輸入中文翻譯：")
            word={'eword':eword,'cword':cword}
            datas[key_id]=word 
            fb.put(url + '/', data=word, name=key_id)       
            time.sleep(2)
            print("{} 已修改完畢\n".format(word))         
        else:
            print("{} 未建立!\n".format(eword)) 

def delete_data():
    while True:
        eword =input("請輸入要刪除的英文單字(Enter==>停止輸入)")
        if eword=="": break
        key_id = CkeckKey(eword)   
        if key_id != "":      # 判斷鍵是否存在
            print("確定刪除{}的資料!：".format(datas.get(key_id)))
            yn=input("(Y/N)?")
            if (yn=="Y" or yn=="y"):
                fb.delete(url + '/' + key_id,None)
                datas.pop(key_id)
                print("資料刪除完畢\n")
        else:
            print("{} 未建立!\n".format(eword)) 


### 主程式從這裡開始 ###

import time,os
from firebase import firebase

url = 'https://chiouapp01-a6172.firebaseio.com/English'
fb = firebase.FirebaseApplication(url, None)
datas=fb.get(url, None)

while True:
    menu()
    choice = input("請輸入您的選擇：")
    try:
        choice = int(choice)
        if choice==1:
            search_data()
        elif choice==2:
            input_data()
        elif choice==3:
            disp_data()
        elif choice==4:
            edit_data()
        elif choice==5:
            delete_data()
        else:
            break
    except:    
        print("\n不合法按鍵!")
        time.sleep(1)
print("程式執行完畢！")