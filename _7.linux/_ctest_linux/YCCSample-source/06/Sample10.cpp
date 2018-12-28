#include <iostream>
using namespace std;

int main()
{
   int res;

   cout << "請問要在第幾次終止迴圈呢？\n";

   cin >> res;

   for(int i=1; i<=10; i++){
      cout << "第" << i << "次的處理。\n";
      if(i == res)
         break;
   }

   return 0;
}

