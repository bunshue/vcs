#include <iostream>
using namespace std;

//buy��ƪ��w�q
int buy(int x, int y)
{
   int z;

   cout << "�R�F" << x << "�U���P" << y << "�U�������l�C\n";

   z = x+y;

   return z;
}

//buy��?�̌Ăяo��
int main()
{
   int num1, num2, sum;

   cout << "�n�R�h�ֿ������l�H\n";
   cin >> num1;

   cout << "�n�R�h�ֿ������l�H\n";
   cin >> num2;

   sum = buy(num1, num2);

   cout << "�X�p��" << sum << "�U���C\n";

   return 0;
}
