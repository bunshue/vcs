// 動手做11-4：讀取 Wii 左手把的搖桿、按鈕與加速度計值
// 詳細的程式說明，請參閱第十一章，11-18頁。

#include <Wire.h>
#include <ArduinoNunchuk.h>

ArduinoNunchuk nunchuk = ArduinoNunchuk();

void setup() {
  Serial.begin(9600);
  nunchuk.init();
}

void loop() {
  nunchuk.update();
  
  Serial.print(nunchuk.analogX, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.analogY, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.accelX, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.accelY, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.accelZ, DEC);
  Serial.print(' ');
  Serial.print(nunchuk.zButton, DEC);
  Serial.print(' ');
  Serial.println(nunchuk.cButton, DEC);
}
