// 動手做9-4：採用 LCD 顯示器呈現溫濕度值（並接LCD）
// 詳細的程式說明，請參閱第九章，9-23頁。

#include <LiquidCrystal.h>
#include <dht11.h>      // DHT11 感測器程式庫
LiquidCrystal lcd(11, 12, 6, 5, 4, 3);

dht11 DHT11;     // 宣告溫濕度檢測器程式物件
const byte dataPin = 2;
void setup() {
  lcd.begin(16, 2);       // 初始化 LCD
 
  lcd.setCursor(4, 0);
  lcd.print("Temp");
  lcd.setCursor(0, 1);
  lcd.print("Humidity");
}
void loop() {
  int chk = DHT11.read(dataPin);
  if (chk == 0) {
    lcd.setCursor(9, 0);   // 顯示溫度
    lcd.print((float)DHT11.temperature, 2);
    lcd.print((char) 0xDF);
    lcd.print("C");
 
    lcd.setCursor(9, 1);   // 顯示濕度
    lcd.print((float)DHT11.humidity, 2);
    lcd.print("%");
  }
  delay(2000);
}
