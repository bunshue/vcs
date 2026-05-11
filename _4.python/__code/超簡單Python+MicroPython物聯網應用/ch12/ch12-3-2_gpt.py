from machine import Pin
from umqtt.simple import MQTTClient
import utime, xtools

xtools.connect_wifi_led()

# MQTT 客戶端
client = MQTTClient(
    client_id=xtools.get_id(),
    server="broker.hivemq.com",
    ssl=False,
)

topic = "sensors/1234/temp"

while True:
    temp = xtools.random_in_range(10, 35)
    client.connect()  # 連線至 MQTT Broker

    print("送出溫度值:", temp)
    client.publish(topic, str(temp))

    client.disconnect()
    utime.sleep(5)


