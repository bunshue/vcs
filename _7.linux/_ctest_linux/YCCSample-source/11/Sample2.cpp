#include <iostream>
using namespace std;

//���c��ƫ��ACar���ŧi
struct Car{
   int num;
   double gas;
};

int main()
{
   Car car1;

   cout << "�п�J�����C\n";
   cin >> car1.num;
   cout << "�п�J�T�o���e�q�C\n";
   cin >> car1.gas;
   cout << "���P���X�O" << car1.num << "�F�T�o���e�q�O" << car1.gas << "�C\n";

   return 0;
}
