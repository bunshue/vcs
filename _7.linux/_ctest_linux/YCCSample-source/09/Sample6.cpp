#include <iostream>
using namespace std;

int main()
{
   int test[5] = {80,60,55,22,75};

   cout << "test[0]���Ȭ�" << test[0] << "�C\n";
   cout << "test[0]���a�}��" << &test[0] << "�C\n";
   cout << "test���Ȭ�" << test << "�C\n";
   cout << "test+1���Ȭ�" << test+1 << "�C\n";   
   cout << "*(test+1)���Ȭ�" << *(test+1) << "�C\n";   

   return 0;
}
