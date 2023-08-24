# ch15_1.py
def division(x, y):
    return x / y

print(division(10, 2))      # 列出10/2
print(division(5, 0))       # 列出5/0
print(division(6, 3))       # 列出6/3


print('------------------------------------------------------------')	#60個






#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_2.py

# ch15_2.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division(6, 3))           # 列出6/3






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_3.py

# ch15_3.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")

print(division(10, 2))          # 列出10/2
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_4.py

# ch15_4.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")
    except TypeError:           # 除法的資料型態不符
        print("除法資料型態不符")

print(division(10, 2))          # 列出10/2
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_5.py

# ch15_5.py
def division(x, y):
    try:                        # try - except指令
        ans =  x / y
    except ZeroDivisionError:   # 除數為0時執行
        print("除數不可為0")
    else:
        return ans              # 傳回正確的執行結果

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division(6, 3))           # 列出6/3






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_6.py

# ch15_6.py

fn = 'data15_6.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    print(data)                 # 輸出變數data相當於輸出檔案







    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_7.py

# ch15_7.py

fn = 'data15_7.txt'             # 設定欲開啟的檔案
try:
    with open(fn) as file_Obj:  # 用預設mode=r開啟檔案,傳回檔案物件file_Obj
        data = file_Obj.read()  # 讀取檔案到變數data
except FileNotFoundError:
    print("找不到 %s 檔案" % fn)
else:
    print(data)                 # 輸出變數data相當於輸出檔案







    

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_8.py

# ch15_8.py
def division(x, y):
    try:                        # try - except指令
        return x / y
    except Exception:           # 通用錯誤使用
        print("通用錯誤發生")

print(division(10, 2))          # 列出10/2
print(division(5, 0))           # 列出5/0
print(division('a', 'b'))       # 列出'a' / 'b'
print(division(6, 3))           # 列出6/3






print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\Python邁向領航者之路_超零基礎\ch15\ch15_9.py

# ch15_9.py
def division(x, y):
    try:                             # try - except指令
        return x / y
    except:                          # 捕捉所有異常
        print("異常發生")
    finally:                         # 離開函數前先執行此程式碼
        print("階段任務完成")

print(division(10, 2),"\n")          # 列出10/2
print(division(5, 0),"\n")           # 列出5/0
print(division('a', 'b'),"\n")       # 列出'a' / 'b'
print(division(6, 3),"\n")           # 列出6/3






print('------------------------------------------------------------')	#60個


