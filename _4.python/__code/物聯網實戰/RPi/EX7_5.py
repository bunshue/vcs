import pyfirmata
from time import sleep
board = pyfirmata.Arduino("/dev/ttyACM0")
button1 = board.get_pin("d:6:i")
button2 = board.get_pin("d:7:i")
LED = board.get_pin("d:13:o")
servo1 = board.get_pin("d:11:s")
it = pyfirmata.util.Iterator(board)
it.start()
debounce1 = 0
debounce2 = 0
maxDebounce = 500
try:
    while True:
        if button1.read() == 0:
            if debounce1 > maxDebounce:
                debounce1 = 0
                servo1.write(90)
                LED.write(True)
                sleep(0.5)
                while button1.read() == 0:
                    pass
            else:
                debounce1 += 1 
        if button2.read() == 0:
            if debounce2 > maxDebounce:
                debounce2 = 0
                servo1.write(0)
                LED.write(False)
                sleep(0.5)
                while button2.read() == 0:
                    pass
            else:
                debounce2 += 1
except KeyboardInterrupt:
    board.exit()
    print('Exit')
finally:
    print('Bye')
