// 動手做14-2：用 Android 手機藍牙遙控機器人
// 詳細的程式說明，請參閱第十四章，14-17頁。

#include <SoftwareSerial.h>    // 引用「軟體序列埠」程式庫
SoftwareSerial BT(3, 2);    // 設定軟體序列埠(接收腳, 傳送腳)

char command;                  // 接收序列埠值的變數
const byte EA = 6;             // 馬達 A 的致能接腳
const byte IA = 7;             // 馬達 A 的正反轉接腳
const byte EB = 5;             // 馬達 B 的致能接腳
const byte IB = 4;             // 馬達 B 的正反轉接腳

// 設定 PWM 輸出值
const byte speed = 130;

void stop() {               // 馬達停止
  analogWrite(EA, 0);        // 馬達 A 的 PWM 輸出
  analogWrite(EB, 0);        // 馬達 B 的 PWM 輸出
}
void forward() {             // 馬達轉向：前進
  analogWrite(EA, speed);    // 馬達 A 的 PWM 輸出
  digitalWrite(IA, HIGH);
  analogWrite(EB, speed);    // 馬達 B 的 PWM 輸出
  digitalWrite(IB, HIGH); 
}
void backward() {            // 馬達轉向：後退
  analogWrite(EA, speed);    // 馬達 A 的 PWM 輸出
  digitalWrite(IA, LOW);
  analogWrite(EB, speed);    // 馬達 B 的 PWM 輸出
  digitalWrite(IB, LOW);
}
void turnLeft() {            // 馬達轉向：左轉
  analogWrite(EA, speed);    // 馬達 A 的 PWM 輸出
  digitalWrite(IA, LOW);     // 馬達 A 反轉
  analogWrite(EB, speed);    // 馬達 B 的 PWM 輸出
  digitalWrite(IB, HIGH);
}
void turnRight() {           // 馬達轉向：右轉
  analogWrite(EA, speed);    // 馬達 A 的 PWM 輸出
  digitalWrite(IA, HIGH);
  analogWrite(EB, speed);    // 馬達 B 的 PWM 輸出
  digitalWrite(IB, LOW);     // 馬達 B 反轉
}

void setup() {
  BT.begin(9600);            // 啟動軟體序列埠

  pinMode(IA, OUTPUT);       // 馬達 A 的致能腳位
  pinMode(IB, OUTPUT);       // 馬達 B 的致能腳位
  stop();                    // 先停止馬達
}

void loop() {
  if (BT.available() > 0) {
    command = BT.read();

    switch (command) {
    case  'w' :     // 接收到 'w'，前進
      forward();
      break;
    case  'x' :     // 接收到 'x'，後退
      backward();
      break;
    case  'a' :     // 接收到 'a'，左轉
      turnLeft();
      break;
    case  'd' :     // 接收到 'd'，右轉
      turnRight();
      break;
    case  's' :     // 接收到 's'，停止馬達
      stop();
      break;
    }
  }
}
