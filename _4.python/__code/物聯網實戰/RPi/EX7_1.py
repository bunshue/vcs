import smbus
import time
import math
import datetime
bus = smbus.SMBus(1)
arduinoAdr = 0x16
a = []
def main():
    bus.write_byte(arduinoAdr, 0x73)
    while 1:
        data = bus.read_byte(arduinoAdr)
        if data == 0x65:
            a.reverse()
            s1 = 0
            for i in range(2,0,-1):
                s1 = s1 + a.pop()*math.pow(0.1,i)
            a.pop()
            for i in range(3):
                s1 = s1 + a.pop()*math.pow(10,i)
            print("Temperature = {:.1f} C".format(s1))
            x = datetime.datetime.now()
            print(" at {0}".format(x.strftime("%c")))
            time.sleep(10)
            bus.write_byte(arduinoAdr, 0x73)
            a[:]=[]
        elif data == 0x61:
            bus.write_byte(arduinoAdr, 0x73)
        else:
            a.append(data)
        #time.sleep(1)
while True:
    main()
