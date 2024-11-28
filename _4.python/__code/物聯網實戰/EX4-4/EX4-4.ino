#define   tempPin   A0
#define   degreeCPin      5
#define   degreeFPin      6
#define   maxDebounce   500
int readValue = 0;  
int temp = 0;
float degreeF;
unsigned int  debounceC = 0;
unsigned int  debounceF = 0;
void setup() {
  pinMode(degreeCPin, INPUT_PULLUP);
  pinMode(degreeFPin, INPUT_PULLUP);
  Serial.begin(9600);
}
void loop() {
  if (digitalRead(degreeCPin) == LOW) {
    if (debounceC > maxDebounce) {
      debounceC = 0;
      readValue = analogRead(tempPin);
      temp = map(readValue, 0, 1023, 0, 500);
      Serial.print("The degree Celsius = ");
      Serial.println(temp);
      while (digitalRead(degreeCPin) == LOW);
    }
    else {
      debounceC++;
    }
  }
  if (digitalRead(degreeFPin) == LOW) {
    if (debounceF > maxDebounce) {
      debounceF = 0;
      readValue = analogRead(tempPin);
      temp = map(readValue, 0, 1023, 0, 500);
      Serial.print("The degree Fahrenheit = ");
      degreeF = ((float) temp)*9/5 + 32.0;
      Serial.println(degreeF);
      while (digitalRead(degreeFPin) == LOW);
    }
    else {
      debounceF++;
    }
  }
}

