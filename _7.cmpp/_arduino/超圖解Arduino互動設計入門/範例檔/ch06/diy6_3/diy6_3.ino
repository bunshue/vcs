// 動手做6-3：拍手控制開關
// 詳細的程式說明，請參閱第六章，6-15頁。

int micPin = A0;  // 麥克風訊號輸入腳
int ledPin = 13;  // LED 接腳
int micVal = 0;   // 麥克風音量值
boolean toggle = false;     // LED 的狀態，預設為不亮

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  micVal = analogRead(micPin);

  if (micVal > 500) {     // 如果音量大於 500 ...
    Serial.println(micVal);
    toggle = !toggle;
 
    if (toggle) {
      digitalWrite(ledPin, HIGH);  // LED 點亮
    } 
    else {
      digitalWrite(ledPin, LOW);   // LED 熄滅
    }
  }
}


