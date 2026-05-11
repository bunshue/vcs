from machine import Pin 
from umqtt.simple import MQTTClient
import utime, xtools

xtools.connect_wifi_led()
ledG = Pin(12, Pin.OUT)
ledG.value(0)

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
    global ledG
    print("收到訊息: ", msg.decode())
    if msg.decode() == "ON":
        ledG.value(1)
    if msg.decode() == "OFF":
        ledG.value(0)

client.set_callback(sub_cb)   # 指定回撥函數來接收訊息
client.connect()              # 連線

topic = ADAFRUIT_AIO_USERNAME + "/feeds/" +FEED
print(topic)
client.subscribe(topic)      # 訂閱主題

while True:
    print("送出訊息: ON")
    client.publish(topic, "ON")
    utime.sleep(2)
    client.check_msg()
    print("送出訊息: OFF")
    client.publish(topic, "OFF")
    utime.sleep(2)
    client.check_msg() 