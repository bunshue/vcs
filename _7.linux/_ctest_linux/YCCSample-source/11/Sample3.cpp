#include <iostream>
using namespace std;

//���c��ƫ��ACar���ŧi
struct Car{
   int num;
   double gas;
};

int main()
{
   Car car1 = {1234, 25.5};
   Car car2 = {4567, 52.2};

   cout << "car1�����P���X�O" << car1.num << "�F�T�o���e�q�O" << car1.gas << "�C\n";
   cout << "car2�����P���X�O" << car2.num << "�F�T�o���e�q�O" << car2.gas << "�C\n";

   car2 = car1;

   cout << "��car1���w��car2�C\n";

   cout << "car2�����P���X�O" << car2.num << "�F�T�o���e�q�O" << car2.gas << "�C\n";

   return 0;
}
