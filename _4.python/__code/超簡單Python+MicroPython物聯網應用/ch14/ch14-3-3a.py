import ESPWebServer
import xtools

ip_address = xtools.connect_wifi_led()

ESPWebServer.begin(80)              
ESPWebServer.setDocPath("/www") 
print("Web伺服器的 IP 位址: ", ip_address)             

while True:
    ESPWebServer.handleClient()
    