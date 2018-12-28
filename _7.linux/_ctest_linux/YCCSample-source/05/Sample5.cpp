#include <iostream>
using namespace std;

int main()
{
   int res; 

   cout << "請輸入一個整數：\n";

   cin >> res;

   switch(res){
      case 1:
         cout << "輸入的是1。\n";
         break;
      case 2:
         cout << "輸入的是2。\n";
         break;
      default:
         cout << "請輸入1或2。\n";
         break;
   }

   return 0;
}
