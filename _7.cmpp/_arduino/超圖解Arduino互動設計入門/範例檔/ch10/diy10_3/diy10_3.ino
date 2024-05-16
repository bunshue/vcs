// 動手做10-3：透過序列埠調整燈光亮度
// 詳細的程式說明，請參閱第十章，10-10頁。

byte ledPin = 11;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int pwm = 0;
  byte _in;
  // 查看是否有資料從序列埠送進來...
  if (Serial.available()) {
    _in = Serial.read();
    // 若尚未收到「換行」字元...
    while (_in !=  '\n') {
      // 確認字元值介於 '0' （ASCII 值 48）和 '9' （57）之間，
      // 也可以寫成：if (_in >= 48 && _in <= 57) {
      if (_in >=  '0'  && _in <=  '9') {
        pwm = pwm * 10 + (_in -  '0');
      }
      // 讀取下一個字元
      _in = Serial.read();
    }
    // 確認不超過 PWM 的 255 最高值
    if (pwm > 255) {
      pwm = 255;
    }
    // 輸出 PWM
    analogWrite(ledPin, pwm);
  }
}

