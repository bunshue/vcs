#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#include <Servo.h>
#define  servoPin   D1
Servo   servo1;
char ssid[] = "urWiFiAccount";  // replace with your ssid & pass
char pw[] = "urPassword";
const char *mqttServer = "192.168.1.104";
const char *client1ID = "ShutterControl";
char topicSubscribe[] = "appliance/shutter";
char topicPublish[] = "Shutter";
WiFiClient espClient1;
PubSubClient client1(espClient1);
void receiveCMD(char *, byte *, unsigned int);
int Illuminance = 0;
bool Operation = false;
int Opening = 0;
int str2int(byte *, int) ;
int power10(int);
char msg[50];
void receiveCMD(char *topic, byte *payload, unsigned int len) {
  Serial.print("Message received->");
  Serial.print(topic);
  Serial.print(":");
  for (int i = 0; i < len; i++) Serial.print((char) payload[i]);
  Serial.println(); 
  char cmd = payload[0];
  if (cmd == 'x') {
    Operation = true;
    Opening = str2int(payload+1, len-1);
  }
  else Operation = false;
}
void setup() {
  servo1.attach(servoPin);
  servo1.write(0);
  delay(1000);
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
  if (!client1.connected() ) {
    client1.connect(client1ID);
    client1.subscribe(topicSubscribe);
  }
  client1.loop();
  delay(10000);
  Illuminance = analogRead(A0);
  Illuminance = map(Illuminance, 0, 1023, 100, 0);
  sprintf(msg, "{\"Illuminance\": %d}", Illuminance);
  client1.publish("Illuminance", msg);
  if (Operation) {
    sprintf(msg, "Shutter %d percent open", Opening);
    Opening = map(Opening, 0, 100, 0, 180);
    servo1.write(Opening);
    Operation = false;
    client1.publish(topicPublish, msg);
    delay(10000);
  }
}
int str2int(byte *str, int n) {
  int no = 0;
  for (int i=0; i<n; i++) {
    no += (str[i] - 48)*power10(n-i-1);
  }
  return no;
}
int power10(int n) {
  int no = 1;
  for (int i=1; i<n+1; i++) {
    no = no*10;
  }
  return no;
}
