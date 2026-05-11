from machine import Pin, SoftI2C
import ssd1306
import utime
import dht

i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
sensor = dht.DHT11(Pin(22))

# 顯示專案訊息
oled.fill(0)  # 清除內容
oled.text("Raspberry Pi", 0, 0)
oled.text("Pico W Project", 0, 15)
oled.text("Using SSD1306 &", 0, 30)
oled.text("DHT11 Module", 0, 40)
oled.show()
utime.sleep(3)

count = 0
while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        humid = sensor.humidity()
        oled.fill(0)  # 清除內容
        count = count + 1
        oled.text("(" + str(count) + ")", 0, 0)
        oled.text("= TEMP & HUMID =", 0, 20) 
        oled.text("Temp = {} C".format(temp), 0, 35)
        oled.text("Humid= {} %".format(humid), 0, 50)
        oled.show()
        print("(" + str(count) + ")")
        print("Temp = {} C".format(temp))
        print("Humid= {} %".format(humid))
        utime.sleep(2)
    except OSError as e:
        print("錯誤: DHT11感測器讀取錯誤...")   
