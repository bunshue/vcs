// 動手做9-4：製作數位溫濕度顯示器
// 詳細的程式說明，請參閱第九章，9-22頁。

#include <dht11.h>

dht11 DHT11;
const byte dataPin = 2;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int chk = DHT11.read(dataPin);

  /*
    底下這一行可以寫成：
    if (chk == DHTLIB_OK) {
  */
  if (chk == 0) {
    Serial.print("Humidity (%): ");

    // 強置把資料轉換成浮點（float）格式
    Serial.println((float)DHT11.humidity, 2);
    // 

    Serial.print("Temperature (oC): ");
    Serial.println((float)DHT11.temperature, 2);
 
  } else {
    Serial.println("Sensor Error");
  }

  delay(2000);
}
