from pyfirmata import Arduino, util
from time import sleep
port = 'com10'
board = Arduino(port)
# 等待 pyFirmata 和 Arduino 同步
sleep(3)

# 開啟 Iterator 避免序列溢位
it = util.Iterator(board)
it.start()

A0 = board.get_pin('a:0:i')   # A0 為 Analog 輸入埠
D11 = board.get_pin('d:11:p') # D11 為 PWM

try:
    while True:       
        p = A0.read()  # 讀取 A0 埠
        print(p)
        D11.write(p)
except KeyboardInterrupt:
    board.exit()
