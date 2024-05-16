// 動手做5-2：從序列埠控制 LED 開關
// 詳細的程式說明，請參閱第五章，5-20頁。

const byte LED = 13;
char val;     		// 儲存接收資料的變數，採字元類型
void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);
  Serial.print("Welcome to Arduino!");
}

void loop() {
  if( Serial.available() ) {
    val = Serial.read();
    if (val == '1') {
      digitalWrite(LED, HIGH);
      Serial.print("LED ON");
    } 
    else if (val == '0') {
      digitalWrite(LED, LOW);
      Serial.print("LED OFF");
    }
  }
}
