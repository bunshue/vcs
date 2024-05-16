// 動手做9-1：在 LCD 顯示器上顯示日文字元
// 詳細的程式說明，請參閱第九章，9-9頁。

#include <LiquidCrystal.h>
LiquidCrystal lcd(11, 12, 6, 5, 4, 3);

void setup() {
  lcd.begin(16, 2);
  lcd.clear();
  
  char str[] = {'8', 'b', 'i', 't', ' ', 0xCF, 0xB2, 0xBA, 0xDD, 0};
  lcd.print(str);
}
void loop() {
}
