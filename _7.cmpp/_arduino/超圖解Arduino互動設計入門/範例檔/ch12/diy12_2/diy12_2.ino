// 動手做12-2：使用 IRremote 程式庫解析紅外線遙控值
// 詳細的程式說明，請參閱第十二章，12-9頁。

#include <IRremote.h>

int RECV_PIN = 11;

IRrecv irrecv(RECV_PIN);
decode_results results;

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    irrecv.resume();
  }
}
