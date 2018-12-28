#include <iostream>
using namespace std;

int main()
{
   int a = 0;
   int b = 0;

   b = a++;

   cout << "指定後置遞增運算子到b之後的值為" << b << "。\n";

   return 0;
}
