#include <iostream>
using namespace std;

int main()
{
   int a;
   int* pA;

   a = 5;
   pA = &a;

   cout << "�ܼ�a���Ȭ�" << a << "�C\n";
   cout << "�ܼ�a����}(&a)��" << &a << "�C\n";
   cout << "����pA���Ȭ�" << pA << "�C\n";	

   return 0;
}
