// 動手做9-1：在 LCD 顯示器上顯示一段文字
// 詳細的程式說明，請參閱第九章，9-6頁。

#include <LiquidCrystal.h>
LiquidCrystal lcd(11, 12, 6, 5, 4, 3);

void setup() {
  lcd.begin(16, 2);
  lcd.clear();      //  清除畫面，此行可省略
  lcd.print("cubie@yahoo.com");  //  從「原點」開始輸出文字
  lcd.setCursor(5, 1);    //  改變游標位置到第 5 行、第 1 列
  lcd.print("swf.com.tw");   // 再輸出文字
}
void loop() {
}
