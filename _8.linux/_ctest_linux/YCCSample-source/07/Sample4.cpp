#include <iostream>
using namespace std;

//buy��ƪ��w�q
void buy(int x)
{
   cout << "�R�F" << x << "�U�������l�C\n";
}

//buy��ƪ��I�s
int main()
{
   int num;

   cout << "��1�x�n�R�h�ֿ������l�H\n";
   cin >> num;

   buy(num);

   cout << "��2�x�n�R�h�ֿ������l�H\n";
   cin >> num;

   buy(num);

   return 0;
}
