// 動手做10-4：使用 atoi() 轉換字串成數值
// 詳細的程式說明，請參閱第十章，10-12頁。

byte ledPin = 11;

void setup() {
  Serial.begin(9600);
  Serial.println("LED ready.");
}

void loop() {
  int pwm;
  char data[4]; // 預設4個元素空間的陣列
  int i = 0;    // 陣列元素的索引
  char chr;     // 暫存序列輸入的字元
 
  // 查看是否有資料從序列埠送進來...
  if (Serial.available()) {
    // 讀取傳入的字元值
    while ((chr = Serial.read()) !=  '\n') {
      // 確認輸入的字元介於'0'和'9'，且索引i小於3（確保僅讀取前三個字）
      if (chr >=  '0'  && chr <=  '9' && i < 3) {
        data[i] = chr;
        i++;
      }
    }
 
    data[i]= '\0' ;    // 最後補上NULL字元
    pwm = atoi(data);  // 字串轉換成數字
    if (pwm > 255) pwm = 255;
    Serial.print("PWM: ");
    Serial.println(pwm);
    analogWrite(ledPin, pwm);
  }
}
