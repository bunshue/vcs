import paho.mqtt.client as mqtt
import random
import time
def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode('utf-8')
    print(str(msg.topic) + " " + str(msg.payload))
    str1 = random.randint(0,3)
    time.sleep(1)
    RPiClient.publish('commands', str(str1))
RPiClient = mqtt.Client()
RPiClient.connect("192.168.1.104", 1883)
RPiClient.on_message = on_message
RPiClient.subscribe("ack")
RPiClient.loop_start()
RPiClient.publish('commands', '0')
while True:
    time.sleep(1)