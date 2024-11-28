#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define relayPin  D0
#define LSPin     D1
#define LEDPin    D2
const char* ssid = "mayandtclin";
const char* password = "46101222";
const char* mqttServer = "192.168.1.105";
const int maxDebounce = 100;
int   debounce = 0;
bool  currentStatus = HIGH;
WiFiClient wifiClient1;
PubSubClient mqttClient1(wifiClient1);
void receivedCMD(char* topic, byte* payload, unsigned int noChar) {
  char *response;
  char CMD = (char) payload[0];
  Serial.print(topic);
  Serial.print(" ");
  Serial.println(CMD);
  if ( CMD == '1') {
    digitalWrite(LEDPin, HIGH);
    digitalWrite(relayPin, HIGH);   
    response = "ok 1";
  } 
  else if ( CMD == '0')  {
    digitalWrite(LEDPin, LOW);
    digitalWrite(relayPin, LOW);   
    response = "ok 0";
  }
  else {
    response = "Not ok";
  }
  mqttClient1.publish("ack", response);
}
void setup() {
  pinMode(relayPin, OUTPUT);
  pinMode(LEDPin, OUTPUT);    
  pinMode(LSPin, INPUT_PULLUP);
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
  bool reading = digitalRead(LSPin);
  if ( reading == currentStatus && debounce > 0 ) debounce--;
  if ( reading != currentStatus) debounce++;
  if (debounce > maxDebounce) {
    debounce = 0;
    digitalWrite(relayPin, LOW);
    digitalWrite(LEDPin, LOW);
    delay(500);
    mqttClient1.publish("ack", "0");
  }
}
