// 使用Webduino程式庫建立微網站，增加faq.html頁面
// 詳細的程式說明，請參閱第十六章，16-7頁。

#include "SPI.h"
#include "Ethernet.h"
#include "WebServer.h"

static byte mac[] = { 0xF0, 0x7B, 0xCB, 0x4B, 0x7C, 0x9F };
IPAddress ip(192, 168, 1, 25);
IPAddress subnet(255, 255, 255, 0);
IPAddress gateway(192, 168, 1, 1);

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

P(faqPage) = 
    "<!doctype html>"
    "<html><head><meta charset=\"utf-8\" />"
    "<title>微網站FAQ</title>"
    "</head><body>這是FAQ網頁</body></html>";
    
void faqCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  server.httpSuccess();
  if (type != WebServer::HEAD)
  {
    server.printP(faqPage);
  }
}

void setup() {  
  Ethernet.begin(mac, ip, gateway, subnet);
  webserver.setDefaultCommand(&defaultCmd);   // 處理「首頁」請求
  webserver.addCommand("faq.html", &faqCmd);  // 處理「faq頁面」請求
  webserver.begin();
}

void loop() {
  webserver.processConnection();
}
