#include <iostream>
using namespace std;

//Car摸
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

//Car摸Θㄧ计﹚竡
Car::Car()
{
   num = 0;
   gas = 0.0;
   sum++;
   cout << "籹═ó\n";
}
void Car::setCar(int n, double g)
{
   num = n;
   gas = g;
   cout << "籹进ó礟" << num << "═猳甧秖" << gas <<"═ó\n"; 
}
void Car::showSum()
{
   cout << "场Τ" << sum << "进═ó\n";
}
void Car::show()
{
   cout << "═óó礟腹絏" << num << "\n";
   cout << "═猳甧秖" << gas << "\n";
}

int Car::sum = 0;

//Car摸ノ
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
