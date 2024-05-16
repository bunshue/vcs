// 動手做18-1：讀取 RFID 標籤
// 詳細的程式說明，請參閱第十八章，18-9頁。

#include <SoftwareSerial.h>
SoftwareSerial RFID(3, 4);   // 接收腳=3, 傳送腳=4
byte data;          // 暫存標籤資料的變數
void setup() {
  Serial.begin(9600);
  RFID.begin(9600);
  Serial.println("RFID Ready!");
}
void loop() {
  if (RFID.available() > 0) { // 若讀取到序列資料...
    data = RFID.read();       // 儲存讀取到的資料
    Serial.println(data);     // 將資料顯示在序列埠監視窗
  }
}
