#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define relayPin  D0
#define LSPin     D1
#define LEDPin    D2
const char* urWiFiAccount = "urWiFiAccount";
const char* urPassword = "urPassword";
const char* mqttServer = "192.168.1.104";
const int maxDebounce = 500;
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
    digitalWrite(relayPin, LOW);   
    response = "OK 1";
  } 
  else if ( CMD == '0')  {
    digitalWrite(LEDPin, LOW);
    digitalWrite(relayPin, HIGH);   
    response = "OK 0";
  }
  else {
    response = "Not OK";
  }
  mqttClient1.publish("ack", response);
}
void setup() {
  pinMode(relayPin, OUTPUT);
  pinMode(LEDPin, OUTPUT);    
  pinMode(LSPin, INPUT_PULLUP);
  Serial.begin(9600);
  WiFi.begin(urWiFiAccount, urPassword);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  mqttClient1.setServer(mqttServer, 1883);
  mqttClient1.setCallback(receivedCMD);
}
void loop() {
  while( !mqttClient1.connected()) {
    mqttClient1.connect("ESP8266");
    mqttClient1.subscribe("commands");
  }
  mqttClient1.loop();
  if ( digitalRead(LSPin) == 0) {
    if (debounce > maxDebounce) {
      debounce = 0;
      digitalWrite(relayPin, HIGH);
      digitalWrite(LEDPin, LOW);
      delay(500);
      mqttClient1.publish("ack", "OK LS");
    }
    else debounce++;
  }
}
