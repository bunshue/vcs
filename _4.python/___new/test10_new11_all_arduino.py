"""
相關抽出


arduino serial pyfirmata microbit


"""


import pyfirmata

print("------------------------------------------------------------")  # 60個

import serial
ser = serial.Serial('COM7')  # open serial port
print(ser.port)
print(ser.baudrate)
print(ser.bytesize)
print(ser.parity)
print(ser.timeout)
ser.close()             # close port

print("------------------------------------------------------------")  # 60個



import pyfirmata
pin = 13
port = 'COM7'
board=pyfirmata.Arduino(port)
board.digital[pin].write(1)
board.digital[pin].write(0)
board.exit()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import pyfirmata
from time import sleep

board = pyfirmata.Arduino('COM7')
it = pyfirmata.util.Iterator(board)
it.start()

sw = board.get_pin('d:12:i')
led = board.get_pin('d:10:o')
led_s = False
while True:
    value = sw.read() 
    sleep(0.05)
    if value == 1:
        if (led_s == True):
            led.write(0)
            led_s = False            
        else:
            led.write(1)
            led_s = True
#    else:
#        led.write(0)
board.exit()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

import tkinter
import pyfirmata
from time import sleep
pin=10
port = 'COM7'
board=pyfirmata.Arduino(port)
sleep(5)
top=tkinter.Tk()
top.minsize(300,20)
def onPress():
    board.digital[pin].write(1)
def offPress():
    board.digital[pin].write(0)
onButton=tkinter.Button(top,text="打開LED燈",command=onPress)
offButton=tkinter.Button(top,text="關閉LED燈",command=offPress)
onButton.pack()
offButton.pack()
top.mainloop()
board.exit()

print("------------------------------------------------------------")  # 60個

import serial
ser = serial.Serial('COM7',115200)  # open serial port
print(ser.name)         # check which port was really used
ser.write(b'hello')     # write a string
ser.close()             # close port
#while True:
#    print(ser.readline())
    
    
    
import pyfirmata
from time import sleep
pin=11
port = 'COM51'
board=pyfirmata.Arduino(port)
while True:
    board.digital[pin].write(1)
    sleep(0.2)
    board.digital[pin].write(0)
    sleep(0.2)
board.exit()

print("------------------------------------------------------------")  # 60個

import tkinter
import pyfirmata
from time import sleep
pin=10
port = 'COM7'
board=pyfirmata.Arduino(port)
sleep(5)
top=tkinter.Tk()
top.minsize(300,20)
def onPress():
    board.digital[pin].write(1)
def offPress():
    board.digital[pin].write(0)
onButton=tkinter.Button(top,text="on",command=onPress)
offButton=tkinter.Button(top,text="off",command=offPress)
onButton.pack()
offButton.pack()
top.mainloop()
board.exit()

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

# This code is supporting material for the book
# Python Programming for Arduino
# by Pratik Desai
# published by PACKT Publishing

from pyfirmata import Arduino
from time import sleep


# This function performs buzzer patterns according to given parameters
def buzzerPattern(pin, recurrence, pattern):
    # Defining patterns by array of time delays
    pattern1 = [0.8, 0.2,0.6, 0.8,0.7,0.5,0.7]
    pattern2 = [0.2, 0.8]
    flag = True

    # Running the loop for given repetition
    for i in range(recurrence):
        if pattern == 1:
            p = pattern1
        elif pattern == 2:
            p = pattern2
        else:
            print ("Please enter valid pattern. 1 or 2.")
            exit

        # Follow pattern p to turn the buzzer on/off for time delay
        for delay in p:
            if flag is True:
                # Buzzer is on
                board.digital[pin].write(1)
                flag = False
                sleep(delay)

            else:
                # Buzzer is off
                board.digital[pin].write(0)
                flag = True
                sleep(delay)

    # Silent buzzer at the end of the pattern repetition
    board.digital[pin].write(0)
    board.exit()


# Setting up the Arduino board
port = 'COM7'
board = Arduino(port)
# Need to give some time to pyFirmata and Arduino to synchronize
sleep(5)

notes = [ 261, 294, 330, 349, 392, 440, 494, 523 ]
# Execute the 'buzzerPattern' function with custom parameters
#buzzerPattern(10, 2, 1)

print("------------------------------------------------------------")  # 60個

from microbit import *
while True:
	display.show(Image('11111:22222:33333:44444:55555'))
	sleep(2000)

print("------------------------------------------------------------")  # 60個

from microbit import *
while True:
	display.show([Image.HEART, Image.HEART_SMALL])
	sleep(2000)

print("------------------------------------------------------------")  # 60個

from microbit import *
compass.calibrate()
while True:
	needle = ((15 - compass.heading()) // 30) % 12
	display.show(Image.ALL_CLOCKS[needle])

print("------------------------------------------------------------")  # 60個

from microbit import *
while True:
	display.scroll(str(temperature()))
	sleep(500)

print("------------------------------------------------------------")  # 60個

from machine import pin
import dht
d = dht.DHT11(Pin(2))

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
