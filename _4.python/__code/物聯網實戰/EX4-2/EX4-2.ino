#define   relayPin   5
#define   buttonPin  6
#define   maxDebounce   500
unsigned int  debounce = 0;
void setup() {
  pinMode(relayPin, OUTPUT);
  digitalWrite(relayPin, HIGH);
  pinMode(buttonPin, INPUT_PULLUP);
}
void loop() {
  if (digitalRead(buttonPin) == LOW) {
    if (debounce > maxDebounce) {
      digitalWrite(relayPin, LOW);
      debounce = 0;
      while (digitalRead(buttonPin) == LOW);
    }
    else {
      debounce++;
    }
  }
  else digitalWrite(relayPin, HIGH);
}
