#include <iostream>
using namespace std;

//Car類別的宣告
class Car{
   public:
      int num;
      double gas;
      void show();
};

//Car類別成員函數的定義
void Car::show()
{
   cout << "汽車的車牌號碼為" << num << "。\n";
   cout << "汽油容量為" << gas << "。\n";
}

int main()
{
   Car car1;

   car1.num = 1234;
   car1.gas = 20.5;

   car1.show();

   return 0;
}
