dictStudent = {}

def isHasKeyAndNotNone():
    findKey = str(input("請輸入欲查詢的key："))
    
    if findKey in dictStudent and dictStudent.get(findKey, None) == None:
        EditData(findKey)
        
    elif findKey in dictStudent and dictStudent.get(findKey, None) != None:
        print("%s的值：%s" %(findKey, dictStudent[findKey]))
        CheckOtherKeyValue()
        
    else:
        dictStudent.setdefault(findKey, None)
        print("%s不存在已自動建立key" %(findKey))

def EditData(findKey):
    strInputValue = str(input("請輸入值："))
    dictStudent[findKey] = strInputValue
    CheckOtherKeyValue()

def CheckOtherKeyValue():
    for key, values in dictStudent.items():
        if values == None:
            print(dictStudent)
            strCheck = str(input("目前還有其他欄位值為None，是否繼續進行編輯(Y/N)："))

            while strCheck == "Y":
                isHasKeyAndNotNone()
            else:
                print(dictStudent)
                break

strFieldName = str(input("請輸入欄位名稱(以逗號分隔)："))
dictStudent = dictStudent.fromkeys(strFieldName.split(","))

isHasKeyAndNotNone()
