import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
startPin = 4
stopPin = 17
LEDPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(startPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup( stopPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup( LEDPin, GPIO.OUT)
GPIO.output(LEDPin, False)
def on_message(client, userdata, msg):
   print(str(msg.topic) + " " + str(msg.payload.decode("utf-8")))
RPiClient = mqtt.Client()
RPiClient.connect("192.168.1.104", 1883)
RPiClient.on_message = on_message
RPiClient.subscribe("ack")
RPiClient.loop_start()
RPiClient.publish('commands', '0')
debounceStart = 0
debounceStop  = 0
maxDebounce   = 100
try:
   while True:
      if GPIO.input(startPin) == 0:
          if debounceStart > maxDebounce:
             GPIO.output(LEDPin, True)
             debounceStart = 0
             RPiClient.publish('commands', '1')
             while GPIO.input(startPin) == 0:
                pass
          else:
              debounceStart += 1
      if GPIO.input(stopPin) == 0:
          if debounceStop > maxDebounce:
              GPIO.output(LEDPin, False)
              debounceStop = 0
              RPiClient.publish('commands', '0')
              while GPIO.input(stopPin) == 0:
                  pass
          else:
              debounceStop += 1
except KeyboardInterrupt:
   RPiClient.loop_stop()
   RPiClient.disconnect()
   print('Exit')
finally:
   GPIO.cleanup()
