def menu():
    os.system("cls")
    print("帳號、密碼管理系統")
    print("-------------------------")
    print("1. 新增帳號、密碼")
    print("2. 顯示帳號、密碼")
    print("3. 修  改  密  碼")
    print("4. 刪除帳號、密碼")
    print("0. 結  束  程  式")
    print("-------------------------")
        
def disp_data():
    cursor = conn.execute('SELECT * FROM password')
    print("帳號\t密碼")
    print("================")
    for row in cursor:
        print("{}\t{}".format(row[0],row[1]))
    input("按任意鍵返回主選單")        
    
def input_data():       
    while True:
        name = input("請輸入帳號(Enter==>停止輸入)")
        if name == "": break
        sqlstr = "SELECT * FROM password WHERE name='{}'".format(name)
        cursor = conn.execute(sqlstr) 
        row = cursor.fetchone()
        if not row == None:
            print("{} 帳號已存在!".format(name))
            continue
        password = input("請輸入密碼：")        
        sqlstr = "INSERT INTO password VALUES('{}','{}');".format(name,password)
        conn.execute(sqlstr)
        conn.commit()  
        print("{} 已儲存完畢".format(name))    
    
def edit_data():
    while True:
        name = input("請輸入要修改的帳號(Enter==>停止輸入)")
        if name == "":
            break
        sqlstr = "SELECT * FROM password WHERE name='{}'".format(name)
        cursor = conn.execute(sqlstr) 
        row = cursor.fetchone()
        #print(row)
        if row == None:
            print("{} 帳號不存在!".format(name))
            continue
        print("原來密碼為：{}".format(row[1]))
        password = input("請輸入新密碼：")
        sqlstr = "UPDATE password SET pass='{}' WHERE name='{}'".format(password, name)
        conn.execute(sqlstr)
        conn.commit()        
        input("密碼更改完畢，請按任意鍵返回主選單") 
        break      
    
def delete_data():
    while True:
        name = input("請輸入要刪除的帳號(Enter==>停止輸入)")
        if name == "":
            break
        sqlstr="SELECT * FROM password WHERE name='{}'" .format(name)
        cursor=conn.execute(sqlstr) 
        row = cursor.fetchone()
        if row == None:
            print("{} 帳號不存在!".format(name))
            continue
        print("確定刪除{}的資料!：".format(name))
        yn = input("(Y/N)?")
        if (yn == "Y" or yn == "y"):
            sqlstr = "delete from password where name='{}'".format(name)
            conn.execute(sqlstr)
            conn.commit()
            input("已刪除完畢，請按任意鍵返回主選單") 
            break

### 主程式從這裡開始 ###

import os,sqlite3

db_filename = 'C:/_git/vcs/_1.data/______test_files1/_db/python02.sqlite';

conn = sqlite3.connect(db_filename)
while True:
    menu()
    choice = int(input("請輸入您的選擇："))
    print()
    if choice==1:
        input_data()
    elif choice==2:
        disp_data()
    elif choice==3:
        edit_data()
    elif choice==4:
        delete_data()
    else:
        break    

conn.close()
print("程式執行完畢！")
