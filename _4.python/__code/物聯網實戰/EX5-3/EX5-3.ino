#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define LEDPin1 D0
#define LEDPin2 D1
const char* ssid = "urWiFiAccount";//請查無線網路名稱
const char* password = "urPassword"; //請查密碼
const char* mqttServer = "192.168.1.105"; //請確認
WiFiClient wifiClient1;
PubSubClient mqttClient1(wifiClient1);
void receivedCMD(char* topic, byte* payload, unsigned int noChar) {
  char temp[10];
  char *response=temp;
  char LED = (char) payload[0];
  Serial.println(LED);
  if ( LED == '1') {
    digitalWrite(LEDPin1, HIGH);
    digitalWrite(LEDPin2, LOW);   
    response = "OK 1";
  } 
  else if ( LED == '2')  {
    digitalWrite(LEDPin1, LOW);
    digitalWrite(LEDPin2, HIGH);  
    response = "OK 2";
  }
  else if ( LED == '3')  {
    digitalWrite(LEDPin1, HIGH); 
    digitalWrite(LEDPin2, HIGH); 
    response = "OK 3";
  }
  else if ( LED == '0') {
    digitalWrite(LEDPin1, LOW);
    digitalWrite(LEDPin2, LOW);
    response = "OK 0";
  }
  else {
    response = "Not OK";
  }
  mqttClient1.publish("ack", response);
}
void setup() {
  pinMode(LEDPin1, OUTPUT);    
  pinMode(LEDPin2, OUTPUT);
  Serial.begin(9600);
  WiFi.begin(ssid, password);
  mqttClient1.setServer(mqttServer, 1883);
  mqttClient1.setCallback(receivedCMD);
}
void loop() {
  while( !mqttClient1.connected()) {
    mqttClient1.connect("ESP8266");
    mqttClient1.subscribe("commands");
   }
  mqttClient1.loop();
}
