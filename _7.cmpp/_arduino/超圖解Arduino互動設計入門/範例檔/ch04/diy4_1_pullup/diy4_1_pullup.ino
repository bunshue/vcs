// 啟用內建的上拉電阻，詳細的程式說明，請參閱第四章，4-14頁。
const byte LED = 13;
 const byte SW = 2;
 void setup() {
    pinMode(LED, OUTPUT);
    pinMode(SW, INPUT_PULLUP); // 啟用開關接腳內部的上拉電阻
 }
 void loop(){
    boolean val = digitalRead(SW);
    if (val == 0) {
       digitalWrite(LED, HIGH);
    }    else {
       digitalWrite(LED, LOW);
    }
 }
