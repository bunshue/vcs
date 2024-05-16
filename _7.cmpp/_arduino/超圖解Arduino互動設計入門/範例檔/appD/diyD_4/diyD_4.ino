// 附錄D：交流電調光器程式
// 程式說明請參閱附錄D，D-12頁。

const byte acPin = 3;    // 觸發 TRIAC 的腳位
const byte potPin = A0;  // 指定可變電阻的接腳
byte dim = 64;           // 調光器的亮度輸出（0~127，預設為一半）
// 零交越值，預設為 0，代表未達零交越點
volatile boolean zeroCross = 0;

void zeroCrosssISR()  {
  zeroCross = 1;            // 代表「已抵達零交越點」
  digitalWrite(acPin, LOW); // 關閉 TRIAC
}
void setup() {
  pinMode(acPin, OUTPUT);  // 觸發 TRIAC 的腳位要設定成「輸出」

  // 捕捉中斷 0 腳位（數位 2 腳）的上昇訊號，
  // 執行上面的 zeroCrosssISR()函數
  attachInterrupt(0, zeroCrosssISR, RISING);
}

void loop() {
  int val = analogRead(potPin); // 從 A0 腳讀取可變電阻的分壓值
  // 將電阻的 0~1023 分壓值轉變成 0~127 再存入 dim
  dim = map(val, 0, 1023, 0, 127);
  
  if (zeroCross) {                // 若已抵達零交越點，則...
    int dimTime = (65*dim);       // 計算延遲時間（單位：微秒）
    delayMicroseconds(dimTime);   // 延遲一段微秒數
    digitalWrite(acPin, HIGH);    // 觸發 TRIAC
    zeroCross = 0;                // 重設 zeroCross 變數
  }
}

