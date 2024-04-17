# ex11_02.py
import pyfirmata
pin = 13
port = 'COM7'
board=pyfirmata.Arduino(port)
board.digital[pin].write(1)
board.digital[pin].write(0)
board.exit()
