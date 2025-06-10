from machine import Pin,Timer
import dht,time     

temp,hum=0,0
d = dht.DHT11(Pin(0)) #在D3建立DHT11物件
led = Pin(2, Pin.OUT) #D4內建Led

def readdht(t):
    global temp,hum
    try:
        d.measure()  #重新測量溫溼度
        temp=d.temperature()       #讀取攝氏溫度
        hum=d.humidity()           #讀取相對溼度
        print("溫    度: %3.1f °C" % temp)
        print("相對溼度: %3.1f %% RH" % hum)
    except:
        print('讀取不正常!')  

timer = Timer(1)
timer.init(period=2000, mode=Timer.PERIODIC, callback=readdht)

try:
    while True:
        if temp>24: # 溫度>24度，開燈
            led.value(0)
        else: # 溫度<24度，熄燈
            led.value(1)
        time.sleep(0.1) #暫停 0.1 秒
except:
    timer.deinit()
    print('stopped')  