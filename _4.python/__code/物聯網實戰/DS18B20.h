#include <OneWire.h>
void sensorToGo(OneWire);
char* searchSensor(OneWire);
char* checkData(byte *, int *);
float getTemperature(byte *);
