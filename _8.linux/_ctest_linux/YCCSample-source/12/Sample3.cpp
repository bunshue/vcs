#include <iostream>
using namespace std;

//Car類別的宣告
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
      cout << "把車牌號碼設為" << num << "、把汽油容量設為" << gas << "。\n";
   }
   else{
      cout << g << "不是正確的汽油容量。\n";
      cout << "無法變更汽油容量。\n";
   }
}

//buy函數的宣告
void buy(Car c);

int main()
{
   Car car1;

   car1.setNumGas(1234, 20.5);

   buy(car1);

   return 0;
}

//buy函數的定義
void buy(Car c)
{
    int n = c.getNum();
    double g = c.getGas();
    cout << "購買了車牌號碼為" << n << "、汽油容量為" << g << "的車子。\n";
}
