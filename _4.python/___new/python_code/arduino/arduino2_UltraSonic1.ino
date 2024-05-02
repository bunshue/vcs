/*
本程式為SR04超音波感測器的範例

首先要安裝ErickSimoes/Ultrasonic的函式庫
VCC接5V，GND接地。Trig接到pin 12，Echo接到pin 13。
*/

#include <Ultrasonic.h>

Ultrasonic ultrasonic(12, 13);
int distance;

void setup() {
  Serial.begin(9600);
}

void loop() {
  
  distance = ultrasonic.read(); //不加參數就是輸出CM，可用read(INC)輸出英寸
  
  Serial.print("Distance in CM: ");
  Serial.println(distance);
  delay(500); //每次間格0.5秒
}
