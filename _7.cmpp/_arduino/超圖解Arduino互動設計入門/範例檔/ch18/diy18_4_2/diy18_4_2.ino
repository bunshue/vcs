const byte LED_PIN = 5;    // LED燈的接腳
const byte PWR_LED = 13;   // 電源指示燈的接腳

bool powerOn = false;   // LED電源是否開啟，預設「否」
bool btnStatus;         // 按鈕狀態
int pwmVal = 0;         // 電源輸出值

// 宣告觸鍵的自訂結構類型
typedef struct {
  byte pin;         // 按鍵的接腳編號
  bool lastStatus;  // 上次的狀態
} key;

// 宣告電源鍵的接腳和預設狀態
key powerKey = { 10, LOW };

// 宣告「調亮」鍵的接腳和預設狀態
key upKey = { 11, LOW };

// 宣告「調暗」鍵的接腳和預設狀態
key downKey = { 12, LOW };

void setup() {
  Serial.begin(9600);
  pinMode(powerKey.pin, INPUT);
  pinMode(upKey.pin, INPUT);
  pinMode(downKey.pin, INPUT);
  pinMode(LED_PIN, OUTPUT);
  pinMode(PWR_LED, OUTPUT);
}

void loop() {
  // 讀取電源鍵的狀態
  btnStatus = digitalRead(powerKey.pin);

  // 如果電源鍵的訊號從低電位變成高電位…
  if (btnStatus && powerKey.lastStatus == LOW) {
    powerOn = !powerOn;  // 反相電源狀態
    digitalWrite(PWR_LED, powerOn);

    if (powerOn) {  // 若powerOn為true…
      // 依照pwmVal的值點亮LED
      analogWrite(LED_PIN, pwmVal);
    } else {
     // 關閉LED燈
     digitalWrite(LED_PIN, LOW);
    }
  }
  // 紀錄這次的電源鍵訊號狀態
  powerKey.lastStatus = btnStatus;

  // 讀取「調亮」鍵的狀態
  btnStatus = digitalRead(upKey.pin);
  
  // 若「有開啟電源」且「此按鍵訊號是高電位」且「前次訊號是低電位」
  if (powerOn && btnStatus && upKey.lastStatus == LOW) {
    // 增加亮度值，每次增加10，不能超過255。
    if ((pwmVal+10) <= 255) {
      pwmVal += 10;
      Serial.println(pwmVal);
      analogWrite(LED_PIN, pwmVal);
    } 
  }
  upKey.lastStatus = btnStatus;

  // 讀取「調暗」鍵的狀態
  btnStatus = digitalRead(downKey.pin);

  if (powerOn && btnStatus && downKey.lastStatus == LOW) {
    // 減少亮度值，最低值為0
    if ((pwmVal-10) >= 0) {
      pwmVal -= 10;
      Serial.println(pwmVal);
      analogWrite(LED_PIN, pwmVal);
    }
  }
  downKey.lastStatus = btnStatus;
}
