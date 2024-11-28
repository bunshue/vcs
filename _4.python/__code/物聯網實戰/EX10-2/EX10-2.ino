#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define motorRunPin   D1 
#define motorDirPin   D3 
char limitSWPin[] = {D5, D6, D7}; 
char ssid[] = "urWiFiAccount";  // replace with your ssid & pass
char pw[] = "urPassword";
const char *mqttServer = "192.168.1.104";
const char *client1ID = "CurtainControl";
const char topicSubscribe[] = "appliance/curtain";
const char topicPublish[] = "Curtain";
WiFiClient espClient1;
PubSubClient client1(espClient1);
void receiveCMD(char *, byte *, unsigned int);
char opening = '0';
char previousOpening = '0';
char strCommand;
unsigned long startTime;
void receiveCMD(char *topic, byte *payload, unsigned int len) {
  Serial.print("Message arrived->");
  Serial.print(topic);
  Serial.print(":");
  for (int i = 0; i < len; i++) Serial.print((char) payload[i]);
  Serial.println();
  opening = payload[0];  
}
void setup() {
  delay(1000);
  Serial.begin(9600);
  WiFi.begin(ssid, pw);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  client1.setServer(mqttServer, 1883);
  client1.setCallback(receiveCMD);
  for (int i=0; i<3; i++) pinMode(limitSWPin[i], INPUT_PULLUP);
  pinMode(motorDirPin, OUTPUT);
  pinMode(motorRunPin, OUTPUT);
}
void loop() {
  if (!client1.connected() ) {
    client1.connect(client1ID);
    client1.subscribe(topicSubscribe);
  }
  client1.loop();
  switch (opening) {
    case '0':
      if ( opening == previousOpening ) break;
      else {
        previousOpening = opening;
        startTime = millis();
        while ( digitalRead(limitSWPin[0])==HIGH && (millis()-startTime)<10000 ) {
          yield();
          digitalWrite(motorDirPin, HIGH);
          analogWrite(motorRunPin, 1023);
        }
        analogWrite(motorRunPin, 0);
        client1.publish(topicPublish, "Curtain is closed");
      }
      break;
    case '1':
      if ( opening == previousOpening ) break;
      else if ( opening < previousOpening ) {
        previousOpening = opening;
        startTime = millis();
        while ( digitalRead(limitSWPin[1])==HIGH && (millis()-startTime)<10000 ) {
          yield();
          digitalWrite(motorDirPin, HIGH);
          analogWrite(motorRunPin, 1023);
        }
        analogWrite(motorRunPin, 0);
        client1.publish(topicPublish, "Curtain is half open");
      }
      else {
        previousOpening = opening;
        startTime = millis();
        while ( digitalRead(limitSWPin[1])==HIGH && (millis()-startTime)<10000 ) {
          yield();
          digitalWrite(motorDirPin, LOW);
          analogWrite(motorRunPin, 1023);
        }
        analogWrite(motorRunPin, 0);
        client1.publish(topicPublish, "Curtain is half open");
      }
      break;
    case '2':
      if ( opening == previousOpening ) break;
      else {
        previousOpening = opening;
        startTime = millis();
        while ( digitalRead(limitSWPin[2])==HIGH && (millis()-startTime)<10000 ) {
          yield();
          digitalWrite(motorDirPin, LOW);
          analogWrite(motorRunPin, 1023);
        }
        analogWrite(motorRunPin, 0);
        client1.publish(topicPublish, "Curtain is full open");
      }
      break;
    defalult:
      break;
  }
}
