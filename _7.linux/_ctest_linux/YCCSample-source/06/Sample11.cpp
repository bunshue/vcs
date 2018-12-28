#include <iostream>
using namespace std;

int main()
{
   int res; 

   cout << "請輸入成績（1～5）：\n";

   cin >> res;

   switch(res){
      case 1:
      case 2:
         cout << "還要再加強唷！\n";
         break;
      case 3:
      case 4:
         cout << "就照這個樣子保持下去。\n";
         break;
      case 5:
         cout << "相當優秀唷！\n";
         break;
      default:
         cout << "請輸入成績（1～5）：\n";
         break;
   }
   
   return 0;
}
