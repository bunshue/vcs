#include <iostream>
#include "myfunc.h"
using namespace std;

int main()
{
   int num1, num2, ans;

   cout << "�п�J��1�Ӿ�ơC\n";
   cin >> num1;

   cout << "�п�J��2�Ӿ�ơC\n";
   cin >> num2;

   ans = max(num1, num2);

   cout << "�̤j�Ȭ�" << ans << "�C\n";

   return 0;
}
