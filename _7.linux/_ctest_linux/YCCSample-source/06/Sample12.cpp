#include <iostream>
using namespace std;

int main()
{
   int res;

   cout << "要跳過第幾次的處理？（1～10）\n";

   cin >> res;

   for(int i=1; i<=10; i++){
      if(i == res)
         continue;
      cout << "第" << i << "次的處理。\n";
   }

   return 0;
}
