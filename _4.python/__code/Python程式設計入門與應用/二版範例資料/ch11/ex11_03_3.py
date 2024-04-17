import pyfirmata
#from time import sleep
pin_led=10
pin_button=12
LEDState=False
port = 'COM7'
board=pyfirmata.Arduino(port)
print(board.digital[pin_button].read())
button = board.get_pin('d:12:i')
button.enable_reporting
iterator = pyfirmata.util.Iterator(board)
iterator.start()
print(button.read())

#for i in range(100):
#    print ("Button state: %s" % button.read())
#    # The return values are: True False, and None
#    if str(button.read()) == 'True':
#        print ("Button pressed")
#    elif str(button.read()) == 'False':
#        print ("Button not pressed")
#    else:
#        print ("Button was never pressed")
#    board.pass_time(0.5)
#while True:
##    if (board.digital[pin_button].read()==None):
##        sleep(0.05)
##        if (board.digital[pin_button].read()==None):
##            LEDState=not(LEDState)
##            print('改變',LEDState)
##            #board.digital[pin_led].write(LEDState)
##            sleep(0.2)
##            while (board.digital[pin_button].read()==None):
##                sleep(0.01)
##                print('等待',board.digital[pin_button].read())
#    pvalue = board.digital[pin_button].read()
#    print(pvalue)
#    while pvalue is None:
#        pass
#    if pvalue is True:
#        print("Pressed")
#    else:
#        print("no Pressed")
##        
##    if (board.digital[pin_button].read() == None):
##        print("Pressed!")
##        board.digital[pin_button].write(None)
##        print(board.digital[pin_button].read())
##    board.pass_time(1)    
board.exit()
