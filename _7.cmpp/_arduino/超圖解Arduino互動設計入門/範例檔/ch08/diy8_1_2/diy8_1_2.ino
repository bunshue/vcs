// 動手做8-1：建立自訂函數，函數原型
// 詳細的程式說明，請參閱第八章，8-6頁。

float cirArea(int);

void setup() {
  Serial.begin(9600);
  float ans = cirArea(10);
  Serial.println(ans);
}
void loop() {
}

float cirArea(int r) {
  float area = 3.14 * r * r;
  return area;
}
