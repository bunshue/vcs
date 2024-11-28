#include <DS18B20.h>
#define sensorPin 5
OneWire tempSensor(sensorPin);
byte data[9];
int errorCode;
float temp;
char msg[20];
char* errormsg=msg;
void setup(void) {
  Serial.begin(9600);
  errormsg = searchSensor(tempSensor);
  Serial.println(errormsg);
}
void loop(void) {
  sensorToGo(tempSensor);
  for (int i = 0; i < 9; i++) data[i] = tempSensor.read();
  errormsg = checkData(data, &errorCode);
  if ( errorCode != 0) {
    Serial.println(errormsg);
  }
  else {
    temp = getTemperature(data);
    Serial.print("Current temperature in Celsius = ");
    Serial.println(temp);
    delay(2000);
  }
}
