#include <iostream>
using namespace std;

//Car���O���ŧi
class Car{
   private:
      int num;
      double gas;
   public:
      void show();
      void setNumGas(int n, double g);
};

//Car���O������ƪ��w�q
void Car::show()
{
   cout << "�T�������P���X��" << num << "�C\n";
   cout << "�T�o�e�q��" << gas << "�C\n";
}
void Car::setNumGas(int n, double g)
{
   if(g > 0 && g < 1000){
      num = n;
      gas = g;
      cout << "�⨮�P���X�]��" << num << "�B�T�o�e�q�]��" << gas << "�C\n";
   }
   else{
      cout << g << "���O���T���T�o�e�q�C\n";
      cout << "�L�k�ܧ�T�o���e�q�C\n";
   }
}

int main()
{
   Car car1;

   //�L�k�i��o�ئs��
   //car1.num = 1234;
   //car1.gas = 20.5;

   car1.setNumGas(1234, 20.5);
   car1.show();

   cout << "�յ۫��w�����T���T�o�e�q�]-10.0�^...�C\n";
   car1.setNumGas(1234, -10.0);
   car1.show();

   return 0;
}
