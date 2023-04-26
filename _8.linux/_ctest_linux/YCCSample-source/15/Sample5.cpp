#include <iostream>
using namespace std;

int main()
{
   int num;
   cout << "請輸入1～9之間的任一數字。\n";
   cin >> num;

   try{
      if(num <= 0)
         throw "輸入了0以下";
      if(num >= 10)
         throw "輸入了10以上";
      cout << num << "。\n";
   }

   catch(char* err){
      cout << "錯誤：:" << err << '\n';
      return 1;
   }

   return 0;
}
