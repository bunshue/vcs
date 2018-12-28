#include <iostream>
using namespace std;

int main()
{
   int a = 5;
   int b = 10;
   int* pA;

   pA = &a;

   cout << "變數a的值為" << a << "。\n";
   cout << "指標pA的值為" << pA << "。\n";	
   cout << "*pA的值為" << *pA << "。\n";

   pA = &b;

   cout << "變數b的值為" << b << "。\n";
   cout << "指標pA的值為" << pA << "。\n";
   cout << "*pA的值為" << *pA << "。\n";

   return 0;
}
