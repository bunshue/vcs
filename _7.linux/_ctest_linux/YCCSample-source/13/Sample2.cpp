#include <iostream>
using namespace std;

//Car���O���ŧi
class Car{
   private:
      int num;
      double gas;
   public:
      Car();
      Car(int n, double g);
      void show();
};

//Car���O������ƪ��w�q
Car::Car()
{
   num = 0;
   gas = 0.0;
   cout << "�s�@�F�@���T���C\n";
}
Car::Car(int n, double g)
{
   num = n;
   gas = g;
   cout << "�s�@�F�@�����P��" << num << "�B�T�o�e�q��" << gas <<"���T���C\n";
}
void Car::show()
{
   cout << "�T�������P���X��" << num << "�C\n";
   cout << "�T�o�e�q��" << gas << "�C\n";
}

int main()
{
   Car car1;
   Car car2(1234, 20.5);

   return 0;
}
