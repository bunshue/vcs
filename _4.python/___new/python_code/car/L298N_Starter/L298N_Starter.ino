//本範例適合初學L298N的人
//在小車裝好後，可用本程式先測試所有線路是否都接正確
//套件可至賣場購買
//https://goods.ruten.com.tw/item/show?21826281062806
//傑森創工製作
// https://www.facebook.com/jasonshow


// 左馬達控制設定
const byte LEFT1 = 8;  //IN1
const byte LEFT2 = 9;  //IN2
const byte LEFT_PWM = 10;

// 右馬達控制設定
const byte RIGHT1 = 7;  //IN3
const byte RIGHT2 = 6;  //IN4
const byte RIGHT_PWM = 5;

// 設定PWM輸出值（代表的是車子的速度）
byte motorSpeed = 130;

void forward() {  // 前進
  //左輪
  digitalWrite(LEFT1, HIGH);
  digitalWrite(LEFT2, LOW);
  analogWrite(LEFT_PWM, motorSpeed);
  
  //右輪。因在小車上馬達安裝方向左右兩個是相反的，所以另一隻馬達的設定要相反，兩輪才能配合。）
  digitalWrite(RIGHT1, LOW);
  digitalWrite(RIGHT2, HIGH);

  analogWrite(RIGHT_PWM, motorSpeed);
}

void backward() { // 後退
  digitalWrite(LEFT1, LOW);
  digitalWrite(LEFT2, HIGH);
  analogWrite(LEFT_PWM, motorSpeed);

  digitalWrite(RIGHT1, HIGH);
  digitalWrite(RIGHT2, LOW);
  analogWrite(RIGHT_PWM, motorSpeed);
}

void turnLeft() { // 左轉
  //左輪不動，右輪動（速度為0）
  
  analogWrite(LEFT_PWM, 0);

  digitalWrite(RIGHT1, LOW);
  digitalWrite(RIGHT2, HIGH);
  analogWrite(RIGHT_PWM, motorSpeed);
}

void turnRight() {  // 右轉
  //右輪不動，左輪動（速度為0）
  
  digitalWrite(LEFT1, HIGH);
  digitalWrite(LEFT2, LOW);
  analogWrite(LEFT_PWM, motorSpeed);
  
  analogWrite(RIGHT_PWM, 0);
}

void stopMotor() {  //停止，兩輪速度為0
  
  analogWrite(LEFT_PWM, 0);

  analogWrite(RIGHT_PWM, 0);
}

void setup() {
  //設定每一個PIN的模式
  pinMode(LEFT1, OUTPUT);
  pinMode(LEFT2, OUTPUT);
  pinMode(LEFT_PWM, OUTPUT);
  pinMode(RIGHT1, OUTPUT);
  pinMode(RIGHT2, OUTPUT);
  pinMode(RIGHT_PWM, OUTPUT);

  //forward();
  
}

void loop() {
  //本範例會讓車子向前、向後、向左、向右、停止，各2秒，然後不斷重複
  
  forward();
  delay(2000);
  backward();
  delay(2000);
  turnLeft();
  delay(2000);
  turnRight();
  delay(2000);
  stopMotor();
  delay(2000);
}