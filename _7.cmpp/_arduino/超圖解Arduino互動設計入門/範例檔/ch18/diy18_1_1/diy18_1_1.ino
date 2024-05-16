const byte colPins[4] = {9, 8, 7, 6};     // 設定「行」腳位
const byte rowPins[4] = {13, 12, 11, 10}; // 設定「列」腳位
const char keymap[4][4] = {     // 設定按鍵的「行、列」代表值
    {'1','2','3','A'}, 
    {'4','5','6','B'}, 
    {'7','8','9','C'},
    {'*','0','#','D'}
};

byte i, j;      // 暫存迴圈的索引數字
byte scanVal;   // 暫存掃描到的按鍵值

void setup(){
  Serial.begin(9600);

  for (i = 0; i <= 3; i++) {
    pinMode(rowPins[i], INPUT);
    pinMode(colPins[i], OUTPUT);
    digitalWrite(colPins[i], HIGH);
    digitalWrite(rowPins[i], HIGH);
  }
}

void loop() {
  for (i = 0; i <= 3; i++) {
    for (j = 0; j <= 3; j++) {
      digitalWrite(colPins[j], LOW);
      scanVal = digitalRead(rowPins[i]);

      if (scanVal == LOW) {    // 如果輸入值是「低電位」…
        Serial.println(keymap[i][j]);  // 輸出按鍵代表的字元
        delay(200);  // 掃描按鍵的間隔時間
        digitalWrite(colPins[j], HIGH);
        break;       // 跳出迴圈
      }
      digitalWrite(colPins[j], HIGH);
    }
  }
}
