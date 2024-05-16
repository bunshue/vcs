// 動手做12-1：偵測人體移動
// 詳細的程式說明，請參閱第十二章，12-5頁。

const byte pirPin = 12;   // 紅外線感測器訊號腳位
const byte ledPin = 13;   // LED 腳位
void setup() {
  pinMode(pirPin, INPUT);  // 感測器訊號腳位設定成「輸入」
  pinMode(ledPin, OUTPUT); // LED 腳位設定成「輸出」
}
void loop() {
  // 讀取感測器值，類型為布林（0 或 1）
  boolean val = digitalRead(pirPin);
  if (val) { // 若感測值為 1...
    digitalWrite(ledPin, HIGH); // 點亮 LED
  } else {
    digitalWrite(ledPin, LOW);
  }
}
