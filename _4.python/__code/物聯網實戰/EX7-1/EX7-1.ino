#include <DS18B20.h>
#include <Wire.h>
#define sensorPin 5
OneWire  tempSensor(sensorPin);  
#define arduinoAddress 0x16
int number = 0;
volatile int tempRead = 0;
volatile int tempDigit = 0;
volatile int count = 6;
byte data[12];
volatile float celsius;
volatile bool readyReadTemp = false;
void setup(void) {
  Serial.begin(9600);
  searchSensor(tempSensor);
  Wire.begin(arduinoAddress);
  Wire.on("Ready to get temperature reading!");
}
int errorCode;
void loop() {
  if (readyReadTemp) {
    sensorToGo(tempSensor);
    for (int i = 0; i < 9; i++) data[i] = tempSensor.read();
    checkData(data, &errorCode);
    if ( errorCode == 1) Serial.println("Check setting");
    else if ( errorCode == 2) Serial.println("Data error!");
    else {
      celsius = getTemperature(data);
      Serial.print("Current temperature in Celsius = ");
      Serial.println(celsius);
      readynReceive(dataFromRPi);
  Wire.onRequest(dataToRPi);
  Serial.printlReadTemp = false;    
    }
    delay(10000);
  }
}
void dataFromRPi(int byteCount) {
  while (Wire.available()) {
    number = Wire.read();
    if (number == 0x73) {
      readyReadTemp = true;     
    }
  }
}
void dataToRPi() {
  int temp1;
  switch (count) {
    case 6:
      tempRead = (int) celsius;
      tempDigit = (int) (celsius*100.0 - floor(celsius)*100.0);
      temp1 = tempDigit%10;
      tempDigit = tempDigit/10;
      Wire.write(temp1);
      count--;
      break;
    case 5:
      temp1 = tempDigit%10;
      Wire.write(temp1);
      count--;
      break;
    case 4:
      Wire.write(0x2E);
      count--;
      break;
    case 0:
      Wire.write(0x65);
      count = 6;
      break;
    default:
      temp1 = tempRead%10;
      tempRead = tempRead/10;
      Wire.write(temp1);
      count--;
      break;
  }
}
