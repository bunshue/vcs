#define photoPin    A0
int readValue = 0;  
float Vout = 0;
const float R1 = 10000;
const float Vr = 5.0;
float R2 = 0;
void setup() {
  Serial.begin(9600);
}
void loop() {
  readValue = map(analogRead(photoPin),0,1023,0,500);
  Vout = (float) readValue/100.0;
  Serial.print("Voltage Reading = ");
  Serial.println(Vout);
  R2 = Vout*R1/(Vr - Vout);
  Serial.print("Resistance of photoresistor = ");
  Serial.println(R2);
  delay(5000);
}
