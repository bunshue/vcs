// 動手做8-5：在矩陣 LED 上顯示動態圖像
// 詳細的程式說明，請參閱第八章，8-28頁。

#include <SPI.h>
// 定義動態圖像內容
const byte sprite[4][8] = {
  { 0x30, 0xBC, 0x6E, 0x3E, 0x3E, 0x6E, 0xBC, 0x30 },
  { 0x18, 0xBE, 0x57, 0x1F, 0x1F, 0x57, 0xBE, 0x18 },
  { 0x30, 0x7C, 0xAE, 0x3E, 0x3E, 0xAE, 0x7C, 0x30 },
  { 0x18, 0x9E, 0x57, 0xBF, 0xBF, 0x57, 0x9E, 0x18 }
};

// 定義 MAX7219 暫存器值
const byte NOOP = 0x0;        // 不運作
const byte DECODEMODE = 0x9;  // 解碼模式
const byte INTENSITY = 0xA;   // 顯示強度
const byte SCANLIMIT = 0xB;   // 掃描限制
const byte SHUTDOWN = 0xC;    // 停機
const byte DISPLAYTEST = 0xF; // 顯示器檢測
// 設定 MAX7219 暫存器資料的自訂函數
void max7219 (const byte reg, const byte data) {
  digitalWrite (SS, LOW);
  SPI.transfer (reg);
  SPI.transfer (data);
  digitalWrite (SS, HIGH);
}
void setup () {
  SPI.begin ();             // 啟動 SPI 連線

  max7219 (SCANLIMIT, 7);   // 設定掃描 8 行
  max7219 (DECODEMODE, 0);  // 不使用 BCD 解碼
  max7219 (INTENSITY, 8);   // 設定成中等亮度
  max7219 (DISPLAYTEST, 0); // 關閉顯示器測試
  max7219 (SHUTDOWN, 1);    // 關閉停機模式（亦即，「開機」）

  // 清除顯示畫面
  for (byte i=0; i < 8; i++) {
    max7219 (i + 1, 0);
  }
}

void loop () {
  for (byte j = 0; j<4; j++) {  // 一共 4 個畫面
    for (byte i=0; i<8; i++) {  // 每個畫面 8 行
      max7219 (i + 1, sprite[j][i]);
    }
    delay(100);
  }
}

