// 動手做8-1：全域變數
// 詳細的程式說明，請參閱第八章，8-9頁。

int val;

void setup() {
  Serial.begin(9600);
}
void loop() {
  val ++;
  Serial.println(val);
  delay(500);
}
