#include <iostream>
using namespace std;

//Base1クラスの宣言
class Base1{
   protected:
      int bs1;
   public:
      Base1(int b1=0){bs1 = b1;}
      void showBs1(); 
};

//Base2クラスの宣言
class Base2{
   protected:
      int bs2;
   public:
      Base2(int b2=0){bs2 = b2;}
      void showBs2(); 
};

//Derivedクラスの宣言
class Derived : public Base1, public Base2{
   protected:
      int dr;
   public:
      Derived(int d=0){dr = d;}
      void showDr();
};

//Base1クラスメンバ関数の定義
void Base1::showBs1()
{
   cout << "bs1は" << bs1 << "です。\n";
}

//Base2クラスメンバ関数の定義
void Base2::showBs2()
{
   cout << "bs2は" << bs2 << "です。\n";
}

//Derivedクラスメンバ関数の定義
void Derived::showDr()
{
   cout << "drは" << dr << "です。\n";
}

int main()
{
   Derived drv;

   drv.showBs1();
   drv.showBs2();
   drv.showDr();

   return 0;
}
