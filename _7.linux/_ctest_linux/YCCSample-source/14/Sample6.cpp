#include <iostream>
using namespace std;

//Vehicleクラスの宣言
class Vehicle{
   protected:
      int speed;
   public:
      void setSpeed(int s);
      virtual void show() = 0;
};

//Carクラスの宣言
class Car : public Vehicle{
   private:
      int num;
      double gas;
   public:
      Car(int n, double g);
      void show();
};

//Planeクラスの宣言
class Plane : public Vehicle{
   private:
      int flight;
   public:
      Plane(int f);
      void show();
};

//Vehicleクラスメンバ関数の定義
void Vehicle::setSpeed(int s)
{
   speed = s;
   cout << "速度を" << speed << "にしました。\n";
}

//Carクラスメンバ関数の定義
Car::Car(int n, double g)
{
   num = n;
   gas = g;
   cout << "ナンバー" << num << "ガソリン量を" << gas << "の車を作成しました。\n";
}
void Car::show()
{
   cout << "車のナンバーは" << num << "です。\n";
   cout << "ガソリン量は" << gas << "です。\n";
   cout << "速度は" << speed << "です。\n";
}

//Planeクラスメンバ関数の定義
Plane::Plane(int f)
{
   flight = f;
   cout << "便" << flight << "の飛行機を作成しました。\n";
}
void Plane::show()
{
   cout << "飛行機の便は" << flight << "です。\n";
   cout << "速度は" << speed << "です。\n";
}

int main()
{
   Vehicle* pVc[2];

   Car car1(1234, 20.5);
   pVc[0] = &car1;
   pVc[0]->setSpeed(60);

   Plane pln1(232);
   pVc[1] = &pln1;
   pVc[1]->setSpeed(500);

   for(int i=0; i<2 ;i++){
      pVc[i]->show();
   }
}
