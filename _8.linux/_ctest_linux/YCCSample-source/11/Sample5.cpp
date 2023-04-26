#include <iostream>
using namespace std;

//結構資料型態Car的宣告
struct Car{
   int num;
   double gas;
};

//show函數的宣告
void show(Car* pC);

int main()
{
   Car car1 = {0, 0.0};

   cout << "請輸入車號號碼。\n";
   cin >> car1.num;

   cout << "請輸入汽油的容量。\n";
   cin >> car1.gas;

   show(&car1);

   return 0;
}

//show函數的定義
void show(Car* pC)
{
   cout << "車牌號碼是" << pC->num << "；汽油的容量是" << pC->gas << "。\n";
}
