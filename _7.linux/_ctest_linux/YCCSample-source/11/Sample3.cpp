#include <iostream>
using namespace std;

//結構資料型態Car的宣告
struct Car{
   int num;
   double gas;
};

int main()
{
   Car car1 = {1234, 25.5};
   Car car2 = {4567, 52.2};

   cout << "car1的車牌號碼是" << car1.num << "；汽油的容量是" << car1.gas << "。\n";
   cout << "car2的車牌號碼是" << car2.num << "；汽油的容量是" << car2.gas << "。\n";

   car2 = car1;

   cout << "把car1指定給car2。\n";

   cout << "car2的車牌號碼是" << car2.num << "；汽油的容量是" << car2.gas << "。\n";

   return 0;
}
