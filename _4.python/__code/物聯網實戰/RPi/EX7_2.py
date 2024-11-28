import pyfirmata
from time import sleep
board = pyfirmata.Arduino("/dev/ttyACM0")
LED = board.get_pin("d:13:o")
button = board.get_pin("d:6:i")
it = pyfirmata.util.Iterator(board)
it.start()
debounce = 0
maxDebounce = 500
try:
    while True:
        if button.read() == 0:
            if debounce > maxDebounce:
                debounce = 0
                for i in range(10):
                    LED.write(True)
                    sleep(0.5)
                    LED.write(False)
                    sleep(0.5)
                for i in range(10):
                    LED.write(True)
                    sleep(0.25)
                    LED.write(False)
                    sleep(0.25)
                while button.read() == 0:
                    pass
            else:
                debounce += 1
except KeyboardInterrupt:
    board.exit()
    print('Exit')
finally:
    print('Bye')
