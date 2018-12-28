#include <iostream>
using namespace std;

int main()
{
   int num1 = 2;
   int num2 = 3;
   int sum = num1+num2;

   cout << "變數num1的值是" << num1 << "。\n";
   cout << "變數num2的值是" << num2 << "。\n";
   cout << "num1+num2的值是" << sum << "。\n";

   num1 = num1+1;

   cout << "變數num1的值加1後是" << num1 << "。\n";

   return 0;
}
