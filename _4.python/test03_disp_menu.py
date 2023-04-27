def disp_menu():
    print('各種網路資料抓取範例')
    print('------------------------')
    print('1.Yahoo字典1')
    print('2.Yahoo字典2')
    print('3.統一發票號碼')
    print('4.世界地震資料 json格式')
    print('5.台灣樂透開彩')
    print('6.取得氣象資料')
    print('7.蘋果日報標題')
    print('0.結束')
    print('------------------------')

def example01():
    print('範例01')

def example02():
    print('範例02')

def example03():
    print('範例03')

def example04():
    print('範例04')

def example05():
    print('範例05')

def example06():
    print('範例06')

def example07():
    print('範例07')

def example08():
    print('範例08')

def example09():
    print('範例09')

while True:
    print()
    disp_menu()
    sel = input("請輸入您的選擇:")
    if sel < '0' or sel > '9':
        continue
    
    choice = int(sel)
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
    elif choice == 5:
        example05()
    elif choice == 6:
        example06()
    elif choice == 7:
        example07()
    elif choice == 8:
        example08()
    elif choice == 9:
        example09()
    else:
        break


