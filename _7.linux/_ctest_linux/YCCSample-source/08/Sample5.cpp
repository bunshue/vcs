#include <iostream>
using namespace std;

int main()
{
   int a;
   int* pA;

   a = 5;
   pA = &a;

   cout << "變數a的值為" << a << "。\n";

   *pA = 50;

   cout << "將50指派給*pA。\n";
   cout << "變數a的值為" << a << "。\n";

   return 0;
}
