// 動手做11-5：自行解析Nunchuck的訊息 
// 詳細的程式說明，請參閱第十一章，11-24頁。

#include <Wire.h>

int tempX = 0;
int tempY = 0;

void setup() {
  Serial.begin(9600);
  // 啟動和Wii手把的I2C連線
  Wire.begin();
  Wire.beginTransmission(0x52);
  Wire.write(0x40);
  Wire.write(0x00);
  Wire.endTransmission();
}

void loop() {
  byte buff[6];
  // 向手把請求資料
  Wire.requestFrom(0x52, 6);
  
  // 讀取資料並解碼
  byte i = 0;
  while(Wire.available()) {
    if(i < 6) {
      buff[i] = (Wire.read() ^ 0x17) + 0x17;
    }
    i++;
  }
  
  byte btnZ = ~buff[5] & 0x01;         // Z==1
  byte btnC = (~buff[5] >> 1) & 0x01;  // C==2
  byte joyX = buff[0];
  byte joyY = buff[1];
  int accX = buff[2] << 2 | ((buff[5] >> 2) & 0x03);
  int accY = buff[3] << 2 | ((buff[5] >> 4) & 0x03);
  int accZ = buff[4] << 2 | ((buff[5] >> 6) & 0x03);
  
  // 顯示按鈕與加速度值
  Serial.print("Z=");
  Serial.print(btnZ);
  Serial.print(" C=");
  Serial.print(btnC);
  Serial.print(" XY=");
  Serial.print(joyX);
  Serial.print(",");
  Serial.print(joyY);
  Serial.print(" XYZ=");
  Serial.print(accX, DEC);
  Serial.print(",");
  Serial.print(accY, DEC);
  Serial.print(",");
  Serial.print(accZ, DEC);
  Serial.print("\n");
  
  // 告知手把已收到資料
  Wire.beginTransmission(0x52);
  Wire.write(0x00);
  Wire.endTransmission();

  delay(50);
}
