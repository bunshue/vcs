#include <iostream>
using namespace std;

int main()
{
   int sum = 0;
   int num = 0;

   cout << "請輸入第1個整數。\n";
   cin >> num;
   sum += num;
   cout << "請輸入第2個整數。\n";
   cin >> num;
   sum += num;
   cout << "請輸入第3個整數。\n";
   cin >> num;
   sum += num;

   cout << "3個整數的合計為" << sum << "。\n";

   return 0;
}
