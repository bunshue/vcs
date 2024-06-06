// 動手做9-5：使用超音波感測器製作數位量尺
// 詳細的程式說明，請參閱第九章，9-29頁。

const byte trigPin = 13;  // 超音波模組的觸發腳
const int echoPin = 12;    // 超音波模組的接收腳
unsigned long d;          // 儲存高脈衝的持續時間

unsigned long ping() {
  digitalWrite(trigPin, HIGH);   // 觸發腳設定成高電位
  delayMicroseconds(5);          // 持續 5 微秒
  digitalWrite(trigPin, LOW);    // 觸發腳設定成低電位
 
  return pulseIn(echoPin, HIGH); // 傳回高脈衝的持續時間
}

void setup() {
  pinMode(trigPin, OUTPUT);  // 觸發腳設定成「輸出」
  pinMode(echoPin, INPUT);   // 接收腳設定成「輸入」
 
  Serial.begin(9600);        // 初始化序列埠
}
void loop(){
  d = ping() / 58;       // 把高脈衝時間值換算成公分單位
  Serial.print(d);       // 顯示距離
  Serial.print("cm");
  Serial.println();
  delay(1000);          // 等待一秒鐘（每隔一秒測量一次）
}
