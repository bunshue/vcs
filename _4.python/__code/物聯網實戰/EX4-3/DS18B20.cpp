#include <DS18B20.h>
byte bufferSensor[8];
char *errorMsg[]={"Sensor OK","CRC not OK","Not DS18B20","Data not 
OK"};
char* searchSensor(OneWire tempSensor) {
 while ( !tempSensor.search(bufferSensor)) {
 tempSensor.reset_search();
 delay(250);
 }
 int codeNo=0;
 if (OneWire::crc8(bufferSensor, 7) != bufferSensor[7]) {
 codeNo=1;
 }
 if (bufferSensor[0] != 0x28) {
 codeNo=2;
 }
 return errorMsg[codeNo];
}
void sensorToGo(OneWire tempSensor) {
 tempSensor.reset();
 tempSensor.select(bufferSensor);
 tempSensor.write(0x44, 1); 
 delay(1000); 
 tempSensor.reset();
 tempSensor.select(bufferSensor); 
 tempSensor.write(0xBE); 
}
char* checkData(byte *data) {
 int codeNo=0;
 if (OneWire::crc8(data, 8) != data[8]) codeNo=3;
 return errorMsg[codeNo];
}
float getTemperature(byte *data) {
 float temp = 0.0;
 int16_t rawData;
 rawData = (data[1] << 8) | data[0]
 temp = (float) rawData / 16.0 ;
 return temp;
}
