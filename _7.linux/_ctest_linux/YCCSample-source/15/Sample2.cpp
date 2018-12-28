#include <iostream>
#include <string>
using namespace std;

//Car類別的宣告
class Car{
   private:
      int num;
      double gas;
      char* pName;
   public:
      Car::Car(char* pN ,int n, double g);
      ~Car();
      void show();
};

//Car類別成員函式的定義
Car::Car(char* pN ,int n, double g)
{
   pName = new char[strlen(pN)+1];
   strcpy(pName, pN);
   num = n;
   gas = g;
   cout << "建立了" << pName << "。\n";
}
Car::~Car()
{
   cout << "把" << pName << "丟棄。\n";
   delete[] pName;
}
void Car::show()
{
   cout << "汽車的車牌號碼為" << num << "。\n";
   cout << "汽車容量為" << gas << "。\n";
   cout << "名稱為" << pName << "。\n";
}

//Car類別的利用
int main()
{
   Car car1("mycar", 1234, 25.5);
   car1.show();

   return 0;
}
