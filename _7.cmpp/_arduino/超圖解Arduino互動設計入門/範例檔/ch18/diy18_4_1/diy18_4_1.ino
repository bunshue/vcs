const byte TOUCH_PIN = 10;   // 觸控接腳
const byte LED_PIN = 13;    // LED接腳

bool powerOn = false;   // LED電源是否開啟，預設「否」
bool lastStatus = LOW;  // 開關的上次狀態
bool btnStatus = LOW; // 開關的當前狀態

void setup() {
  pinMode(TOUCH_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  // 讀取開關當前的狀態
  btnStatus = digitalRead(TOUCH_PIN);

  // 如果目前開關的狀態是「高電位」，且之前的狀態是「低電位」…
  if (btnStatus == HIGH && lastStatus == LOW) {
powerOn = !powerOn;   // 反相電源狀態
digitalWrite(LED_PIN, powerOn);
  }

  lastStatus = btnStatus;    // 紀錄訊號狀態
}
