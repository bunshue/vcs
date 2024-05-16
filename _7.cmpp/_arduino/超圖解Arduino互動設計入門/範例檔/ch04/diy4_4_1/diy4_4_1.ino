// 跑馬燈範例程式三
// 詳細的程式說明，請參閱第四章，4-27頁。

const byte LEDs[] = {8,9,10,11,12};
const byte total = sizeof(LEDs);
byte index = 0;
byte lastLightLED = 0; // 紀錄上一次點亮的LED

const byte SW = 2;     // 開關的腳位
boolean buttonState;             // 當前讀取到的開關值
boolean lastButtonState = LOW;   // 上一次紀錄的開關值
long lastDebounceTime = 0;  // 紀錄上一次開關發生變化的時間
long debounceDelay = 50;    // 消除彈跳的時間間隔（ms）

void setup() {
  for (byte i=0; i<total; i++) {
    pinMode(LEDs[i], OUTPUT);
  }
  pinMode(SW, INPUT);
}

void loop() {
  // 讀取開關腳位的狀態
  int reading = digitalRead(SW);
  
  // 以下是消除開關彈跳的程式，取自Arduino的Debounce範例
  // 若開關狀態改變，則紀錄目前的時間
  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    // 延遲一段時間（50ms）後，若確認開關狀態改變了...
    if (reading != buttonState) {
      // 讀取開關值
      buttonState = reading;
      // 若開關狀態為「高電位」...
      if (buttonState == HIGH) {
        // 熄滅上一次點亮的LED
        digitalWrite(lastLightLED, LOW);
        lastLightLED = index;
        // 點亮索引指定的LED;
        digitalWrite(LEDs[index], HIGH);
        // 設定索引值
        if (index < total) {
          index ++;
        } 
        else {
          index = 0;
        }
      }
    }
  }
  
  // 紀錄開關狀態
  lastButtonState = reading;
}


