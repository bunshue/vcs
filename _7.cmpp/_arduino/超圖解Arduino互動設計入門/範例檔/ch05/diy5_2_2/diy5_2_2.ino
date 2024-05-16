// 動手做5-2：從序列埠控制 LED 開關，使用switch..case
// 詳細的程式說明，請參閱第五章，5-22頁。

const byte LED = 13;
char val;     		// 儲存接收資料的變數，採字元類型
void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(115200);
  //Serial.println("Welcome to Arduino!");
}

void loop() {
  if( Serial.available() ) {
    val = Serial.read();
    switch (val) {
    case '0' :
      digitalWrite(LED, LOW);
      Serial.println("LED OFF");
      break;
    case  '1' :
      digitalWrite(LED, HIGH);
      Serial.println("LED ON");
      break;
    }
  }
}

