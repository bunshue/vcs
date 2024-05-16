// 動手做6-4：拍手控制開關改良版
// 詳細的程式說明，請參閱第六章，6-19頁。

int micPin = A0;       // 麥克風訊號輸入腳
int ledPin = 13;       // LED 接腳
int micVal = 0;        // 麥克風音量值
boolean toggle = false;     // LED 的狀態，預設為不亮
unsigned long nowClap = 0;  // 當前的拍手時間
unsigned long lastClap = 0; // 上次的拍手時間
unsigned int claps = 0;     // 拍手次數
unsigned long timeDiff = 0; // 拍手時間差

void setup() {
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600);
}
void loop() {
  // 讀取麥克風的音量，此電路的最高值約 790
  micVal = analogRead(micPin);

  if (micVal > 500) {     // 如果音量大於 500
    nowClap = millis();   // 儲存當前的毫秒數

    claps ++;            // 拍手次數加 1
    Serial.println(claps); // 顯示拍手次數

    if (claps == 2) {     // 若拍了兩次...
      timeDiff = nowClap - lastClap;  // 求取時間差
      // 如果兩次拍手的間隔時間在 0.3~1.5 秒之間...
      if (timeDiff > 300 && timeDiff< 1500) {
        toggle = !toggle;  // 將 LED 的狀態值反相
        claps = 0;  // 重設拍手次數
      } 
      else {
        claps = 1;  // 若第二次拍手間隔太短或太長，就算拍一次
      }
    }
    // 儲存目前時間給下一次比較「時間差」
    lastClap = nowClap;
  }
  if (toggle) {
    digitalWrite(ledPin, HIGH);
  } 
  else {
    digitalWrite(ledPin, LOW);
  }
}

