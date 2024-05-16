// 詳細的程式說明，請參閱第三章，3-13頁。
byte led = 13;

void setup() {  
  pinMode(led, OUTPUT);
}

void loop() {
  digitalWrite(led, HIGH);
  delay(1000);
  digitalWrite(led, LOW);
  delay(1000);
}
