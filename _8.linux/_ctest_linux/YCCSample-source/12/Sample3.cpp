#include <iostream>
using namespace std;

//Car���O���ŧi
class Car{
   private:
      int num;
      double gas;
   public:
      int getNum(){return num;}
      double getGas(){return gas;}
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
      cout << "�⨮�P���X�]��" << num << "�B��T�o�e�q�]��" << gas << "�C\n";
   }
   else{
      cout << g << "���O���T���T�o�e�q�C\n";
      cout << "�L�k�ܧ�T�o�e�q�C\n";
   }
}

//buy��ƪ��ŧi
void buy(Car c);

int main()
{
   Car car1;

   car1.setNumGas(1234, 20.5);

   buy(car1);

   return 0;
}

//buy��ƪ��w�q
void buy(Car c)
{
    int n = c.getNum();
    double g = c.getGas();
    cout << "�ʶR�F���P���X��" << n << "�B�T�o�e�q��" << g << "�����l�C\n";
}
