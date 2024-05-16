// 動手做8-6： LED 矩陣逐字捲動效果，將常數保存在「程式記憶體」裡
// 詳細的程式說明，請參閱第八章，8-38頁。

#include <avr/pgmspace.h>
#include <SPI.h>
#include "fonts_p.h"  // 引用外部的LED字元外觀定義檔

byte buffer[8] = {0,0,0,0,0,0,0,0};
// 儲存要顯示的訊息
char msg[] = {'A','r','d','u','i','n','o',' '};
int msgSize = sizeof(msg);

// 定義MAX7219暫存器值
const byte NOOP = 0x0;	        // 不運作
const byte DECODEMODE = 0x9; 	// 解碼模式
const byte INTENSITY = 0xA; 	// 顯示強度
const byte SCANLIMIT = 0xB; 	// 掃描限制
const byte SHUTDOWN = 0xC; 	// 停機
const byte DISPLAYTEST = 0xF; 	// 顯示器檢測

// 設定MAX7219暫存器資料的自訂函數
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
    buffer[7] = pgm_read_byte(&fonts[chr][j]);
    max7219 (8, buffer[7]);
    delay(100);
  }
}

void setup () {
  SPI.begin ();		    // 啟動SPI連線
  
  max7219 (SCANLIMIT, 7);   // 設定掃描8行
  max7219 (DECODEMODE, 0);  // 不使用BCD解碼
  max7219 (INTENSITY, 8);   // 設定成中等亮度
  max7219 (DISPLAYTEST, 0); // 關閉顯示器測試
  max7219 (SHUTDOWN, 1);    // 關閉停機模式（亦即，「開機」）
  
  // 清除顯示畫面（LED矩陣中的八行都設定成0）
  for (byte i=0; i < 8; i++) {
    max7219 (i + 1, 0);
  }                                     
}
 
void loop () {
 byte chr;
 for (int i = 0; i < msgSize; i++) {
   chr = *(msg + i);
   scroll(chr);
 }
}
