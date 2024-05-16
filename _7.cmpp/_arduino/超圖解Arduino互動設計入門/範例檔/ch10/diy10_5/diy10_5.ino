// 動手做10-5：電晶體馬達控制與調速器
// 詳細的程式說明，請參閱第十章，10-23頁。

byte potPin = A0;  // 類比輸入腳位（接 10KΩ可變電阻）
byte motorPin = 5; // 類比輸出腳位（接電晶體馬達控制電路）
int potValue = 0;  // 類比輸出值
byte val = 0;      // 儲存類比範圍轉換值

void setup() {
  pinMode(motorPin, OUTPUT);
}
void loop() {
  potValue = analogRead(potPin);
  val = map(potValue, 0, 1023, 0, 255);
  analogWrite(motorPin, val);
}
