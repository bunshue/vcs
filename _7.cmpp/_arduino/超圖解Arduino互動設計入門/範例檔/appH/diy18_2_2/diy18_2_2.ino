// 動手做18-2：使用 memcmp() 函數比較陣列值
// 詳細的程式說明，請參閱第十八章，18-16頁。

byte tagA[3] = {1, 2, 3};
byte tagB[3] = {4, 5, 6};

void setup() {
  Serial.begin(9600);

  if (memcmp(tagA, tagB, 3) == 0) {
    Serial.println("YES!");
  } 
  else {
    Serial.println("NO!");
  }
}

void loop() {
}

