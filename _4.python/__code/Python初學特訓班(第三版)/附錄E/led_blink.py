#pip install pyfirmata
from pyfirmata import Arduino
from time import sleep
PORT="com10"
board=Arduino(PORT)
# 等待 pyFirmata 和 Arduino 同步
sleep(1)
while True:
    # D10 未設定，預設為 OUTPUT
    board.digital[10].write(1) 
    sleep(1)
    board.digital[10].write(0)
    sleep(1)