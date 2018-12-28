#include "stdafx.h"
#include <iostream>
using namespace std;
//資料 + 功能 + 保護成員的功能 => 封裝 encapusulation
class Car{		//Car類別的宣告
        //存取指定子access specifier
        private:        //資料成員(性質)
        int num;
        double gas;
        public:         //成員函數(功能)
        static int sum; //static靜態資料成員
        Car();          //constructor overload，建構式多載，製做不同樣式的初始化
        Car(int n, double g);
        int getNum(){return num;}       //inline fx
        double getGas(){return gas;}    //inline fx
        void setCar(int n, double g);
        void show();
        static void showSum();  //static靜態成員函數
        void setNumGas(int n, double g);
};
class RacingCar : public Car{	//RacingCar類別的宣告，衍生類別的宣告
        private:
        int course;
        public:
        RacingCar();            //衍生類別的建構式
        RacingCar(int n, double g, int c);
        void setCourse(int c);
};
//Car類別成員函數的定義
Car::Car()      //建構式 constructor
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
//RacingCar類別成員函數的定義
RacingCar::RacingCar()          //建構式constructor
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
void buy(Car c)         //buy函數的定義
{
        int n = c.getNum();
        double g = c.getGas();
        cout << "購買了車牌號碼為" << n << "、汽油容量為" << g << "的車子。\n";
}
int Car::sum = 0;       //靜態資料成員的初始化
void buy(Car c);        //buy函數的宣告

int main()
{
        Car car1;       //建立物件，宣告變數car1，儲存Car類別的值
        car1.setCar(1234, 20.5);
        Car::showSum();
        Car car2;
        car2.setCar(4567, 30.5);
        Car::showSum();
        car1.setNumGas(1234, 20.5);
        buy(car1);
        RacingCar rccar1;
        rccar1.setCar(1234, 20.5);              //呼叫繼承而來的成員函數
        rccar1.setCourse(5);                    //呼叫新增的成員函數
        RacingCar rccar2(1234, 20.5, 5);
        //建構式的多載
        Car car3;
        Car car4(1234, 20.5);
		getchar();//或system("pause");
        return 0;
}



