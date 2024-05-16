#include <SPI.h>
#include <MFRC522.h>     // 引用程式庫
#include <Servo.h>         // 引用伺服馬達程式庫

#define RST_PIN      A0  // 讀卡機的重置腳位
#define SS_PIN       10  // 晶片選擇腳位
#define SERVO_PIN    2   // 伺服馬達的控制訊號接腳

bool lockerSwitch = false;  // 伺服馬達的狀態

Servo servo;    // 宣告伺服馬達物件

struct RFIDTag {   // 定義結構
   byte uid[4];
   char *name;
};

struct RFIDTag tags[] = {  // 初始化結構資料，請自行修改RFID識別碼。
  {{60,209,110,133}, "Arduino"},
  {{212,211,192,97}, "Raspberry Pi"},
  {{21,8,10,83}, "Espruino"}
};

byte totalTags = sizeof(tags) / sizeof(RFIDTag);  // 計算結構資料筆數，結果為3。

MFRC522 mfrc522(SS_PIN, RST_PIN);  // 建立MFRC522物件

// 開鎖或關鎖
void locker(bool toggle) {
  if (toggle) {
      servo.write(90);  // 開鎖
  } else {
      servo.write(0);   // 關鎖
  }
  delay(15);    // 等伺服馬達轉到定位
}

void setup() {
  Serial.begin(9600);
  Serial.println();
  Serial.print("size of RFIDTag:");
  Serial.println(sizeof(RFIDTag));
  Serial.print("size of tag:");
  Serial.println(sizeof(tags));
  Serial.println("RFID reader is ready!");

  SPI.begin();
  mfrc522.PCD_Init();       // 初始化MFRC522讀卡機模組
  servo.attach(SERVO_PIN);  // 將伺服馬達物件附加在數位2腳
  locker(lockerSwitch);
}

void loop() {
    // 確認是否有新卡片
    if (mfrc522.PICC_IsNewCardPresent() && mfrc522.PICC_ReadCardSerial()) {
      byte *id = mfrc522.uid.uidByte;   // 取得卡片的UID
      byte idSize = mfrc522.uid.size;   // 取得UID的長度
      bool foundTag = false;    // 是否找到紀錄中的標籤，預設為「否」。
      
      for (byte i=0; i<totalTags; i++) {
        if (memcmp(tags[i].uid, id, idSize) == 0) {  // 比對陣列資料值
          Serial.println(tags[i].name);  // 顯示標籤的名稱
          foundTag = true;  // 設定成「找到標籤了！」
          
          lockerSwitch = !lockerSwitch;  // 切換鎖的狀態
          locker(lockerSwitch);          // 開鎖或關鎖
          break;  // 退出for迴圈
        }
      }

      if (!foundTag) {  // 若掃描到紀錄之外的標籤，則顯示"Wrong card!"。
        Serial.println("Wrong card!");

        // 如果鎖是開啟狀態，則關閉它。
        if (lockerSwitch) {
          lockerSwitch = false;
          locker(lockerSwitch);
        }
      }

      mfrc522.PICC_HaltA();  // 讓卡片進入停止模式      
    } 
}
