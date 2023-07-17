#include <SPI.h>
#include <RF24.h>
#include <printf.h>

RF24 radio(2, 4);  // CE, CSN
byte w_pipe[] = "11111";
byte r_pipe[] = "22222";  // 增加

void setup() {
    Serial.begin(9600);
    printf_begin();
    delay(100);
    radio.begin();
    radio.setRetries(15, 15);
    radio.openReadingPipe(1, r_pipe); // 增加
    radio.openWritingPipe(w_pipe);
    radio.printDetails();  
    radio.startListening();   // 增加
}

char data[32];
void loop() {
  if (Serial.available()) {
    // 從序列埠讀資料
    delay(10);
    int n = Serial.available();
    Serial.readBytes(data, n);
    data[n] = '\0';

    // 將資料送到樹莓派
    radio.stopListening(); 
    radio.write(data, strlen(data));
    radio.startListening(); 
    printf("send '%s', len=%d\n", data, strlen(data));
  }

  if (radio.available()) {
    // 取得從樹莓派送回來的資料
    radio.read(data, 32);
    printf("\t=> %s\n", data);
  }
}
