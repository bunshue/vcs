#include <iostream>
using namespace std;

//buy��ƪ��ŧi
void buy(int x=10);

//buy��ƪ��I�s
int main()
{
   cout <<  "��1���H100�U���R�J�C\n";
   buy(100);

   cout <<  "��2���H�w�]����R�J�C\n";
   buy();

   return 0;
}

//buy��ƪ��w�q
void buy(int x)
{
   cout <<  "�R�F" << x << "�U�������l�C\n";
}