// 動手做6-1：從序列埠讀取「類比輸入」值
// 詳細的程式說明，請參閱第六章，6-4頁。

const byte potPin = A0;
int val;       // 接收類比輸入值的變數，類型為整數
void setup() {
  Serial.begin(9600);  // 以 9600bps 速率初始化序列埠
}
void loop() {
  val = analogRead(potPin);
  Serial.println(val);
  delay(500);
}
