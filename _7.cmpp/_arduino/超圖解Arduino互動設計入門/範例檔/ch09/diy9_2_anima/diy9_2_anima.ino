// 動手做9-2：在 LCD 上顯示自訂字元動畫
// 詳細的程式說明，請參閱第九章，9-12頁。

#include <LiquidCrystal.h>
LiquidCrystal lcd(11, 12, 6, 5, 4, 3);

byte sp[6][8] = {
  {B00100, B01110, B11111, B10101, B11111, B01110, B01010, B10001},
  {B00100, B01110, B11111, B11010, B11111, B00100, B01010, B01010},
  {B00100, B01110, B11111, B11110, B11111, B01110, B00100, B00100},
  {B00100, B01110, B11111, B11111, B11111, B00100, B01010, B01010},
  {B00100, B01110, B11111, B01111, B11111, B01110, B00100, B00100},
  {B00100, B01110, B11111, B01101, B11111, B00100, B01010, B01010}
};

byte index = 0;

void setup(){
  for (byte i=0; i<6; i++) {
    lcd.createChar (i, sp[i]);
  }
}

void loop(){
  lcd.setCursor(0, 0); // 游標固定在左上角
  lcd.write(index);    // 可以寫成：lcd.print(char(index));
  index ++;
  if (index > 5) {   // 將 index 值限制在 0~5 之間
    index = 0;
  }
  delay(300);        // 等待 0.3 秒再換下一個字元顯示
}
