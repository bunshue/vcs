#include <iostream>
using namespace std;

int main()
{
   int a = 5;
   int& rA = a;

   cout << "�ܼ�a���Ȭ�" << a << "�C\n";
   cout << "�ѷ�rA���Ȭ�" << rA << "�C\n";

   rA = 50;

   cout << "�N50������rA�C\n";
   cout << "�ѷ�rA�����ܧ�" << rA << "�C\n";
   cout << "�ܼ�a���Ȥ]�ܧ�" << a << "�C\n";
   cout << "�ܼ�a����}��" << &a << "�C\n";
   cout << "�ѷ�rA��}�]�O" << &rA << "�C\n";

   return 0;
}
