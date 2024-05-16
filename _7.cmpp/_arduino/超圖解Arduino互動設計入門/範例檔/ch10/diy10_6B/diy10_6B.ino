// 動手做10-6：自動迴避障礙物的自走車
// 詳細的程式說明，請參閱第十章，10-32頁。

const byte TrigPin = 13;      // 超音波模組的觸發腳
const int EchoPin = 12;       // 超音波模組的接收腳
const int dangerThresh = 580; // 10cm × 58
const byte speed = 100;       // 馬達的 PWM 輸出值

long distance;  // 暫存接收訊號的高電位持續時間
const byte EA = 6; // 馬達 A 的致能接腳
const byte IA = 7; // 馬達 A 的正反轉接腳
const byte EB = 5; // 馬達 B 的致能接腳
const byte IB = 4; // 馬達 B 的正反轉接腳

byte dir = 0; // 記錄行進狀態，0 代表「前進」，1 代表「右轉」

void stop() { // 馬達停止
  analogWrite(EA, 0); // 馬達 A 的 PWM 輸出
  analogWrite(EB, 0); // 馬達 B 的 PWM 輸出
}

void forward() { // 馬達轉向：前進
  analogWrite(EA, speed); // 馬達 A 的 PWM 輸出
  digitalWrite(IA, HIGH);
  analogWrite(EB, speed); // 馬達 B 的 PWM 輸出
  digitalWrite(IB, HIGH);
}

void backward() { // 馬達轉向：後退
  analogWrite(EA, speed); // 馬達 A 的 PWM 輸出
  digitalWrite(IA, LOW);
  analogWrite(EB, speed); // 馬達 B 的 PWM 輸出
  digitalWrite(IB, LOW);
}

void turnLeft() { // 馬達轉向：左轉
  analogWrite(EA, speed); // 馬達 A 的 PWM 輸出
  digitalWrite(IA, LOW);  // 馬達 A 反轉
  analogWrite(EB, speed); // 馬達 B 的 PWM 輸出
  digitalWrite(IB, HIGH);
}

void turnRight() { // 馬達轉向：右轉
  analogWrite(EA, speed); // 馬達 A 的 PWM 輸出
  digitalWrite(IA, HIGH);
  analogWrite(EB, speed); // 馬達 B 的 PWM 輸出
  digitalWrite(IB, LOW);  // 馬達 B 反轉
}

long ping() { // 超音波感測程式
  digitalWrite(TrigPin, HIGH); // 觸發腳設定成高電位
  delayMicroseconds(5);    // 持續 5 微秒
  digitalWrite(TrigPin, LOW);  // 觸發腳設定成低電位

  return pulseIn(EchoPin, HIGH); // 測量高電位的持續時間（μs）
}

void setup(){
  pinMode(TrigPin, OUTPUT);  // 觸發腳設定成「輸出」
  pinMode(EchoPin, INPUT);   // 接收腳設定成「輸入」
  pinMode(IA, OUTPUT);
  pinMode(IB, OUTPUT);
}

void loop(){
  distance = ping(); // 讀取障礙物的距離
  if (distance>dangerThresh) { // 如果距離大於 10cm...
    if (dir != 0) { // 如果目前的行進狀態不是「前進」
      dir = 0; // 設定成「前進」
      stop();  // 暫停馬達 0.5 秒
      delay(500);
    }
    forward(); // 前進
  } 
  else {
    if (dir != 1) { // 如果目前的狀態不是「右轉」
      dir = 1; // 設定成「右轉」
      stop();  // 暫停馬達 0.5 秒
      delay(500);
    }
    turnRight(); // 向右轉
  }
  delay(1000);   // 持續 1 秒
}

