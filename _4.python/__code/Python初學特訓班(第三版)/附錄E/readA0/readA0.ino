int LED = 10;
String ReadString;
char ch;
void setup() {
    Serial.begin(9600);
    // 設定 A0 輸入
    pinMode(A0, INPUT);
}

void loop() 
{
   int val = analogRead(A0); // 讀取 A0 埠
   // 傳送資料至電腦
   Serial.println(val);
   while( Serial.available() > 0) {
      ch=Serial.read(); // 讀取序列埠
      ReadString +=ch; // 將字串組合
      delay(0.01);
   }
   if (ReadString == "ON") { // Led 點亮
      digitalWrite(LED, HIGH);
      ReadString="";
   }
   if (ReadString == "OFF") { // Led 熄滅
      digitalWrite(LED, LOW); 
      ReadString="";
   }
   if (ReadString.length()>0){ // 顯示接收字串
       ReadString="";
   }
}
