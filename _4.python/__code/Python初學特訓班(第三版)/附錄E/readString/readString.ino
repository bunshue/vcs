int LED = 10;
String ReadString;
char ch;
void setup() {
   Serial.begin(9600);
}

void loop() {
   while( Serial.available() > 0) {
      ch=Serial.read(); // 讀取序列埠
      ReadString +=ch; // 將字串組合
      delay(0.01);
   }
   if (ReadString.length()>0){ // 顯示接收字串
       Serial.println("ReadString=" + ReadString);
   }
   if (ReadString == "ON") { // Led 點亮
      digitalWrite(LED, HIGH);
      ReadString="";
   }
   if (ReadString == "OFF") { // Led 熄滅
      digitalWrite(LED, LOW); 
      ReadString="";
   }
}
