#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#define   DHT22Pin  D1
char ssid[]="urWiFiAccount";  
char pw[]="urPassword";
char topicPublish[]="environment/livingroom";
const char *mqttServer = "192.168.1.104";
const char *client1ID = "DHT22LivingRoom";
WiFiClient espClient1;
DHT  dht22(DHT22Pin,DHT22);
PubSubClient client1(espClient1);
char msg[50];
float Temperature, Humidity;
void setup() {
  dht22.begin();
  Serial.begin(9600);
  WiFi.begin(ssid, pw);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  client1.setServer(mqttServer, 1883);
}
void loop() {
  if (!client1.connected() ) {
    client1.connect(client1ID);
  }
  client1.loop();
  delay(2000);
  Humidity = dht22.readHumidity();
  Serial.print("Relative Humidity: ");
  Serial.print(Humidity);
  Serial.println(" %");
  Serial.print("Temperature:       ");
  Temperature = dht22.readTemperature();
  Serial.print(Temperature);
  Serial.println(" C");
  delay(2000); 
  sprintf(msg, "{\"Temperature\": %d, \"Humidity\": %d}", int(Temperature), int(Humidity));
  Serial.print("Publishing message = ");
  Serial.println(msg);
  client1.publish(topicPublish, msg);
}
