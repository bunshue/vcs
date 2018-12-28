#include <iostream>
using namespace std;

//Car類別的宣告
class Car{
   private:
      int num;
      double gas;
   public:
      Car(int n=0, double g=0);
      void show();
};

//Car類別成員函數的定義
Car::Car(int n, double g)
{
   num = n;
   gas = g;
   cout << "製作了一輛車牌為" << num << "、汽油容量為" << gas <<"的汽車。\n";
}
void Car::show()
{
   cout << "汽車的車牌號碼為" << num << "。\n";
   cout << "汽油容量為" << gas << "。\n";
}

int main()
{
   Car car1;
   Car car2(1234, 20.5);

   return 0;
}
