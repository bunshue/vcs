import pyfirmata
import random
import time
board = pyfirmata.Arduino("/dev/ttyACM0")
r = board.get_pin("d:9:p")
g = board.get_pin("d:10:p")
b = board.get_pin("d:11:p")
it = pyfirmata.util.Iterator(board)
it.start()
try:
    while True:
        rv = random.random()
        gv = random.random()
        bv = random.random()
        r.write(rv)
        g.write(gv)
        b.write(bv)
        time.sleep(1)
except KeyboardInterrupt:
    board.exit()
    print('Exit')
finally:
    print('Bye')
