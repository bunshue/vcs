#include <iostream>
using namespace std;

int main()
{
   const double pi = 3.1415;

   cout << "圓周率的值為" << pi << "。\n";
   cout << "圓周率的值無法變更。\n";

   //無法以指定的方式作變更
   //pi = 1.44;

   return 0;
}
