#include <iostream>
using namespace std;

//buy函數的定義
void buy(int x, int y)
{
   cout << "買了" << x << "萬元與" << y << "萬元的車子。\n";
}

//buy函數的呼叫
int main()
{
   int num1, num2;

   cout << "要買多少錢的車子？\n";
   cin >> num1;

   cout << "要買多少錢的車子？\n";
   cin >> num2;

   buy(num1, num2);

   return 0;
}
