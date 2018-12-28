#include <iostream>
using namespace std;

int main()
{
   char res; 

   cout << "你是男生嗎？\n";
   cout << "請輸入Y或N。\n";

   cin >> res;

   if (res == 'Y' || res == 'y'){
      cout << "你是男生喔！\n";
     }
   else if(res == 'N' || res == 'n'){
      cout << "你是女生喔！\n";
   }
   else{
      cout << "請輸入Y或N。\n";
   }

   return 0;
}
