#include <iostream>
using namespace std;

//���c��ƫ��ACar���ŧi
struct Car{
   int num;
   double gas;
};

//show��ƪ��ŧi
void show(Car* pC);

int main()
{
   Car car1 = {0, 0.0};

   cout << "�п�J�������X�C\n";
   cin >> car1.num;

   cout << "�п�J�T�o���e�q�C\n";
   cin >> car1.gas;

   show(&car1);

   return 0;
}

//show��ƪ��w�q
void show(Car* pC)
{
   cout << "���P���X�O" << pC->num << "�F�T�o���e�q�O" << pC->gas << "�C\n";
}
