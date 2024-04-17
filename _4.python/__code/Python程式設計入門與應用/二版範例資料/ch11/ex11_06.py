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
