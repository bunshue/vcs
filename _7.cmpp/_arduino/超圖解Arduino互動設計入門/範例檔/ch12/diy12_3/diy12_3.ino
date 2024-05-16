// 動手做12-3：使用 IRremote 程式庫解析紅外線遙控值
// 詳細的程式說明，請參閱第十二章，12-12頁。

#include <IRremote.h>
#include <Servo.h>

Servo servo;
const byte RECV_PIN = 11;    // 紅外線接收腳
const byte LED_PIN = 13;     // LED 腳
const byte SERVO_PIN = 8;   // 伺服器接腳
boolean sw = false;         // 開關狀態，預設為「關」
byte servoPos = 90;          // 伺服器角度，預設為 90 度

IRrecv irrecv(RECV_PIN);    // 初始化紅外線接收器
decode_results results;      // 儲存紅外線碼解析值

void setup() {
  irrecv.enableIRIn();       // 啟動紅外線接收器
  pinMode(LED_PIN, OUTPUT);  // LED 腳位設定成「輸出」
  servo.attach(SERVO_PIN);   // 連接伺服器
  servo.write(servoPos);   // 設定伺服器的旋轉角度
}

void loop() {
  if (irrecv.decode(&results)) { // 如果收到紅外線遙控訊號...
    switch (results.value) { // 讀取解析之後的數值，並且比較...
      case 0xC1C7C03F: // 若此數值等於「錄影」...
        sw = !sw;      // 將開關變數值予以反相
        digitalWrite(LED_PIN, sw); // 依據「開關」值，設定 LED 燈
        break;
      case 0xC1C7C43B: // 若此數值等於「左方向鍵」...
        if (servoPos > 10) { // 若伺服器旋轉角度大於 10...
          servoPos -= 10;    // 減少旋轉角度 10 度
          servo.write(servoPos);
        }
        break;
      case 0xC1C744BB: // 若此數值等於「右方向鍵」...
        if (servoPos < 170) { // 若伺服器旋轉角度小於 170...
          servoPos += 10;     // 增加旋轉角度 10 度
          servo.write(servoPos);
        }
        break;
    }
 
    irrecv.resume(); // 準備接收下一筆資料
  }
}
