#include <iostream>
using namespace std;

int main()
{
   int a = 5;
   int b = 10;
   int* pA;

   pA = &a;

   cout << "�ܼ�a���Ȭ�" << a << "�C\n";
   cout << "����pA���Ȭ�" << pA << "�C\n";	
   cout << "*pA���Ȭ�" << *pA << "�C\n";

   pA = &b;

   cout << "�ܼ�b���Ȭ�" << b << "�C\n";
   cout << "����pA���Ȭ�" << pA << "�C\n";
   cout << "*pA���Ȭ�" << *pA << "�C\n";

   return 0;
}
