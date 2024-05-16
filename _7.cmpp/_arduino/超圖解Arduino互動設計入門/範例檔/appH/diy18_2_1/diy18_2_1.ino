// 動手做18-2：使用 RFID 控制開關
// 詳細的程式說明，請參閱第十八章，18-14頁。

#include <SoftwareSerial.h>

SoftwareSerial RFID(3, 4); // 接收腳=3, 傳送腳=4

const byte TAG_LEN = 14;   // 定義標籤資料的長度
byte temp[TAG_LEN];        // 存放讀入標籤的 14 個數字
String rfidStr = "";

const byte ledPin = 13;   // LED 位於 13 腳
// 請將底下的數字改成你的 RFID 標籤數字
// 代表「開啟」的 RFID 編碼值
String tagON= "24850484853505649577052713" ;
// 代表「關閉」的 RFID 編碼值
String tagOFF = "24854484855535452575356503" ;

// 負責讀入 RFID 編碼值的自訂函數，傳回值類型為「布林」
boolean readTag() {
  // 代表是否讀入資料的變數，預設值為 0，代表沒有
  boolean ok = 0;
  if (RFID.available()) { // 如果讀卡機傳入新的資料...
    delay(100);           // 等 0.1 秒，讓其餘數字都傳進來
 
    // 執行 14 次迴圈，讀取緩衝區裡的數字
    for (byte i=0; i<TAG_LEN; i++) {
      temp[i] = RFID.read();
    }
    RFID.flush();   // 清除緩衝區
    ok = 1;       // 讀取完畢後，設定成 1，代表有讀到新資料
  }
  return ok;       // 傳回 0 或 1
}

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
  RFID.begin(9600);
  Serial.println("RFID Ready!");
}

void loop() {
  if (readTag()) {
    rfidStr = "";
    for (byte i=0; i<TAG_LEN; i++) {
       rfidStr += temp[i];
    }
    Serial.println(rfidStr);
 
    if (rfidStr == tagON) { // 如果 RFID 碼等於「開啟」的編碼值
      digitalWrite(ledPin, HIGH); // 點亮 LED
    } else if (rfidStr == tagOFF) {
      // 否則，若 RFID 碼等於「關閉」編碼
      digitalWrite(ledPin, LOW);  // 關閉 LED
    }
  }
}
