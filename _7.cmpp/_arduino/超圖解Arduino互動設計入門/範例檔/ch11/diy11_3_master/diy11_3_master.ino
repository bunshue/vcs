// 動手做11-3：在I2C介面上傳送整數資料（主控端）
// 詳細的程式說明，請參閱第十一章，11-16頁。

#include <Wire.h>
void setup() {
  Wire.begin();
}

void loop() {
  byte b1, b2;
  int val = analogRead(A0);   // 類比輸入值的範圍：0~1024
  b1 = val / 256;
  b2 = val % 256;
  Wire.beginTransmission(3);   // 傳送給地址 3 的裝置
  Wire.write(b1);              // 一次傳送一個位元組
  Wire.write(b2);
  Wire.endTransmission();      // 停止傳送
  delay(1000);
}
