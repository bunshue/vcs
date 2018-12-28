#include <iostream>
using namespace std;

//Carクラスの宣言
class Car{
   protected:
      int num;
      double gas;
   public:
      Car();
      void setCar(int n, double g);
      void show();
};

//RacingCarクラスの宣言
class RacingCar : public Car{
   private:
      int course;
   public:
      RacingCar();
      void setCourse(int c);
      void show();
};

//Carクラスメンバ関数の定義
Car::Car()
{
   num = 0;
   gas = 0.0;
   cout << "車を作成しました。\n";
}
void Car::setCar(int n, double g)
{
   num = n;
   gas = g;
   cout << "ナンバーを" << num << "にガソリン量を" << gas << "にしました。\n";
}
void Car::show()
{
   cout << "車のナンバーは" << num << "です。\n";
   cout << "ガソリン量は" << gas << "です。\n";
}

//RacingCarクラスメンバ関数の定義
RacingCar::RacingCar()
{
   course = 0;
   cout << "レーシングカーを作成しました。\n";
}
void RacingCar::setCourse(int c)
{
   course = c;
   cout << "コース番号を" << course << "にしました。\n";
}
void RacingCar::show()
{
   cout << "レーシングカーのナンバーは" << num << "です。\n";
   cout << "ガソリン量は" << gas << "です。\n";
   cout << "コース番号は" << course << "です。\n";
}

int main()
{
   RacingCar rccar1;
   rccar1.setCar(1234, 20.5);
   rccar1.setCourse(5);

   rccar1.show();

   return 0;
}
