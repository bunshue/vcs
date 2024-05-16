// 動手做9-4：採用 LCD 顯示器呈現溫濕度值（兩線序列LCD）
// 詳細的程式說明，請參閱第九章，9-23頁。

#include <Wire.h>
#include <LiquidCrystal_SR.h>  // 序列式 LCD 介面程式庫
#include <dht11.h>             // DHT11 感測器程式庫
LiquidCrystal_SR lcd(8, 7, TWO_WIRE); // 宣告 LCD 模組程式物件

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
