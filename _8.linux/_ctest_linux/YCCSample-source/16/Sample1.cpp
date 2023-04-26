#include <iostream>
using namespace std;

int main()
{
   int i;
   double d;
   char str[100];

   cout << "請輸入整數值。\n";
   cin >> i;
   cout << "請輸入小數值。\n";
   cin >> d;
   cout << "請輸入一個字串。\n";
   cin >> str;

   cout << "所輸入的整數值為" << i << "。\n";
   cout << "所輸入的小數值為" << d << "。\n";
   cout << "所輸入的字串為" << str << "。\n";

   return 0;
}
