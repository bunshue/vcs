#include <iostream>
using namespace std;

int main()
{
   char ch;

   cout << "請連續輸入字元。\n";

   while(cin.get(ch)){
      cout.put(ch);
   }

   return 0;
}
