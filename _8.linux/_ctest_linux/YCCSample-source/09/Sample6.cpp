#include <iostream>
using namespace std;

int main()
{
   int test[5] = {80,60,55,22,75};

   cout << "test[0]的值為" << test[0] << "。\n";
   cout << "test[0]的地址為" << &test[0] << "。\n";
   cout << "test的值為" << test << "。\n";
   cout << "test+1的值為" << test+1 << "。\n";   
   cout << "*(test+1)的值為" << *(test+1) << "。\n";   

   return 0;
}
