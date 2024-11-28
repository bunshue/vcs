#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define LEDPin1 D0
#define LEDPin2 D1
const char* ssid = "mayandtclin";
const char* password = "46101222";
const char* mqttServer = "192.168.1.105";
WiFiClient wifiClient1;
PubSubClient mqttClient1(wifiClient1);
void receivedCMD(char* topic, byte* payload, unsigned int noChar) {
  char *response;
  char LED = (char) payload[0];
  Serial.println(LED);
  if ( LED == '1') {
    digitalWrite(LEDPin1, HIGH);
    digitalWrite(LEDPin2, LOW);   
    response = "ok 1";
  } 
  else if ( LED == '2')  {
    digitalWrite(LEDPin1, LOW);
    digitalWrite(LEDPin2, HIGH);  
    response = "ok 2";
  }
  else if ( LED == '3')  {
    digitalWrite(LEDPin1, HIGH); 
    digitalWrite(LEDPin2, HIGH); 
    response = "ok 3";
  }
  else if ( LED == '0') {
    digitalWrite(LEDPin1, LOW);
    digitalWrite(LEDPin2, LOW);
    response = "ok 0";
  }
  else {
    LED = '4';
    response = "Not ok";
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
