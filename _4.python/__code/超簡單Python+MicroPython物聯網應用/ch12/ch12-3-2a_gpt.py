from machine import Pin
from umqtt.simple import MQTTClient
import utime

# 連接WiFi
import xtools
xtools.connect_wifi_led()


# MQTT 客戶端設定
client = MQTTClient(
    client_id=xtools.get_id(),
    server="broker.hivemq.com",
    ssl=False,
)

def sub_cb(topic, msg):
    global ledG
    print("收到訊息: ", msg.decode())

client.set_callback(sub_cb)   # 指定回撥函數來接收訊息

# 連線至MQTT Broker
client.connect()

topic = "sensors/1234/temp"
client.subscribe(topic)  # 訂閱主題

while True:
    print("等待訊息...")
    client.check_msg()
    utime.sleep(5)
