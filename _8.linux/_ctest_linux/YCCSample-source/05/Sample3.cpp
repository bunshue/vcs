#include <iostream>
using namespace std;

int main()
{
   int res; 

   cout << "請輸入一個整數：\n";

   cin >> res;

   if (res == 1){
      cout << "輸入的是1。\n";
   }
   else{
      cout << "輸入的是1以外的數字。\n";
   }

   return 0;
}
