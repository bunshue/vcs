#include <iostream>
using namespace std;

int main()
{
   int* pA;

   pA = new int;

   cout << "�i��ʺA�O����t�m�C\n";

   *pA = 10;

   cout << "�ϥΰt�m�O����A" << "��X" << *pA << "�C\n";

   delete pA;

   cout << "����t�m�O����C\n";

   return 0;
}
