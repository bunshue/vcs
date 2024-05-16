// 動手做11-6：改造伺服馬達成連續360°旋轉
// 詳細的程式說明，請參閱第十一章，11-28頁。

#include <Servo.h>
Servo servo1;      // 宣告伺服馬達程式物件
Servo servo2;      // 宣告伺服馬達程式物件

void setup() {
  Serial.begin(9600);
  servo1.attach(9); // 設定伺服馬達的接腳
  servo2.attach(10); // 設定伺服馬達的接腳
  servo1.write(90); // 停止伺服馬達
  servo2.write(90); // 停止伺服馬達
}

void loop() {
  byte deg = 0;
  byte _in;

  if (Serial.available()) { // 若有資料從序列埠傳入...
    _in = Serial.read();
    while (_in !=  '\n') {  // 若尚未收到「換行」字元...
      if (_in >=  '0'  && _in <=  '9') {
        deg = deg * 10 + (_in -  '0');
      }
      _in = Serial.read();
    }

    if (deg > 179) { // 確認用戶輸入值最高不超過 179
      deg = 179;
    }
    // 在序列埠監控視窗顯示接收到的角度值
    Serial.print("degree: ");
    Serial.println(deg);
    // 設定伺服馬達的旋轉角度（即：旋轉方向和轉速）
    servo1.write(deg);
    servo2.write(deg);
    delay(15);
  }
}
