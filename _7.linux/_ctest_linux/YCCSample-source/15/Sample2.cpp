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
      void show();
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
   cout << "��" << pName << "���C\n";
   delete[] pName;
}
void Car::show()
{
   cout << "�T�������P���X��" << num << "�C\n";
   cout << "�T���e�q��" << gas << "�C\n";
   cout << "�W�٬�" << pName << "�C\n";
}

//Car���O���Q��
int main()
{
   Car car1("mycar", 1234, 25.5);
   car1.show();

   return 0;
}
