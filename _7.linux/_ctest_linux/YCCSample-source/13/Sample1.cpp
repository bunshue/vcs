#include <iostream>
using namespace std;

//Car���O���ŧi
class Car{
   private:
      int num;
      double gas;
   public:
      Car();
      void show();
};

//Car���O������ƪ��w�q
Car::Car()
{
   num = 0;
   gas = 0.0;
   cout << "�s�@�F�@���T���C\n";
}
void Car::show()
{
   cout << "�T�������P���X��" << num << "�C\n";
   cout << "�T�o�e�q��" << gas << "�C\n";
}

int main()
{
   Car car1;

   car1.show();

   return 0;
}
