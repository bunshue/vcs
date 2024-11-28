#include <ESP8266WiFi.h>
#include <PubSubClient.h>
char relayPin[] = {D1, D2, D3, D4};
const char* ssid = "urWiFiAccount";
const char* pw = "urPassword";
const char* mqttServer = "192.168.1.104";
const char *client1ID = "RELAYMODULELivingRoom";
WiFiClient espClient1;
PubSubClient client1(espClient1);
char topicSubcribe[]="light/livingroom/+";
char topicPublish[]="SwitchLivingRoom";
char msg[20];
void receiveCMD(char* topic, byte* payload, unsigned int len) {
  Serial.print("Message received->");
  Serial.print(topic);
  Serial.print(" : ");
  for (int i = 0; i < len; i++) Serial.print((char)payload[i]);
  Serial.println();
  char relayN = (char) payload[0];
  char onOrOff = (char) payload[1];
  char pin = relayN - 49;
  if ( onOrOff == '1' ) {
    digitalWrite(relayPin[pin], LOW);
    sprintf(msg, "SW %d is ON", pin+1);
    client1.publish(topicPublish, msg);
  }
  else {
    digitalWrite(relayPin[pin], HIGH); 
    sprintf(msg, "SW %d is OFF", pin+1);
    client1.publish(topicPublish, msg);
  }
}
void setup() {
  for(int i=0; i<4; i++) pinMode(relayPin[i], OUTPUT);  
  for(int i=0; i<4; i++) digitalWrite(relayPin[i], HIGH);
  Serial.begin(9600);
  WiFi.begin(ssid, pw);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  client1.setServer(mqttServer, 1883);
  client1.setCallback(receiveCMD);
}
void loop() {
  if (!client1.connected()) {
    client1.connect(client1ID);
    client1.subscribe(topicSubcribe);
  }
  client1.loop();
  delay(2000);
}
