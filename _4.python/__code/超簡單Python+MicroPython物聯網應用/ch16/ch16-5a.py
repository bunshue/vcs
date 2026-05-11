from umqtt.simple import MQTTClient
from machine import Pin, SoftI2C
import ssd1306
import utime
import dht
import xtools

xtools.connect_wifi_led()
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
sensor = dht.DHT11(Pin(22))

# MQTT 客戶端
client = MQTTClient (
    client_id = xtools.get_id(),
    server = "broker.hivemq.com",
    ssl = False,
)
client.connect()  # 連線MQTT
topic_temp = "sensors/123456/temp"
topic_humi = "sensors/123456/humi"
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
        client.publish(topic_temp, str(temp))
        humid = sensor.humidity()
        client.publish(topic_humi, str(humid))
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
