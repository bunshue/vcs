#include <iostream>
using namespace std;

//sum函數的定義
int sum(int x, int y)
{
   return x+y;
}

int main()
{
   int num1, num2, ans;

   cout << "請輸入第1個整數：\n";
   cin >> num1;

   cout << "請輸入第2個整數：\n";
   cin >> num2;

   ans = sum(num1, num2);

   cout << "合計為" << ans << "。\n";

   return 0;
}
