// 動手做18-2：使用 RFID 控制開關，標籤值儲存在程式記憶體區。
// 詳細的程式說明，請參閱第十八章，18-15頁。

#include <avr/pgmspace.h>
#include <SoftwareSerial.h>

SoftwareSerial RFID(3, 4); // 接收腳=3, 傳送腳=4

const byte TAG_LEN = 14;   // 定義標籤資料的長度
const byte TAG_TOTAL = 2;   // 定義標籤資料的組數
byte temp[TAG_LEN];        // 存放讀入標籤的 14 個數字
String rfidStr = "";
int tag = -1;
 
PROGMEM byte tags[TAG_TOTAL][TAG_LEN] = {
    // 第 0 組標籤
    {2, 48, 50, 48, 48, 53, 50, 56, 49, 57, 70, 52, 71, 3},
    // 第 1 組標籤
    {2, 48, 54, 48, 48, 55, 53, 54, 52, 57, 53, 56, 50, 3}
};

const byte ledPin = 13;   // LED 位於 13 腳

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
    for (byte i=0; i<TAG_TOTAL; i++) {
      if (memcmp_P(temp, tags[i], TAG_LEN) == 0 ) {
        Serial.println(i);
        tag = i;   // 記錄標籤編號
        break;     // 若找到相符的標籤，就跳出迴圈，不用再找了。
      } else {
        tag = -1;  // tag值為-1，代表沒有找到相同的標籤編碼。
      }
    }
    
    switch (tag) {
      case 0:      // 如果是編號0的標籤，就點亮LED。
        digitalWrite(ledPin, HIGH);
        break;
      case 1:      // 若是編號1的標籤，關閉LED。
        digitalWrite(ledPin, LOW);
        break;
    }
  }
}
