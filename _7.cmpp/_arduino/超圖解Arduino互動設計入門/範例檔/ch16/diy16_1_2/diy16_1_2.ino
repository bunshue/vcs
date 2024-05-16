// 動手做16-1：監控遠端的溫濕度值，輸出小數點。
// 詳細的程式說明，請參閱第十六章，16-11頁。

#include "SPI.h"
#include "Ethernet.h"
#include "WebServer.h"
#include "Streaming.h"   // 引用處理字串的程式庫（參閱下文說明）
#include "dht11.h"

dht11 DHT11;            // 宣告 DHT11 程式物件
const byte dataPin = 2; // 宣告 DHT11 模組的資料輸入腳位

static byte mac[] = { 0xF0, 0x7B, 0xCB, 0x4B, 0x7C, 0x9F };
IPAddress ip(192, 168, 1, 25);
IPAddress subnet(255, 255, 255, 0);
IPAddress gateway(192, 168, 1, 1);

WebServer webserver("", 80);

P(htmlHead) =
 "<!doctype html><html>"
 "<head><meta charset=\"utf-8\">"
 "<title>Arduino 溫濕度計</title>"
 "</head><body>" ;
 
P(htmlFoot) = "</body></html>";

void defaultCmd(WebServer &server, WebServer::ConnectionType type, char *, bool)
{
  int chk = DHT11.read(dataPin);
  char buffer[5] = "";
  server.httpSuccess();

  if (type != WebServer::HEAD){
    server.printP(htmlHead);

    if (chk == 0) {
      server << "<h1>溫濕度計</h1>";
      server << "<p>溫度：" << dtostrf(DHT11.temperature, 5, 2, buffer)
             << "&deg;C</p>";
      server << "<p>濕度：" << dtostrf(DHT11.humidity, 5, 2, buffer) 
             << "%</p>";
    } else {
      server << "<h1>無法讀取溫濕度值</h1>";
    }
    server.printP(htmlFoot);
  }
}

void setup() {  
  Ethernet.begin(mac, ip, gateway, subnet);
  webserver.setDefaultCommand(&defaultCmd);   // 處理「首頁」請求
  webserver.begin();
}

void loop() {
  webserver.processConnection();
}
