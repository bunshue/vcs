#include <iostream>
using namespace std;

int main()
{
   int res;

   cout << "�аݭn�b�ĴX���פ�j��O�H\n";

   cin >> res;

   for(int i=1; i<=10; i++){
      cout << "��" << i << "�����B�z�C\n";
      if(i == res)
         break;
   }

   return 0;
}

