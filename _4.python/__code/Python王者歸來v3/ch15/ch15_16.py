# ch15_16.py
import traceback                            # 導入taceback

def passWord(pwd):
    """檢查密碼長度必須是5到8個字元"""
    pwdlen = len(pwd)                       # 密碼長度
    if pwdlen < 5:                          # 密碼長度不足            
        raise Exception('密碼長度不足')
    if pwdlen > 8:                          # 密碼長度太長
        raise Exception('密碼長度太長')
    print('密碼長度正確')

for pwd in ('aaabbbccc', 'aaa', 'aaabbb'):  # 測試系列密碼值
    try:
        passWord(pwd)
    except Exception as err:
        errlog = open('errch15_16.txt', 'a')   # 開啟錯誤檔案
        errlog.write(traceback.format_exc())   # 寫入錯誤檔案
        errlog.close()                         # 關閉錯誤檔案
        print("將Traceback寫入錯誤檔案errch15_16.txt完成")
        print("密碼長度檢查異常發生: ", str(err))


