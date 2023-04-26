#include <iostream>
#include <string>
using namespace std;

//Car���O���ŧi
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

//Car���O�����禡���w�q
Car::Car(char* pN ,int n, double g)
{
   pName = new char[strlen(pN)+1];
   strcpy(pName, pN);
   num = n;
   gas = g;
   cout << "�إߤF" << pName << "�C\n";
}
Car::~Car()
{
   cout << "���" << pName << "�C\n";
   delete[] pName;
}
Car::Car(const Car& c)
{
   cout << "��" << c.pName << "�i���l�ơC\n";
   pName = new char[strlen(c.pName) + strlen("���ƻs1")+1];
   strcpy(pName, c.pName);
   strcat(pName, "���ƻs1");
   num = c.num;
   gas = c.gas;
}
Car& Car::operator=(const Car& c)
{
   cout << "��" << pName << "������" << c.pName << "�C\n";
   if(this != &c){
      delete [] pName;
      pName = new char[strlen(c.pName)+strlen("���ƻs2")+1];
      strcpy(pName, c.pName);
      strcat(pName, "���ƻs2");
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
