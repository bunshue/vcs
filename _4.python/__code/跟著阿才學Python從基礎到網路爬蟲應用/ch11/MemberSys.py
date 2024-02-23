import os
import json

#新增員工記錄函式
def fnCreate(): 
    uid = input('編號：')
    if uid in listUid:
        print('編號重複，無法在記憶體中新增員工記錄')
        return 
    name=input('姓名︰')
    salary=int(input('薪資︰'))
    newMember={'編號':uid,'姓名':name,'薪資':salary}
    listMember.append(newMember)
    listUid.append(uid)
    print("記憶體新增編號 %s 的員工記錄" %(uid))
#修改員工記錄函式
def fnUpdate():
    uid = input('編號：')
    for member in listMember:
        if member["編號"]==uid:
           name=input('姓名︰')
           salary=int(input('薪資︰'))
           newMember={'編號':uid,'姓名':name,'薪資':salary}
           cIndex=listMember.index(member)
           listMember[cIndex]=newMember
           print("記憶體修改編號 %s 的員工記錄" %(uid))
           break
    else:
        print("查無編號，無法修改記憶體中的員工記錄")   
#刪除員工記錄函式
def fnDelete():
    uid = input('編號：')
    for member in listMember:
        if member["編號"]==uid:
            listMember.remove(member)
            listUid.remove(uid)
            print("記憶體刪除編號 %s 的員工記錄" %(uid))
            break
    else:
        print("查無編號，無法刪除記憶體中的員工記錄")
#顯示員工記錄函式
def fnPrintMember():
    if len(listMember)==0:
        print("記憶體中目前無員工記錄")
        return 
    for member in listMember:
        for key in member:
            print(member[key], end='\t')
        print()
#員工記錄儲存至MemberInfo.json的函式        
def fnSaveJSONFile():
    f=open(jsonfile,"w",encoding="utf_8")
    json.dump(listMember, f ,ensure_ascii=False, indent=4)
    f.close() 
    print("記憶體中的員工記錄成功儲存至 %s 檔案" %(jsonfile))
            
jsonfile = "MemberInfo.json"  
listMember=[]
listUid=[]
if os.path.exists(jsonfile):
    f=open('MemberInfo.json', 'r', encoding='utf_8')
    listMember=json.load(f)
    listUid=[]    
    for member in listMember:
        listUid.append(member['編號'])
    f.close()

# 主程式
print("======= DTC員工管理系統 =======")
while True:
   option=int(input('系統功能->1.新增 2.修改 3.刪除 4.查詢 5.儲存JSON檔案 其他.離開：'))
   if option==1:
       fnCreate()
   elif option==2:
       fnUpdate()
   elif option==3:
       fnDelete()
   elif option==4:
       fnPrintMember()
   elif option==5:
       fnSaveJSONFile()
   else:
       print("離開系統")
       break;



