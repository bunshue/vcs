
try:
    file_object = open('c:/python.txt', "r") 
    print(file_object.read())  
    file_object.close()

except FileNotFoundError:
    print("檔案不存在")

except PermissionError:
    print("權限不足")

except Exception as e:
    print("讀取檔案時發生未知錯誤：", e)









