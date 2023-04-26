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
      Car::Car(const Car& c);
      Car& Car::operator=(const Car& c);
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
   cout << "丟棄" << pName << "。\n";
   delete[] pName;
}
Car::Car(const Car& c)
{
   cout << "用" << c.pName << "進行初始化。\n";
   pName = new char[strlen(c.pName) + strlen("的複製1")+1];
   strcpy(pName, c.pName);
   strcat(pName, "的複製1");
   num = c.num;
   gas = c.gas;
}
Car& Car::operator=(const Car& c)
{
   cout << "把" << pName << "指派給" << c.pName << "。\n";
   if(this != &c){
      delete [] pName;
      pName = new char[strlen(c.pName)+strlen("的複製2")+1];
      strcpy(pName, c.pName);
      strcat(pName, "的複製2");
      num = c.num;
      gas = c.gas;
   } 
   return *this;
}

int main()
{
   Car mycar("mycar", 1234, 25.5);

   Car car1 = mycar;

   Car car2("car2", 0, 0);
   car2 = mycar;

   return 0;
}
