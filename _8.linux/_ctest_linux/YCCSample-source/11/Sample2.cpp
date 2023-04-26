#include <iostream>
using namespace std;

//結構資料型態Car的宣告
struct Car{
   int num;
   double gas;
};

int main()
{
   Car car1;

   cout << "請輸入車號。\n";
   cin >> car1.num;
   cout << "請輸入汽油的容量。\n";
   cin >> car1.gas;
   cout << "車牌號碼是" << car1.num << "；汽油的容量是" << car1.gas << "。\n";

   return 0;
}
