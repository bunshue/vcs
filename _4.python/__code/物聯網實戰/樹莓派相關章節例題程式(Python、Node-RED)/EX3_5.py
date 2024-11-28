import time
import adafruit_dht
import board

dht = adafruit_dht.DHT22(board.D18, use_pulseio=False)
count = 0

print('Temperature and humidity are measuring...')
while True:
    try:
        print(time.asctime())
        temp = dht.temperature
        humi = dht.humidity
        print('Temperature={0:0.1f}C Humidity={1:0.1f}%'.format(temp, humi))
        time.sleep(10.0)
    except RuntimeError:
        time.sleep(2.0)
        continue
    except KeyboardInterrupt:
        print("Exit!")

