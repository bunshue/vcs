// 使用Webduino程式庫建立微網站，增加faq.html頁面
// 詳細的程式說明，請參閱第十六章，16-7頁。

#include "SPI.h"
#include "Ethernet.h"
#include "WebServer.h"
#include "Streaming.h"

static byte mac[] = { 0xF0, 0x7B, 0xCB, 0x4B, 0x7C, 0x9F };
IPAddress ip(192, 168, 1, 25);
IPAddress subnet(255, 255, 255, 0);
IPAddress gateway(192, 168, 1, 1);

WebServer webserver("", 80);

P(htmlHead) =
 "<!doctype html><html>"
 "<head><meta charset=\"utf-8\">"
 "<title>Arduino 微網站</title>"
 "</head><body>" ;
 
P(htmlFoot) = "</body></html>";

P(homePage) = "這是微網站的首頁。";

void defaultCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  server.httpSuccess();
  
  if (type != WebServer::HEAD) 
  {
    server.printP(htmlHead);
    server.printP(homePage);
    server.printP(htmlFoot);
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

void postCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  char name[16];
  char value[16];
  server.httpSuccess();

  if (type == WebServer::POST)
  {
    server.printP(htmlHead);
    while (server.readPOSTparam(name, 16, value, 16)){
       server << "<p>參數 </p>" << name << " 的值是" << value << "</p>";
    }
    server.printP(htmlFoot);
  }
}

P(FORM) =
  "<form method=\"post\" action=\"sw\">"
  "訊息：<input name=\"msg\" type=\"text\"><br>"
  "燈光：<input name=\"light\" type=\"radio\" value=\"ON\"> 開"
  "<input name=\"light\" type=\"radio\" value=\"OFF\" checked> 關"
  "<br><br><input type=\"submit\" name=\"button\" value=\"送出\">"
  "</form>";

void formCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  server.httpSuccess();

  if (type != WebServer::HEAD)
  {
    server.printP(htmlHead);
    server.printP(FORM);
    server.printP(htmlFoot);
  }
}

void setup() {  
  Ethernet.begin(mac, ip, gateway, subnet);
  webserver.setDefaultCommand(&defaultCmd);   // 處理「首頁」請求
  webserver.addCommand("faq.html", &faqCmd);  // 處理「faq頁面」請求
  webserver.addCommand("sw", &postCmd);       // 處理「sw表單處理頁面」請求
  webserver.addCommand("form.html", &formCmd);
  webserver.begin();
}

void loop() {
  webserver.processConnection();
}
