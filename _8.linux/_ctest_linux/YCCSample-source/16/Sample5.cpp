#include <iostream>
using namespace std;

int main()
{
   double pi = 3.141592;
   int num;

   cout << "輸出圓周率。\n";
   cout << "要輸出有效小數點幾位數？(1～7)\n";
   cin >> num;

   cout.precision(num);

   cout << "圓周為" << pi << "。\n";

   return 0;
}

