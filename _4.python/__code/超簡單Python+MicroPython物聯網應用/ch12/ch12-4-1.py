from machine import Pin 
from umqtt.simple import MQTTClient
import utime, xtools

xtools.connect_wifi_led()
ledR = Pin(15, Pin.OUT)
ledR.value(0)

ADAFRUIT_AIO_USERNAME = "<USERNAME>"
ADAFRUIT_AIO_KEY = "<AIO KEY>"
FEED = "lights"

# MQTT 客戶端
client = MQTTClient (
    client_id = xtools.get_id(),
    server = "io.adafruit.com",
    user = ADAFRUIT_AIO_USERNAME,
    password = ADAFRUIT_AIO_KEY,
    ssl = False,
)

def sub_cb(topic, msg):
    if msg.decode() == "ON":
        ledR.value(1)
    elif msg.decode() == "OFF":
        ledR.value(0)
    print("收到訊息: ", msg.decode())

client.set_callback(sub_cb)   # 指定回撥函數來接收訊息
client.connect()              # 連線

topic = ADAFRUIT_AIO_USERNAME + "/feeds/" +FEED
print(topic)
client.subscribe(topic)      # 訂閱主題

while True:
    client.check_msg()
    utime.sleep(1) 