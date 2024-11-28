import pyfirmata
board = pyfirmata.Arduino("/dev/ttyACM0")
temperature = board.get_pin("a:0:i")
temperature.enable_reporting()
button = board.get_pin("d:6:i")
it = pyfirmata.util.Iterator(board)
it.start()
readyMeasure = False
debounce = 0
maxDebounce = 500
try:
    while True:
        if button.read() == 0:
            if debounce > maxDebounce:
                readyMeasure = True
                debounce = 0
                while button.read() == 0:
                    pass
            else:
                debounce += 1
        if readyMeasure == True:
            temp = temperature.read()
            if temp != None:
                temp = temp*5/0.01
                print("The temperature is {Temp} C".format(Temp=int(temp)))
            readyMeasure = False
except KeyboardInterrupt:
    print('Exit')
finally:
    board.exit()
    print('Bye')
