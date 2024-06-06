const byte TrigPin = 13;  // 超音波模組的觸發腳
const int EchoPin = 12;   // 超音波模組的接收腳
const int dangerThresh = 580; // 10cm × 58
const byte speed = 100;   // 馬達的 PWM 輸出值
long distance;            // 暫存接收訊號的高電位持續時間
const byte ENA = 5;   // 馬達 A 的致能接腳
const byte ENB = 6;   // 馬達 B 的致能接腳

const byte IN1 = 10; // 馬達 A 的正反轉接腳
const byte IN2 = 9;  // 馬達 A 的正反轉接腳
const byte IN3 = 8;  // 馬達 B 的正反轉接腳
const byte IN4 = 7;  // 馬達 B 的正反轉接腳

byte dir = 0; // 記錄行進狀態，0 代表「前進」，1 代表「右轉」

void stop() { // 馬達停止
    analogWrite(ENA, 0); // 馬達 A 的 PWM 輸出
    analogWrite(ENB, 0); // 馬達 B 的 PWM 輸出
}

void forward() { // 馬達轉向：前進（兩個馬達都正轉）
    analogWrite(ENA, speed); // 馬達 A 的 PWM 輸出
    digitalWrite(IN1, HIGH); // 請參閱表 10-4 的設定
    digitalWrite(IN2, LOW);
    analogWrite(ENB, speed); // 馬達 B 的 PWM 輸出
    digitalWrite(IN3, HIGH); // 請參閱表 10-4 的設定
    digitalWrite(IN4, LOW);
}

void backward() { // 馬達轉向：後退（兩個馬達都反轉）
    analogWrite(ENA, speed); // 馬達 A 的 PWM 輸出
    digitalWrite(IN1, LOW); // 請參閱表 10-4 的設定
    digitalWrite(IN2, HIGH);
    analogWrite(ENB, speed); // 馬達 B 的 PWM 輸出
    digitalWrite(IN3, LOW); // 請參閱表 10-4 的設定
    digitalWrite(IN4, HIGH); 
}

void turnLeft() { // 馬達轉向：左轉（馬達 A 反轉、馬達 B 正轉）
    analogWrite(ENA, speed); // 馬達 A 的 PWM 輸出
    digitalWrite(IN1, LOW); // 請參閱表 10-4 的設定
    digitalWrite(IN2, HIGH);
    analogWrite(ENB, speed); // 馬達 B 的 PWM 輸出
    digitalWrite(IN3, HIGH); // 請參閱表 10-4 的設定
    digitalWrite(IN4, LOW);
}

void turnRight() { // 馬達轉向：右轉（馬達 A 正轉、馬達 B 反轉）
    analogWrite(ENA, speed); // 馬達 A 的 PWM 輸出
    digitalWrite(IN1, HIGH); // 請參閱表 10-4 的設定
    digitalWrite(IN2, LOW);
    analogWrite(ENB, speed); // 馬達 B 的 PWM 輸出
    digitalWrite(IN3, LOW); // 請參閱表 10-4 的設定
    digitalWrite(IN4, HIGH);
}

long ping() { // 超音波感測程式
    digitalWrite(TrigPin, HIGH);     // 觸發腳設定成高電位
    delayMicroseconds(10);          // 持續 10 微秒
    digitalWrite(TrigPin, LOW); // 觸發腳設定成低電位
    return pulseIn(EchoPin, HIGH); // 測量高電位的持續時間（μs ）
}

void setup(){
    pinMode(TrigPin, OUTPUT); // 觸發腳設定成「輸出」
    pinMode(EchoPin, INPUT); // 接收腳設定成「輸入」
    pinMode(IN1, OUTPUT);    // 馬達控制板的接腳全都設定成「輸出」
    pinMode(IN2, OUTPUT);
    pinMode(IN3, OUTPUT);
    pinMode(IN4, OUTPUT);
}

void loop(){ 
    distance = ping(); // 讀取障礙物的距離
    if (distance>dangerThresh) {
        // 如果距離大於 10cm... 
        if (dir != 0) { // 如果目前的行進狀態不是「前進」
            dir = 0;  // 設定成「前進」 
            stop();
            delay(500);  // 暫停馬達 0.5 秒
        } 
        
        forward(); // 前進
    } else {
        if (dir != 1) { // 如果目前的狀態不是「右轉」
            dir = 1;  // 設定成「右轉」
            stop();
            delay(500);  // 暫停馬達 0.5 秒
        } 
        turnRight();
    }
    delay(1000);
}
