/*
 本範例程式改寫自arduino.cc官方論壇的這一篇文章：

 http://forum.arduino.cc/index.php?PHPSESSID=1mlmloei1vpish99327r5gfol0&topic=22512.15
 
 原者：
 Ryan McLaughlin <ryanjmclaughlin@gmail.com> 

本程式採用具備定時執行指定函數程式的TimerOne程式庫，
已收錄在書本光碟的libraries資料夾
讀者也可以在此網址下載： http://code.google.com/p/arduino-timerone/downloads/list

相關說明請參閱筆者網站的這一篇文章：

http://swf.com.tw/?p=501
*/

#include <TimerOne.h>

/*
 設定一個充當計算關閉TRIAC的延遲時間的「計數器」，
 其值將在每65為秒增加1，
 當i的值增加到大於或等於dim（調光值）時，
 再令TRIAC開啟。
*/
volatile int i=0;
volatile boolean zeroCross=0;  // 儲存零交越狀態的變數
const byte acPin = 3;          // TRIAC訊號輸出接腳
const byte potPin = A0;        // 可變電阻的接腳
int dim = 64;                  // 調光器的階段值 (0-128) ， 128代表關閉。

void setup() {
  pinMode(acPin, OUTPUT);                     // TRIAC的控制輸出腳
  attachInterrupt(0, zeroCrossISR, RISING);   // 偵測零交越訊號
  /* 
   執行TimerOne程式庫裡的Timer1定時觸發程式，
   參數65代表定時器的運作週期是65為秒。
  */
  Timer1.initialize(65); 
  // 設定讓定時器每隔65為秒，自動執行dim_check函數。
  Timer1.attachInterrupt(dim_check, 65);                                          
}

// 每當偵測到零交越點，底下的函數就會被執行
void zeroCrossISR() {
  zeroCross = true;        
  i=0;
  digitalWrite(acPin, LOW);  // 關閉TRIAC
}                                 

// 底下的函數將每隔65微秒觸發一次
void dim_check() {                   
  if(zeroCross) {     // 若已經過零交越點....       
    if(i>=dim) {      // 判斷是否過了延遲觸發時間...
      digitalWrite(acPin, HIGH);  // 開啟燈光       
      i=0;                        // 重設「計數器」      
      zeroCross=false;
    } 
    else {
      i++;  // 增加「計數器」                   
    }                                
  }                                  
}                                      

void loop() {
  // 讀取可變電阻的值（0~1023），除以8可得到0~127的值。  
  dim = analogRead(potPin) / 8;
}


