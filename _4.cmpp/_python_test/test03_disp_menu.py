def disp_menu():
    print("各種網路資料抓取範例")
    print("------------")
    print("1.Yahoo字典1")
    print("2.Yahoo字典2")
    print("3.統一發票號碼")
    print("0.結束")
    print("------------")

def example01():
    print('範例01')

def example02():
    print('範例02')

def example03():
    print('範例02')

def example04():
    print('範例02')

while True:
    disp_menu()
    choice = int(input("請輸入您的選擇:"))
    if choice == 0 :
        break
    if choice == 1: 
        example01()
    elif choice == 2:
        example02()
    elif choice == 3:
        example03()
    elif choice == 4:
        example04()
    else:
        break
    x = input("請按Enter鍵回主選單")







