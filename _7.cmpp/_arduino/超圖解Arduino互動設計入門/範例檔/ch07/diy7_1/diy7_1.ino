// 動手做7-1：連接 LED 七段顯示器與Arduino板
// 詳細的程式說明，請參閱第七章，7-5頁。

byte index = 0;
const byte LEDs[10] = {
  B1111110,
  B0110000,
  B1101101,
  B1111001,
  B0110011,
  B1011011,
  B1011111,
  B1110000,
  B1111111,
  B1111011
};
void setup(){
  DDRD = B11111111; // 將 0~7 腳全設定成「輸出」
}
void loop() {
  // 從 LEDs 陣列中，取出 0~9 元素，
  // 一開始先取出第 0 個元素並由「埠口 D」輸出
  PORTD = LEDs[index];

  index ++;       // 將 index 值加 1
  // 為了確保 index 值在 0~9 之間循環，當 index 值等於 10 時，
  // 將它重設為 0
  if (index == 10) {
    index = 0;
  }
  delay(1000);      // 暫停一秒
}

