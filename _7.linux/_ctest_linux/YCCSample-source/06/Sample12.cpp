#include <iostream>
using namespace std;

int main()
{
   int res;

   cout << "�n���L�ĴX�����B�z�H�]1��10�^\n";

   cin >> res;

   for(int i=1; i<=10; i++){
      if(i == res)
         continue;
      cout << "��" << i << "�����B�z�C\n";
   }

   return 0;
}
