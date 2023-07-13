import msvcrt

print('要在cmd下執行')

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

print('請輸入密碼 : ')
pwd = pwd_input()
print('\n取得從command line輸入的密碼 : ', pwd)

#以下為從cmd視窗操作時用
print('\nmsvcrt操作')
print('輸出字元')
msvcrt.putch(b'g')
msvcrt.putch(b'o')
msvcrt.putch(b'o')
msvcrt.putch(b'd')
'''
msvcrt.putch('g')
msvcrt.putch('u')
msvcrt.putch('y')
'''
print('按任意鍵繼續')
ans = msvcrt.getch()
print('你按了 : ', ans)
