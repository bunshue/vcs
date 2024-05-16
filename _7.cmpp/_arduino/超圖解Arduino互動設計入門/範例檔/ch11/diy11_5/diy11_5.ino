// 動手做11-5：使用 Wii 左手把控制機械手臂
// 詳細的程式說明，請參閱第十一章，11-22頁。

#include <Wire.h>
#include <ArduinoNunchuk.h>
#include <Servo.h>    // 引用伺服馬達程式庫

ArduinoNunchuk nunchuk = ArduinoNunchuk();
Servo servoX, servoY;  // 宣告伺服馬達程式物件
int posX, posY;        // 暫存伺服馬達角度的變數

void setup() {
  nunchuk.init();   // 初始化 Wii 左手把
  servoX.attach(8);  // 伺服碼馬達接在數位 8 和 9 腳
  servoY.attach(9);
}

void loop() {
  nunchuk.update();

  if (nunchuk.zButton) {   // 若 Z 鈕的值為 1...
    // 用加速度 X, Y 軸值設定伺服馬達的旋轉角度值
    posX = map(nunchuk.accelX, 300, 740, 0, 179);
    posY = map(nunchuk.accelY, 280, 720, 0, 179);
  } 
  else {
    posX = map(nunchuk.analogX, 30, 225, 0, 179);
    posY = map(nunchuk.analogY, 29, 223, 0, 179);
  }
  
  servoX.write(posX); // 設定伺服馬達的旋轉角度
  servoY.write(posY);
  delay(15);
}

