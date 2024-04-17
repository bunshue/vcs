import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:12:i')
led = board.get_pin('d:10:o')
LEDState = False
while True:
    value = sw.read() 
    sleep(0.05)
    if value == 1:
        if (LEDState == True):
            led.write(0)
            led_s = False            
        else:
            led.write(1)
            led_s = True
board.exit()
