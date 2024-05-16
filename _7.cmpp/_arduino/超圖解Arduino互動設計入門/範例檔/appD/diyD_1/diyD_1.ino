// 附錄D：典型的輪詢程式
// 程式說明請參閱附錄D，D-2頁。

const byte swPin = 2;         // 開關接在數位 2 腳
const byte ledPin = 13;       // LED 接在 13 腳（內建）
boolean state = LOW;          // 儲存開關的狀態值
void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(swPin, INPUT);      // 開關腳設定為「輸入」
  digitalWrite(swPin, HIGH);  // 啟用微控器內部的上拉電阻
}  
void loop(){
  // 讀取開關的狀態（高電位或低電位）
  state = digitalRead(swPin); 
  digitalWrite(ledPin, state);// 依照開關狀態點亮或關閉 LED
}
