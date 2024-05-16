// 動手做7-2：序列連接七段顯示器
// 詳細的程式說明，請參閱第七章，7-13頁。

const byte dataPin = 2;    // 74HC595 序列腳接「數位 2」
const byte latchPin = 3;   // 74HC595 暫存器時脈腳接「數位 3」
const byte clockPin = 4;   // 74HC595 序列時脈腳接「數位 4」
byte index = 0;            // 七段顯示器的數字索引

const byte LEDs[10] = {
  B01111110,
  B00110000,
  B01101101,
  B01111001,
  B00110011,
  B01011011,
  B01011111,
  B01110000,
  B01111111,
  B01110011
};

void setup() {
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin, OUTPUT);
}

void loop() {
  digitalWrite(latchPin, LOW);   // 關上閘門
  shiftOut(dataPin, clockPin, LSBFIRST, LEDs[index]);
  digitalWrite(latchPin, HIGH);  // 開啟閘門
  delay(1000);       // 暫停一秒
  index ++;
  if (index == 10) {
    index = 0;
  }
}

