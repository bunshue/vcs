// 動手做15-3：建立微型網站伺服器，動態IP
// 詳細的程式說明，請參閱第十五章，15-29頁。

#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0xF0, 0x7B, 0xCB, 0x4B, 0x7C, 0x9F };

EthernetServer server(80);

void setup() {
  Serial.begin(9600);

  Ethernet.begin(mac);
  IPAddress ip = Ethernet.localIP();
  server.begin();
  
  Serial.print("My IP address: ");
  Serial.print(ip);
}

void loop() {
  EthernetClient client = server.available();

  if (client) {
    while (client.connected()) {
      if (client.available()) {
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println();

          client.println("<h1>Arduino物聯網應用</h1>");
          break;
      }
    }

    delay(1);
    client.stop();
  }
}
