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
  <script>
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById('status').innerHTML=xhttp.responseText;
      }
    };
    function turnOn() {
      document.getElementById('status').innerHTML = '點亮中...';
      xhttp.open('GET', '/on', true);
      xhttp.send();
    }
    function turnOff() {
      document.getElementById('status').innerHTML = '熄滅中...';
      xhttp.open('GET', '/off', true);
      xhttp.send();
    }
  </script>
</head>
<body>
  <h1>LED: <span id='status'>熄滅</span></h1><hr>
  <p><button style="font-size:40px" onclick='turnOn()'>開啟</button></p>
  <p><button style="font-size:40px" onclick='turnOff()'>關閉</button></p>
</body>
</html>
"""

ledR = Pin(15, Pin.OUT)
ledR.value(0)

def handleRoot(socket, args): 
    global html
    ESPWebServer.ok(socket, "200", "text/html", html)

def handleOn(socket, args): 
    ledR.value(1)   # 點亮LED
    ESPWebServer.ok(socket, "200", "點亮")
    
def handleOff(socket, args):
    ledR.value(0)   # 熄滅LED
    ESPWebServer.ok(socket, "200", "熄滅")
    
ESPWebServer.begin(80)
ESPWebServer.onPath("/", handleRoot)
ESPWebServer.onPath("/on", handleOn)
ESPWebServer.onPath("/off", handleOff)
print("Web伺服器的 IP 位址: ", ip_address)
while True:
    ESPWebServer.handleClient()
    