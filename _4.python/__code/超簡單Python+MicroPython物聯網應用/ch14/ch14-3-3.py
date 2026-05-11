import ESPWebServer
import xtools

ip_address = xtools.connect_wifi_led()
html = """
<html>
<head>
   <meta name="viewport" content="width=device-width,initial-scale=1">
</head>
<body>
   <h1>ESPWebServer: Hello World</h1>
</body>
</html>"""

def handleRoot(socket, args):    
    global html
    ESPWebServer.ok(socket, "200", "text/html", html) 

ESPWebServer.begin(80)              
ESPWebServer.onPath("/", handleRoot)
print("Web伺服器的 IP 位址: ", ip_address)             

while True:
    ESPWebServer.handleClient()
    