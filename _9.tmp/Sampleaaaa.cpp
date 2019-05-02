


#include <iostream>
using namespace std;

//Car類別的宣告
class Car{
   private:
      int num;
      double gas;
   public:
      static int sum;
      Car();
      Car(int n, double g);
      int getNum(){return num;}
      double getGas(){return gas;}
	void setCar(int n, double g);
      void show();
	static void showSum();
      void setNumGas(int n, double g);
};

//RacingCar類別的宣告
//RacingCarクラスの宣言
class RacingCar : public Car{
   private:
      int course;
   public:
      RacingCar();
      RacingCar(int n, double g, int c);
      void setCourse(int c);
};

//Car類別成員函數的定義
Car::Car()
{
   num = 0;
   gas = 0.0;
   sum++;
   cout << "製作了汽車。\n";
}
Car::Car(int n, double g)
{
   num = n;
   gas = g;
   cout << "製作了一輛車牌為" << num << "、汽油容量為" << gas <<"的汽車。\n";
}
void Car::setCar(int n, double g)
{
   num = n;
   gas = g;
   cout << "製作了一輛車牌為" << num << "、汽油容量為" << gas <<"的汽車。\n";
}

void Car::showSum()
{
   cout << "全部一共有" << sum << "輛汽車。\n";
}
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

//RacingCarクラスメンバ関数の定義
RacingCar::RacingCar()
{
   course = 0;
   cout << "レーシングカーを作成しました。\n";
}
RacingCar::RacingCar(int n, double g, int c) : Car(n, g)
{
   course = c;
   cout << "コース番号" << course << "のレーシングカーを作成しました。\n";
}
void RacingCar::setCourse(int c)
{
   course = c;
   cout << "コース番号を" << course << "にしました。\n";
}



int Car::sum = 0;

//buy函數的宣告
void buy(Car c);

int main()
{
/*
   Car mycars[3]={
      Car(),
      Car(1234,25.5),
      Car(4567,52.2)
   };
   */

   Car car1;
   car1.setCar(1234, 20.5);

   Car::showSum();

   Car car2;
   car2.setCar(4567, 30.5);

   Car::showSum();

   car1.setNumGas(1234, 20.5);

   buy(car1);


   RacingCar rccar1;
   rccar1.setCar(1234, 20.5);
   rccar1.setCourse(5);


   RacingCar rccar2(1234, 20.5, 5);

   return 0;
}

//buy函數的定義
void buy(Car c)
{
    int n = c.getNum();
    double g = c.getGas();
    cout << "購買了車牌號碼為" << n << "、汽油容量為" << g << "的車子。\n";
}



