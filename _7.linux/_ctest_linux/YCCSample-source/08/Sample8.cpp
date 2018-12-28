#include <iostream>
using namespace std;

int main()
{
   int a = 5;
   int& rA = a;

   cout << "變數a的值為" << a << "。\n";
   cout << "參照rA的值為" << rA << "。\n";

   rA = 50;

   cout << "將50指派給rA。\n";
   cout << "參照rA的值變更為" << rA << "。\n";
   cout << "變數a的值也變更為" << a << "。\n";
   cout << "變數a的位址為" << &a << "。\n";
   cout << "參照rA位址也是" << &rA << "。\n";

   return 0;
}
