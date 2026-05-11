import ESPWebServer
from machine import Pin
import xtools

ip_address = xtools.connect_wifi_led()
html= """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
</head>
<body>
  <h1>LED 狀態: <strong>{0}</strong></h1><hr>
  <p><a href='/?led=on'><button style="font-size:40px">開啟</button></a></p>
  <p><a href='/?led=off'><button style="font-size:40px">關閉</button></a></p>
</body>
</html>
"""

ledR = Pin(15, Pin.OUT)
ledR.value(0)

def handleCmd(socket, args): 
    global html
    state = "熄滅"
    if "led" in args: 
        if args["led"] == "on": 
            ledR.value(1) 
            state = "點亮"
        elif args["led"] == "off":
            ledR.value(0) 
            state = "熄滅"
    response = html.format(state)
    ESPWebServer.ok(socket, "200", "text/html", response)

ESPWebServer.begin(80)   
ESPWebServer.onPath("/", handleCmd) 
print("Web伺服器的 IP 位址: ", ip_address)  

while True:
    ESPWebServer.handleClient()
    