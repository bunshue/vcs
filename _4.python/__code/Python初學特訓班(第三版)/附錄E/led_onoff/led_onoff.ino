int LED = 10; // Pin 10
void setup() {
   Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    if (Serial.read() == 'H') {
      digitalWrite(LED, HIGH); // 燈亮
    }else{
      digitalWrite(LED, LOW);  // 燈熄
    }
  }
  delay(1);
}
