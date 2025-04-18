#include "arduino_secrets.h"
/* 
  Sketch generated by the Arduino IoT Cloud Thing "Untitled"
  https://create.arduino.cc/cloud/things/913396fe-625f-4602-a114-72e0b126e11a 

  Arduino IoT Cloud Variables description

  The following variables are automatically generated and updated when changes are made to the Thing

  float humi;
  float temp;

  Variables which are marked as READ/WRITE in the Cloud Thing will also have functions
  which are called when their values are changed from the Dashboard.
  These functions are generated with the Thing and added at the end of this sketch.
*/

#include "thingProperties.h"

#include <DHT.h>
#define 	DHTPIN 		D1    
#define 	DHTTYPE    	DHT11     
DHT 	dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  delay(1500); 
  dht.begin();
  initProperties();
  ArduinoCloud.begin(ArduinoIoTPreferredConnection);
  setDebugMessageLevel(2);
  ArduinoCloud.printDebugInfo();
}

void loop() {
  ArduinoCloud.update();
  delay(2000);
  humi = dht.readHumidity();
  temp = dht.readTemperature();
  if (isnan(humi) || isnan(temp) ) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
}




