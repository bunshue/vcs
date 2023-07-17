import Adafruit_DHT as Ada

sensor = Ada.DHT11
pin = 4
while True:
    humi, temp = Ada.read_retry(sensor, pin, delay_seconds=5)
    if (humi, temp) != (None, None):
        print('溫度:{:.1f}, 濕度:{:.0f}%'.format(humi, temp))
