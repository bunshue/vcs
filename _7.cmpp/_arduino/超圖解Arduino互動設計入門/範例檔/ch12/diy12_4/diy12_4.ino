// 動手做12-4：從 Arduino 發射紅外線遙控電器
// 詳細的程式說明，請參閱第十二章，12-14頁。

#include <IRremote.h>
IRsend irsend;

void setup(){
  Serial.begin(9600);
}

void loop() {
  if (Serial.read() != -1) {
    irsend.sendNEC(0xC1C7C03F, 32);
    Serial.println("Action!");
  }
}
