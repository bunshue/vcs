#include <iostream>
using namespace std;

int main()
{
   int a;
   int* pA;

   a = 5;
   pA = &a;

   cout << "�ܼ�a���Ȭ�" << a << "�C\n";

   *pA = 50;

   cout << "�N50������*pA�C\n";
   cout << "�ܼ�a���Ȭ�" << a << "�C\n";

   return 0;
}
