#include <iostream>
using namespace std;

//Car�N���X�̐錾
class Car{
   private:
      int num;
      double gas;
   public:
      Car();
      Car(int n, double g);
      void setCar(int n, double g);
      void show();
};

//RacingCar�N���X�̐錾
class RacingCar : public Car{
   private:
      int course;
   public:
      RacingCar();
      RacingCar(int n, double g, int c);
      void setCourse(int c);
};

//Car�N���X�����o�֐��̒�`
Car::Car()
{
   num = 0;
   gas = 0.0;
   cout << "�Ԃ��쐬���܂����B\n";
}
Car::Car(int n, double g)
{
   num = n;
   gas = g;
   cout << "�i���o�[" << num << "�K�\������" << gas << "�̎Ԃ��쐬���܂����B\n";
}
void Car::setCar(int n, double g)
{
   num = n;
   gas = g;
   cout << "�i���o�[��" << num << "�ɃK�\�����ʂ�" << gas << "�ɂ��܂����B\n";
}
void Car::show()
{
   cout << "�Ԃ̃i���o�[��" << num << "�ł��B\n";
   cout << "�K�\�����ʂ�" << gas << "�ł��B\n";
}

//RacingCar�N���X�����o�֐��̒�`
RacingCar::RacingCar()
{
   course = 0;
   cout << "���[�V���O�J�[���쐬���܂����B\n";
}
RacingCar::RacingCar(int n, double g, int c) : Car(n, g)
{
   course = c;
   cout << "�R�[�X�ԍ�" << course << "�̃��[�V���O�J�[���쐬���܂����B\n";
}
void RacingCar::setCourse(int c)
{
   course = c;
   cout << "�R�[�X�ԍ���" << course << "�ɂ��܂����B\n";
}

int main()
{
   RacingCar rccar1(1234, 20.5, 5);

   return 0;
}
