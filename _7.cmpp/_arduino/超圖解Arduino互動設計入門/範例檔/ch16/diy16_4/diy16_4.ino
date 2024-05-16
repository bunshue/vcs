// 動手做16-4：從瀏覽器控制遠端的燈光開關
// 詳細的程式說明，請參閱第十六章，16-28頁。

#include "SPI.h"
#include "Ethernet.h"
#include "WebServer.h"
#include "Streaming.h"

const byte LED_PIN = 8;
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

void defaultCmd(WebServer &server, WebServer::ConnectionType type)
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
    
void faqCmd(WebServer &server, WebServer::ConnectionType type)
{
  server.httpSuccess();
  if (type != WebServer::HEAD)
  {
    server.printP(faqPage);
  }
}

P(FORM) =
  "<form method=\"post\" action=\"sw\">"
  "訊息：<input name=\"msg\" type=\"text\"><br>"
  "燈光：<input name=\"light\" type=\"radio\" value=\"ON\"> 開"
  "<input name=\"light\" type=\"radio\" value=\"OFF\" checked> 關"
  "<br><br><input type=\"submit\" name=\"button\" value=\"送出\">"
  "</form>";

void formCmd(WebServer &server, WebServer::ConnectionType type)
{
  server.httpSuccess();

  if (type != WebServer::HEAD)
  {
    server.printP(htmlHead);
    server.printP(FORM);
    server.printP(htmlFoot);
  }
}

void postCmd(WebServer &server, WebServer::ConnectionType type)
{
  char name[16], value[16];
  server.httpSuccess();

  if (type == WebServer::POST)
  {
    server.printP(htmlHead);
    while (server.readPOSTparam(name, 16, value, 16)){
      if (strcmp(name, "msg") == 0) {
        server << "<h1>" << value << "</h1>";
      }

      if (strcmp(name, "light") == 0) {
        server << "<p>燈光已經";
        if (strcmp(value, "ON") == 0) {
          server << "打開。</p>";
          digitalWrite(LED_PIN, HIGH);
        } else {
          server << "關閉。</p>";
          digitalWrite(LED_PIN, LOW);
        }
      }
    }
    server.printP(htmlFoot);
  }
}

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Ethernet.begin(mac, ip, gateway, subnet);
  webserver.setDefaultCommand(&defaultCmd);     // 處理「首頁」請求
  webserver.addCommand("faq.html", &faqCmd);    // 處理「faq頁面」請求
  webserver.addCommand("sw", &postCmd);         // 處理「sw表單處理頁面」請求
  webserver.addCommand("form.html", &formCmd);  // 處理「表單頁面」請求
  webserver.begin();
}

void loop() {
  webserver.processConnection();
}
