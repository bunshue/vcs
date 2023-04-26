#include <iostream>
using namespace std;
//資料 + 功能 + 保護成員的功能 => 封裝 encapusulation
class Car{		//Car類別的宣告，基礎類別
        //存取指定子access specifier
        private:        //資料成員(性質)
        int num;
        double gas;
        public:         //成員函數(功能)
        static int sum; //static靜態資料成員
        Car();          //constructor overload，建構式多載，製做不同樣式的初始化
        Car(int n, double g);
	   ~Car();		//destructor解構式的宣告
        int getNum(){return num;}       //inline fx
        double getGas(){return gas;}    //inline fx
        void setCar(int n, double g);
        void show();
        static void showSum();  //static靜態成員函數，即使未建立物件也可以進行呼叫
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
Car::~Car()	//解構式destructor，解構式不能有參數
{
        cout << "把一個物件丟棄\n";
	  sum--;
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
        cout << "做成賽車\n";
}
RacingCar::RacingCar(int n, double g, int c) : Car(n, g)
{
        course = c;
        cout << "做成把跑到號碼設為" << course << "的賽車。\n";
}
void RacingCar::setCourse(int c)
{
        course = c;
        cout << "把跑到號碼設為" << course << "\n";
}
void buy(Car c)         //buy函數的定義
{
        int n = c.getNum();
        double g = c.getGas();
        cout << "購買了車牌號碼為" << n << "、汽油容量為" << g << "的車子。\n";
}
int Car::sum = 0;       //靜態資料成員的初始化
void buy(Car c);        //buy函數的宣告


int main()      //使用指向基底類別的指標
{
        Car* pCars[2];          //準備基底類別的指標

        Car car1;               //作成基底類別的物件
        RacingCar rccar1;       //作成衍生類別的物件

        pCars[0] = &car1;
        pCars[0] -> setCar(1234, 20.5);         //雙方都可以用指向基底類別的指標的陣列來處理

        pCars[1] = &rccar1;
        pCars[1] -> setCar(4567, 30.5);

        for(int i = 0; i<2; i++) {
                pCars[i] -> show();     //呼叫show()成員函數
        }
        return 0;
}



