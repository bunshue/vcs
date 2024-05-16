// 詳細的程式說明，請參閱第三章，3-24頁。
const byte LED = 13;

void setup() {  
  pinMode(LED, OUTPUT);
}

void loop() {
  digitalWrite(LED, HIGH);
  delay(1000);
  digitalWrite(LED, LOW);
  delay(1000);
}
