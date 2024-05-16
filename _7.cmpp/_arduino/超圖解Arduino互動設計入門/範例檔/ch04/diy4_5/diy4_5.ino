// 跑馬燈範例程式四
// 詳細的程式說明，請參閱第四章，4-29頁。

byte data = B00001;    // B 要大寫，也可以寫成 0b00001
byte shift = 0;        // 位移的位元數
byte max = 5;          // 最大位移數
void setup(){
  DDRB = B011111;      // 8~12 腳設成輸出。
}
void loop() {
  PORTB = data << shift;
  shift ++;
  if (shift == max) {
    shift = 0;
  }
  delay(100);
}
