#include <iostream>
using namespace std;

int main()
{
   int test[5] = {80,60,55,22,75};

   cout << "test[0]的值為" << test[0] << "。\n";
   cout << "test[0]的位址為" << &test[0] << "。\n";
   cout << "test的值為" << test << "。\n";
   cout << "也就是說*test的值為" << *test << "。\n";

   return 0;
}
