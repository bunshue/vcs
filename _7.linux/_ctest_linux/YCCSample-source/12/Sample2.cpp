#include <iostream>
using namespace std;

//Car類別的宣告
class Car{
   private:
      int num;
      double gas;
   public:
      void show();
      void setNumGas(int n, double g);
};

//Car類別成員函數的定義
void Car::show()
{
   cout << "汽車的車牌號碼為" << num << "。\n";
   cout << "汽油容量為" << gas << "。\n";
}
void Car::setNumGas(int n, double g)
{
   if(g > 0 && g < 1000){
      num = n;
      gas = g;
      cout << "把車牌號碼設為" << num << "、汽油容量設為" << gas << "。\n";
   }
   else{
      cout << g << "不是正確的汽油容量。\n";
      cout << "無法變更汽油的容量。\n";
   }
}

int main()
{
   Car car1;

   //無法進行這種存取
   //car1.num = 1234;
   //car1.gas = 20.5;

   car1.setNumGas(1234, 20.5);
   car1.show();

   cout << "試著指定不正確的汽油容量（-10.0）...。\n";
   car1.setNumGas(1234, -10.0);
   car1.show();

   return 0;
}
