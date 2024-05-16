// 動手做5-3：透過「序列埠繪圖家」 呈現訊號波形
// 詳細的程式說明，請參閱第五章，5-25頁。

const byte LED = 13;    // LED接數位第13腳
const byte SW = 12;    // 開關接數位第12腳

void setup() {
  pinMode(LED, OUTPUT);       // LED 接腳設定成「輸出」
  pinMode(SW, INPUT_PULLUP);  // 啟用開關接腳內部的上拉電阻
  Serial.begin(9600);
}

void loop(){
  bool val = digitalRead(SW);  // 讀取開關的數值
  if (val == 0) {               // 如果開關是低電位
    digitalWrite(LED, HIGH);    // 打開LED燈
  } else {
    digitalWrite(LED, LOW);     // 關閉LED燈
  }

  Serial.println(val);  // 請使用println()輸出序列資料
}
