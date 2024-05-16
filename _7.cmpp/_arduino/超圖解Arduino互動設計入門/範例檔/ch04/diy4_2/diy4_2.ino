// 跑馬燈範例程式一
// 詳細的程式說明，請參閱第四章，4-17頁。

const byte LED1 = 8;
const byte LED2 = 9;
const byte LED3 = 10;
void setup() {
  // 三個 LED 接腳都設定成「輸出」
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}
void loop() {
  digitalWrite(LED1, HIGH);   // 點亮第一個 LED
  digitalWrite(LED2, LOW);    // 熄滅第二個 LED
  digitalWrite(LED3, LOW);    // 熄滅第三個 LED
  delay(100);      	      // 持續 0.1 秒
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, HIGH);    // 點亮第二個 LED
  digitalWrite(LED3, LOW);
  delay(100);
  digitalWrite(LED1, LOW);
  digitalWrite(LED2, LOW);
  digitalWrite(LED3, HIGH);    // 點亮第三個 LED
  delay(100);
}
