#include <iostream>
#include "myfunc.h"
using namespace std;

int main()
{
   int num1, num2, ans;

   cout << "請輸入第1個整數。\n";
   cin >> num1;

   cout << "請輸入第2個整數。\n";
   cin >> num2;

   ans = max(num1, num2);

   cout << "最大值為" << ans << "。\n";

   return 0;
}
