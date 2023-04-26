#include <iostream>
using namespace std;

int main()
{
   int* pA;

   pA = new int;

   cout << "進行動態記憶體配置。\n";

   *pA = 10;

   cout << "使用配置記憶體，" << "輸出" << *pA << "。\n";

   delete pA;

   cout << "釋放配置記憶體。\n";

   return 0;
}
