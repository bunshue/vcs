from pyfirmata import Arduino,util
from time import sleep
port = 'com10'
board = Arduino(port)
# 等待 pyFirmata 和 Arduino 同步
sleep(1)

# 開啟 Iterator 避免序列溢位
it = util.Iterator(board)
it.start()

D2 = board.get_pin('d:2:i')  # D2 為 intput
try:
    while True:
        p = D2.read() # 讀取 D2
        print(p)
        if p==True:
            board.digital[11].write(1) 
        else:
            board.digital[11].write(0) 
except KeyboardInterrupt:
    board.exit()