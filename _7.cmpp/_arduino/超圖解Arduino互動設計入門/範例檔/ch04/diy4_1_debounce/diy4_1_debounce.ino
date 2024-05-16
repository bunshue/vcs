// 消除開關的彈跳訊號，詳細的程式說明，請參閱第四章，4-15頁。

const byte LED = 13;   // LED 的腳位
const byte SW = 2;     // 開關的腳位
boolean lastState = LOW; // 記錄上次的開關狀態，預設為「低電位」
boolean toggle = LOW;    // 輸出給 LED 的訊號，預設為「低電位」
byte click = 0;        // 開關訊號的改變次數，預設為 0

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(SW, INPUT);
  lastState = digitalRead(SW);   // 讀取開關的初始值
}

void loop() {
  boolean b1 = digitalRead(SW);

  if (b1 != lastState) {     // 如果和之前的開關值不同...
    delay(20);               // 等待 20 毫秒
    boolean b2 = digitalRead(SW);   // 再讀取一次開關值

    if (b1 == b2) {    // 確認兩次開關值是否一致
      lastState = b1; // 儲存開關的狀態
      click ++;       // 增加訊號變化次數
    }
  }

  if (click == 2) {    // 如果開關狀態改變兩次
    click = 0;         // 狀態次數歸零
    toggle = !toggle;            // 取相反值
    digitalWrite(LED, toggle);   // 輸出
  }
}

