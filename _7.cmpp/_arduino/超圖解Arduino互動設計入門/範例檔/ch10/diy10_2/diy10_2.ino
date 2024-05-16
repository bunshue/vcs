// 動手做10-2：隨機數字與燭光效果
// 詳細的程式說明，請參閱第十章，10-7頁。

byte ledPin = 11; // 類比輸出腳位

void setup() {
  pinMode(ledPin, OUTPUT);
  randomSeed(analogRead(A5));
}
void loop() {
  analogWrite(ledPin, random(135)+120);
  delay(random(200));
}

