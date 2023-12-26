# ch11_27.py
def printmsg( ):
    """ 函數本身沒有定義變數, 只有執行列印全域變數功能 """
    print("函數列印: ", msg)    # 列印全域變數

msg = 'Global Variable'         # 設定全域變數
print("主程式列印: ", msg)      # 列印全域變數
printmsg( )                     # 呼叫函數


