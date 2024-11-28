#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define LEDPin1 D0
#define LEDPin2 D1
const char* ssid = "mayandtclin";
const char* password = "46101222";
const char* mqttServer = "192.168.1.103";
WiFiClient wifiClient1;
PubSubClient mqttClient1(wifiClient1);
void receivedCMD(char* topic, byte* payload, unsigned int noChar) {
  char LED = (char) payload[0];
  if ( LED == '1') {
    digitalWrite(LEDPin1, HIGH);
    digitalWrite(LEDPin2, LOW);   
  } 
  else if ( LED == '2')  {
    digitalWrite(LEDPin1, LOW);
    digitalWrite(LEDPin2, HIGH);  
  }
  else if ( LED == '3')  {
    digitalWrite(LEDPin1, HIGH); 
    digitalWrite(LEDPin2, HIGH); 
  }
  else {
    digitalWrite(LEDPin1, LOW);
    digitalWrite(LEDPin2, LOW);
  }
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
  }
  mqttClient1.subscribe("commands");
  mqttClient1.loop();
}
