#include <iostream>
using namespace std;

//Car���O���ŧi
class Car{
   private:
      int num;
      double gas;
   public:
      static int sum;
      Car();
      void setCar(int n, double g);
      void show();
      static void showSum();
};

//Car���O������ƪ��w�q
Car::Car()
{
   num = 0;
   gas = 0.0;
   sum++;
   cout << "�s�@�F�T���C\n";
}
void Car::setCar(int n, double g)
{
   num = n;
   gas = g;
   cout << "�s�@�F�@�����P��" << num << "�B�T�o�e�q��" << gas <<"���T���C\n"; 
}
void Car::showSum()
{
   cout << "�����@�@��" << sum << "���T���C\n";
}
void Car::show()
{
   cout << "�T�������P���X��" << num << "�C\n";
   cout << "�T�o�e�q��" << gas << "�C\n";
}

int Car::sum = 0;

//Car���O���Q��
int main()
{
   Car::showSum();

   Car car1;
   car1.setCar(1234, 20.5);

   Car::showSum();

   Car car2;
   car2.setCar(4567, 30.5);

   Car::showSum();

   system("pause");
   return 0;
}
