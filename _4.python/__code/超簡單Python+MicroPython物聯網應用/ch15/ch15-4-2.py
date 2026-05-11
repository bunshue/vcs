from hcsr04 import HCSR04
import utime

sensor = HCSR04(trigger_pin=11, echo_pin=10)

while True: 
    distance = sensor.distance_cm()
    print(distance, "cm")
    utime.sleep(1)
    