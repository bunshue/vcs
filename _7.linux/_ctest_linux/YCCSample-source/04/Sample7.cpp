#include <iostream>
using namespace std;

int main()
{
   int a = 1;
   int b = 0;

   cout << "short int���A���j�p��" << sizeof(short int) << "byte�C\n";
   cout << "int���A���j�p��" << sizeof(int) << "byte�C\n";
   cout << "long int���A���j�p��" << sizeof(long int) << "byte�C\n";
   cout << "float���A���j�p��" << sizeof(float) << "byte�C\n";
   cout << "double���A���j�p��" << sizeof(double) << "byte�C\n";
   cout << "long double���A���j�p��" << sizeof(long double) << "byte�C\n";
   cout << "�ܼ�a���j�p��" << sizeof(a) << "byte�C\n";
   cout << "�B�⦡a+b���j�p��" << sizeof(a+b) << "byte�C\n";

   return 0;
}
