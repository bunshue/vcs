#include <iostream>
using namespace std;

int main()
{
   int test[5] = {80,60,55,22,75};

   cout << "test[0]���Ȭ�" << test[0] << "�C\n";
   cout << "test[0]����}��" << &test[0] << "�C\n";
   cout << "test���Ȭ�" << test << "�C\n";
   cout << "�]�N�O��*test���Ȭ�" << *test << "�C\n";

   return 0;
}
