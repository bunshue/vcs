#include <iostream>
using namespace std;

//Car���O���ŧi
class Car{
   public:
      int num;
      double gas;
      void show();
};

//Car���O������ƪ��w�q
void Car::show()
{
   cout << "�T�������P���X��" << num << "�C\n";
   cout << "�T�o�e�q��" << gas << "�C\n";
}

int main()
{
   Car car1;

   car1.num = 1234;
   car1.gas = 20.5;

   car1.show();

   return 0;
}
