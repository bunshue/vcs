#include <Servo.h>
Servo servoMotor1;  
int degree = 0;   
void setup() {
  servoMotor1.attach(5);  
}
void loop() {
  for (degree = 0; degree <= 180; degree += 2) {
    servoMotor1.write(degree);              
    delay(20);                       
  }
  delay(1000);
  servoMotor1.write(0);
}
