// 附錄C：光耦合元件的控制程式
// 程式說明請參閱附錄C，C-5頁。

const byte pirPin = 12; // 紅外線感測器訊號腳位
const byte ledPin = 13; // LED 腳位
const byte recPin = 9;  // 錄影鈕
const byte stopPin = 8; // 停止鈕
long oldTime;           // 暫存當前時間
/* 10 分鐘的毫秒數：1000 × 60 × 10
  底下這一行可改寫成：
  long delayTime = 1000L * 60L * 10L;       */
long delayTime = 600000;
long diffTime;          // 儲存時間差
boolean turnOn = false; // 代表是否點亮 LED 的變數，預設為「否」

void setup() {
  pinMode(pirPin, INPUT);    // 感測器訊號腳位設定成「輸入」
  pinMode(ledPin, OUTPUT);   // LED 腳位設定成「輸出」
  pinMode(recPin, OUTPUT);   // 「錄影」腳設定成「輸出」
  pinMode(stopPin, OUTPUT);  // 「停止」腳設定成「輸出」
}

void loop() {
  // 讀取感測器值，類型為布林（0 或 1）
  boolean val = digitalRead(pirPin);
  // LED 尚未點亮且感測值為 1...
  if (turnOn == false && val == true) {
    turnOn = true;                // 設定為「已點亮」
    oldTime = millis();           // 暫存當前時間的毫秒值
    digitalWrite(ledPin, HIGH);   // 點亮 LED
    digitalWrite(recPin, HIGH);   // 相當於「按著」錄影鈕
    delay(100);                   // 經 0.1 秒後…
    digitalWrite(recPin, LOW);    // 「放開」錄影鈕，
                                  // 構成「按一下」的動作
  }
 
  if (turnOn) {                   // 如果 LED 目前是點亮的...
    // 比較現在時間與之前記錄的時間
    diffTime = millis() - oldTime;
    // 如果時間差大於或等於延遲時間（10 分鐘）...
    if (diffTime >= delayTime) {
      turnOn = false;            // 設定為「關閉 LED」

      digitalWrite(ledPin, LOW);   // 關閉 LED
      digitalWrite(stopPin, HIGH);   // 相當於「按著」停止鈕
      delay(100);                    // 經 0.1 秒後…
      digitalWrite(stopPin, LOW);    // 「放開」停止鈕，
                                    // 構成「按一下」的動作
    }
  }
}

