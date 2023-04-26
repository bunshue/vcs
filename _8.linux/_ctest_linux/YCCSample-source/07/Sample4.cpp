#include <iostream>
using namespace std;

//buy函數的定義
void buy(int x)
{
   cout << "買了" << x << "萬元的車子。\n";
}

//buy函數的呼叫
int main()
{
   int num;

   cout << "第1台要買多少錢的車子？\n";
   cin >> num;

   buy(num);

   cout << "第2台要買多少錢的車子？\n";
   cin >> num;

   buy(num);

   return 0;
}
