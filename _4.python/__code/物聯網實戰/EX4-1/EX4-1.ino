#define   LEDPin           3
#define   buttonPin        2
#define   maxDebounce   500
unsigned int  debounce = 0;
bool preState = false;
void setup() {
  pinMode(LEDPin, OUTPUT);
  digitalWrite(LEDPin, LOW);
  pinMode(buttonPin, INPUT_PULLUP);
}
void loop() {
  if (digitalRead(buttonPin) == LOW) {
    if (debounce > maxDebounce) {
      digitalWrite(LEDPin, !preState);
      preState = !preState;
      debounce = 0;
      while (digitalRead(buttonPin) == LOW);
    }
    else {
      debounce++;
    }
  }
}

