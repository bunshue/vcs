#include <iostream>
using namespace std;

int main()
{
   int num = 1;

   while(num){
      cout << "請輸入一個整數：（以0結束）\n";
      cin >> num;
      cout << "輸入" << num << "。\n";
   }
   cout << "迴圈結束。\n";

   return 0;
}
