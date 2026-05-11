from umqtt.simple import MQTTClient
import utime, xtools

xtools.connect_wifi_led()

HOST = "mqtt3.thingspeak.com"
CHANNEL_ID = "<CHANNEL ID>"
CLIENT_ID = "<CLIENT_ID>"
USERNAME = "<USERNAME>"
PASSWORD = "<PASSWORD>"

topic = "channels/" + CHANNEL_ID + "/publish"

client = MQTTClient (
    client_id = CLIENT_ID,
    server = HOST,
    user = USERNAME,
    password = PASSWORD,
    ssl = False,
)

while True:
    print("儲存溫度和濕度資料!")
    temp = xtools.random_in_range(10, 35)
    hum = xtools.random_in_range(60, 90)
    print(temp, hum)
    payload = "field1="+str(temp)+"&field2="+str(hum)
    client.connect()
    client.publish(topic, payload)
    client.disconnect()
    utime.sleep(15)
    