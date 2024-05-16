// 動手做8-6： LED 矩陣逐字捲動效果程式之一
// 詳細的程式說明，請參閱第八章，8-32頁。

#include <SPI.h>
#include "fonts.h" // 引用外部的 LED 字元外觀定義檔
byte buffer[8] = {0, 0, 0, 0, 0, 0, 0, 0};
// 儲存要顯示的訊息
char msg[] = { 'A', 'r', 'd', 'u', 'i', 'n', 'o', ' ' };
int msgSize = sizeof(msg);
// 定義 MAX7219 暫存器值
const byte NOOP = 0x0;         // 不運作
const byte DECODEMODE = 0x9;   // 解碼模式
const byte INTENSITY = 0xA;    // 顯示強度
const byte SCANLIMIT = 0xB;    // 掃描限制
const byte SHUTDOWN = 0xC;     // 停機
const byte DISPLAYTEST = 0xF;  // 顯示器檢測
// 設定 MAX7219 暫存器資料的自訂函數
void max7219 (const byte reg, const byte data) {
  digitalWrite (SS, LOW);
  SPI.transfer (reg);
  SPI.transfer (data);
  digitalWrite (SS, HIGH);
}

// 捲動字元
void scroll(byte chr) {
  for (byte j = 0; j<8; j++) {
    for (byte i=0; i<7; i++) {
      buffer[i] = buffer[i+1];
      max7219 (i + 1, buffer[i]);
    }
    buffer[7] = fonts[chr][j];
    max7219 (8, buffer[7]);
    delay(100);
  }
}
void setup () {
  SPI.begin ();             // 啟動 SPI 連線
 
  max7219 (SCANLIMIT, 7);   // 設定掃描 8 行
  max7219 (DECODEMODE, 0);  // 不使用 BCD 解碼
  max7219 (INTENSITY, 8);   // 設定成中等亮度
  max7219 (DISPLAYTEST, 0); // 關閉顯示器測試
  max7219 (SHUTDOWN, 1);    // 關閉停機模式（亦即，「開機」）
 
  // 清除顯示畫面（LED 矩陣中的八行都設定成 0）
  for (byte i=0; i < 8; i++) {
    max7219 (i + 1, 0);
  }
}

void loop () {
  byte chr;
  // 從 msg 陣列的第 0 個字元開始，每次從中取出一個字...
  for (int i = 0; i < msgSize; i++) {
    chr = msg[i];
    scroll(chr);
  }
}
