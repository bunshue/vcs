#include <iostream>
using namespace std;

//Car�N���X�̐錾
class Car{
   protected:
      int num;
      double gas;
   public:
      Car();
      void setCar(int n, double g);
      void show();
};

//RacingCar�N���X�̐錾
class RacingCar : public Car{
   private:
      int course;
   public:
      RacingCar();
      void setCourse(int c);
      void show();
};

//Car�N���X�����o�֐��̒�`
Car::Car()
{
   num = 0;
   gas = 0.0;
   cout << "�Ԃ��쐬���܂����B\n";
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
void RacingCar::setCourse(int c)
{
   course = c;
   cout << "�R�[�X�ԍ���" << course << "�ɂ��܂����B\n";
}
void RacingCar::show()
{
   cout << "���[�V���O�J�[�̃i���o�[��" << num << "�ł��B\n";
   cout << "�K�\�����ʂ�" << gas << "�ł��B\n";
   cout << "�R�[�X�ԍ���" << course << "�ł��B\n";
}

int main()
{
   RacingCar rccar1;
   rccar1.setCar(1234, 20.5);
   rccar1.setCourse(5);

   rccar1.show();

   return 0;
}
