#include <iostream>
using namespace std;

//buy��ƪ��w�q
void buy(int x, int y)
{
   cout << "�R�F" << x << "�U���P" << y << "�U�������l�C\n";
}

//buy��ƪ��I�s
int main()
{
   int num1, num2;

   cout << "�n�R�h�ֿ������l�H\n";
   cin >> num1;

   cout << "�n�R�h�ֿ������l�H\n";
   cin >> num2;

   buy(num1, num2);

   return 0;
}
