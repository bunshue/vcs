#include <iostream>
using namespace std;

//max函數的定義
inline int max(int x, int y){if(x>y) return x; else return y;}

int main()
{
   int num1, num2, ans;

   cout << "請輸入第1個整數：\n";
   cin >> num1;

   cout << "請輸入第2個整數：\n";
   cin >> num2;

   ans = max(num1, num2);

   cout << "最大值為" << ans << "。\n";

   return 0;
}
