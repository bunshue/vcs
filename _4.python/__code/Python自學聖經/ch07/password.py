import msvcrt
def pwd_input():  
    chars = [] 
    while True:
        try:
            newChar = msvcrt.getch().decode(encoding="utf-8")
        except:
            return input("請在cmd命令行下執行，否則密碼輸入將無法隱藏:")
        if newChar in '\r\n': # 如果是換行，结束輸入             
             break 
        elif newChar == '\b': # 如果是退格，删除密碼末尾一位並且删除一個星號
             if chars:  
                 del chars[-1] 
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 游標退回一格
                 msvcrt.putch( ' '.encode(encoding='utf-8')) # 输出一個空格覆蓋原來的星號
                 msvcrt.putch('\b'.encode(encoding='utf-8')) # 游標退回一格準備接受新的输入                 
        else:
            chars.append(newChar)
            msvcrt.putch('*'.encode(encoding='utf-8')) # 顯示 * 號
    return (''.join(chars) )