// 動手做5-1：從序列埠監控視窗觀察變數值
// 詳細的程式說明，請參閱第五章，5-16頁。

const byte ledPin = 13;

void setup() {
  Serial.begin(9600);
  Serial.println("Hello," );  
  Serial.print("\tLED pin is: ");
  Serial.print(ledPin);
  Serial.print("\nBYE!");
}

void loop() {
}

/*

Serial.println("AAAA" );
Serial.println("BBBB" );
Serial.println("CCCC" );

Serial.print("AAAA");
Serial.print("BBBB");
Serial.print("CCCC");

*/