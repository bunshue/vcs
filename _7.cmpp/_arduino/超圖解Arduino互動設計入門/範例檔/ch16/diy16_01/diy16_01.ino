// 使用Webduino程式庫建立微網站
// 詳細的程式說明，請參閱第十六章，16-2頁。

#include "SPI.h"
#include "Ethernet.h"
#include "WebServer.h"

static byte mac[] = { 0xF0, 0x7B, 0xCB, 0x4B, 0x7C, 0x9F };

WebServer webserver("", 80);

P(homePage) = 
    "<!doctype html>"
    "<html><head><meta charset=\"utf-8\" />"
    "<title>Arduino微網站</title>"
    "</head><body>"
    "這是微網站的首頁。"
    "</body></html>";

void defaultCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  server.httpSuccess();
  
  if (type != WebServer::HEAD) 
  {
    server.printP(homePage);
  }
}

void setup() {  
  Ethernet.begin(mac);
  webserver.setDefaultCommand(&defaultCmd);   // 處理「首頁」請求
  webserver.begin();
}

void loop() {
  webserver.processConnection();
}
