from smbus2 import SMBus
import time
import math
import datetime

arduinoAddress = 0x16
a = []
first = True
while True:
    with SMBus(1) as bus:
        bus.write_byte_data(arduinoAddress, 0, 0x73)
        data = bus.read_byte_data(arduinoAddress, 0)
        if data == 0x65:
            if len(a) == 0:
                break
            a.reverse()
            s1 = 0
            for i in range(2,0,-1):
                s1 = s1 + a.pop()*math.pow(0.1,i)
            a.pop()
            for i in range(3):
                s1 = s1 + a.pop()*math.pow(10,i)
            if not first:
                print("Temperature = {:.1f} C".format(s1))
                x = datetime.datetime.now()
                print(" at {0}".format(x.strftime("%c")))
            time.sleep(10)
            a[:]=[]
            first = False
        else:
            a.append(data)

