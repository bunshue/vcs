// 跑馬燈範例程式三
// 詳細的程式說明，請參閱第四章，4-27頁。

const byte LEDs[] = {8,9,10,11,12};
const byte total = sizeof(LEDs);
byte index = 0;

void setup() {
  for (byte i=0; i<total; i++) {
    pinMode(LEDs[i], OUTPUT);
  }
}

void loop() {
  for (byte i=0; i<total; i++) {
    digitalWrite(LEDs[i], LOW);
  }

  digitalWrite(LEDs[index], HIGH);
  if (index < total) {
    index ++;
  } 
  else {
    index = 0;
  }
  delay(100);
}


