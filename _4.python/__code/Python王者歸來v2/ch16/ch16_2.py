# ch16_2.py
def taiwanPhoneNum(string):
    """檢查是否有含手機聯絡資訊的台灣手機號碼格式"""
    if len(string) != 12:       # 如果長度不是12
        return False            # 傳回非手機號碼格式
    
    for i in range(0, 4):       # 如果前4個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格式
        
    if string[4] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式
   
    for i in range(5, 8):       # 如果中間3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格

    if string[8] != '-':        # 如果不是'-'字元
        return False            # 傳回非手機號碼格式

    for i in range(9, 12):      # 如果最後3個字出現非數字字元
        if string[i].isdecimal() == False:
            return False        # 傳回非手機號碼格
    return True                 # 通過以上測試

def parseString(string):
    """解析字串是否含有電話號碼"""
    notFoundSignal = True       # 註記沒有找到電話號碼為True
    for i in range(len(string)):  # 用迴圈逐步抽取12個字元做測試
        msg = string[i:i+12]
        if taiwanPhoneNum(msg):
            print(f"電話號碼是: {msg}")
            notFoundSignal = False        
    if notFoundSignal:          # 如果沒有找到電話號碼則列印
        print(f"{string} 字串不含電話號碼")

msg1 = 'Please call my secretary using 0930-919-919 or 0952-001-001'
msg2 = '請明天17:30和我一起參加明志科大教師節晚餐'
msg3 = '請明天17:30和我一起參加明志科大教師節晚餐, 可用0933-080-080聯絡我'
parseString(msg1)
parseString(msg2)
parseString(msg3)





