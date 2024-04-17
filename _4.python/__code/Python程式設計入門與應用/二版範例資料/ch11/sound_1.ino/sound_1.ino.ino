int buzzerPin=10;  //D9 conectted to a buzzer

void setup() {
 pinMode(buzzerPin, OUTPUT);
 }

void loop() {
  alarmBeep(buzzerPin);
  }

void alarmBeep(int pin) {
  tone(pin, 1000, 1000);
  delay(2000); 
  }
