#include <CapacitiveSensor.h>
#define threshold 1500  // 定義感測電容的臨界值

byte LEDs[] = {11, 12, 13};  // LED接腳

CapacitiveSensor cs[] = {
  CapacitiveSensor(4,5),
  CapacitiveSensor(4,6),
  CapacitiveSensor(4,7)
};

void setup() {
  pinMode(LEDs[0], OUTPUT);
  pinMode(LEDs[1], OUTPUT);
  pinMode(LEDs[2], OUTPUT);
}

void loop() {
  for (byte i=0; i<3; i++) {
    if (cs[i].capacitiveSensor(30) > threshold) {
      digitalWrite(LEDs[i], HIGH);
    } else {
      digitalWrite(LEDs[i], LOW);
    }
  }
}
