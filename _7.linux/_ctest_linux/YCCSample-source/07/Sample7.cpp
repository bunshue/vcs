#include <iostream>
using namespace std;

//sum��ƪ��w�q
int sum(int x, int y)
{
   return x+y;
}

int main()
{
   int num1, num2, ans;

   cout << "�п�J��1�Ӿ�ơG\n";
   cin >> num1;

   cout << "�п�J��2�Ӿ�ơG\n";
   cin >> num2;

   ans = sum(num1, num2);

   cout << "�X�p��" << ans << "�C\n";

   return 0;
}
