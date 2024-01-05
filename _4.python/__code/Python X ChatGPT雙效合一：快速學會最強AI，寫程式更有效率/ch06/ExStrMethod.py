def EditData():
    if len(strEditTitle) > 0:
        print(strEditTitle)
    else:
        print(strTitle)

    print("作者：", strName)
    print("暱稱：", strId)
    print("Gmail：", strEmail)
    print("興趣：", strJoin)

strTitle = ""
strEditTitle = "撰寫Python小網站"

isEditTitle = str(input("是否要更改名稱(Y/N)："))
isSymbol = str(input("是否要更改前後星號(Y/N)："))

if isEditTitle == "Y" and isSymbol == "Y":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strSymbol = str(input("請輸入欲更改前後符號："))

    strEditTitle = strEditTitle.center(36, strSymbol)
    
elif isEditTitle == "Y" and isSymbol == "N":
    strEditTitle = str(input("請輸入欲更改名稱："))
    strEditTitle = strEditTitle.center(36, "*")

elif isEditTitle == "N" and isSymbol == "Y":
    strSymbol = str(input("請輸入欲更改前後符號："))
    strTitle = strTitle.center(36, strSymbol)

strName = str(input("請輸入名字："))
strId = str(input("請輸入暱稱："))
strEmail = str(input("請輸入Gmail："))

while strEmail.endswith("@gmail.com") == False:
    strEmail = str(input("請重新輸入Gmail："))

strSavor = str(input("你的興趣(以逗號分隔)："))
strJoin = "|".join(strSavor.split(","))


print("="*30, "\n")
EditData()
