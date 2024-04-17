#led燈閃爍，亮10次
import pyfirmata
from time import sleep
pin=12
port = 'COM51'
board=pyfirmata.Arduino(port)
for i in range(1,10):
    board.digital[pin].write(1)
    sleep(0.2)
    board.digital[pin].write(0)
    sleep(0.2)
board.exit()