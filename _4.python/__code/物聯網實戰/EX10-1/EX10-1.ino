#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define relayPin1 D1
const char* ssid = "urWiFiAccount";
const char* pw = "urPassword";
const char* mqttServer = "192.168.1.104";
const char *client1ID = "COFFEEMAKER";
WiFiClient espClient1;
PubSubClient client1(espClient1);
char topicSubcribe[] = "appliance/coffeemaker";
char topicPublish[] = "CoffeeMaker";
void receiveCMD(char* topic, byte* payload, unsigned int len) {
  Serial.print("Message received->");
  Serial.print(topic);
  Serial.print(" : ");
  for (int i = 0; i < len; i++) Serial.print((char)payload[i]);
  Serial.println();
  char onOroff = (char) payload[0];
  if ( onOroff == '1') {
    digitalWrite(relayPin1, LOW); 
    client1.publish(topicPublish, "Coffee is ON");
  }
  else {
    digitalWrite(relayPin1, HIGH);
    client1.publish(topicPublish, "Coffee is OFF");
  }
}
void setup() {
  pinMode(relayPin1, OUTPUT);  
  digitalWrite(relayPin1, HIGH);  
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
