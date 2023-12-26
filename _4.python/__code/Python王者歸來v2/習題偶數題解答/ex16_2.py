# ch16_2.py
def compareString(string):
    """檢查是否是搜尋的字串"""
    if string == searchStr:
        return True
    else:
        return False

def parseString(string):
    global num
    # notFoundSignal = True     # 註記沒有找到電話號碼為True
    for i in range(len(data)):  # 用迴圈逐步抽取字串長度做測試
        msg = data[i:i+len(string)]
        if compareString(msg):
            num += 1

fn = 'ex16_2.txt'
with open(fn) as file_obj:      # 讀取ex21_2.txt
    data = file_obj.read()

while True:
    searchStr = input("請輸入與搜尋字串 : ")
    num = 0
    parseString(searchStr)
    print("所搜尋字串 %s 共出現 %d 次" % (searchStr, num))
    print("\n是否繼續,輸入Y或y則程式繼續")
    again = input("= ")       # 讀取使用者輸入
    if again == 'Y' or again == 'y':    # 若輸入Y或y
        pass
    else:
        break
    
    


