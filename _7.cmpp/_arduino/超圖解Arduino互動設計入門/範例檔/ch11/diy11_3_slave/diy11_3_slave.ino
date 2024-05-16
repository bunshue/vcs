// 動手做11-3：在I2C介面上傳送整數資料（從端）
// 詳細的程式說明，請參閱第十一章，11-16頁。

#include <Wire.h>

void setup() {
  Wire.begin(3); // 啟動連線並設定此從端裝置的位址為 3
  // 處理「接收訊息」的事件處理程式
  Wire.onReceive(receiveEvent);
  Serial.begin(9600);
}

void loop() {
  delay(100);
}

void receiveEvent(int numBytes) {
  while(Wire.available() >= 2) {  // 若收到兩個或以上的位元組...
    byte b1 = Wire.read();    // 一次讀取一個位元組
    byte b2 = Wire.read();
    int val = b1 * 256 + b2;    // 還原成整數值
    Serial.println(val);     // 顯示在「序列埠監控視窗」
  }
}
