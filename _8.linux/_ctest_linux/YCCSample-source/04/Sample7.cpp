#include <iostream>
using namespace std;

int main()
{
   int a = 1;
   int b = 0;

   cout << "short int型態的大小為" << sizeof(short int) << "byte。\n";
   cout << "int型態的大小為" << sizeof(int) << "byte。\n";
   cout << "long int型態的大小為" << sizeof(long int) << "byte。\n";
   cout << "float型態的大小為" << sizeof(float) << "byte。\n";
   cout << "double型態的大小為" << sizeof(double) << "byte。\n";
   cout << "long double型態的大小為" << sizeof(long double) << "byte。\n";
   cout << "變數a的大小為" << sizeof(a) << "byte。\n";
   cout << "運算式a+b的大小為" << sizeof(a+b) << "byte。\n";

   return 0;
}
