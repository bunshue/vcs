// 動手做9-3：序列連接 LCD 顯示模組
// 詳細的程式說明，請參閱第九章，9-14頁。

#include <Wire.h>
#include <LiquidCrystal_SR.h>
LiquidCrystal_SR lcd(8, 7, TWO_WIRE);

void setup(){
  lcd.begin(16, 2);   // 初始化 LCD
  lcd.home ();       // 重設游標原點
 
  // 顯示文字
  lcd.write("The quick brown fox jumps over the lazy dog.");
}
void loop(){
}
