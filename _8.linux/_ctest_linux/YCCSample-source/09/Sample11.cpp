#include <iostream>
#include <string>
using namespace std;

int main()
{
   char str[100];

    cout << "請輸入字串（英數）：\n";

    cin >> str;

    cout << "字串的長度為" << strlen(str) << "。\n";

   return 0;
}
