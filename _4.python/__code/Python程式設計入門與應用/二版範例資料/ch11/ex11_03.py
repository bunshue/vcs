import pyfirmata

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:12:i')
led = board.get_pin('d:10:o')
led_s = False
while True:
    value = sw.read() 
    if value == 1:
        led.write(1)
    else:
        led.write(0)
board.exit()