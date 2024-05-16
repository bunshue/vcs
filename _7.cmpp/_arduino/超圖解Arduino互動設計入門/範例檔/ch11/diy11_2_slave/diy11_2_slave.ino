// 動手做11-2：透過I2C介面串連兩個Arduino板（接收端）
// 詳細的程式說明，請參閱第十一章，11-12頁。

#include <Wire.h>

void setup() {
    Wire.begin(3);     // 啟動I2C連線
    Wire.onReceive(receiveEvent);

    Serial.begin(9600);
}

void loop() {
    delay(100);
}
void receiveEvent(int numBytes) {
    while(Wire.available()) {
      char c = Wire.read();
      Serial.print(c);
    }
}
