#define LED  D2
void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  analogWrite(LED, 0);  
}
int reading = 0;
int lightness = 0;
void loop() {
  reading = analogRead(A0);
  Serial.println(reading);
  lightness = map(reading, 0, 1023, 0, 255);
  analogWrite(LED, lightness);
  delay(1000);                                     
}

