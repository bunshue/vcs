#include <iostream>
using namespace std;

//max��ƪ��ŧi
int max(int x, int y);


//max��ƪ��I�s
int main()
{
   int num1, num2, ans;

   cout << "�п�J��1�Ӿ�ơG\n";
   cin >> num1;

   cout << "�п�J��2�Ӿ�ơG\n";
   cin >> num2;

   ans = max(num1, num2);

   cout << "�̤j�Ȭ�" << ans << "�C\n";

   return 0;
}

//max��ƪ��w�q
int max(int x, int y)
{
   if (x > y)
      return x;
   else
      return y;
}
