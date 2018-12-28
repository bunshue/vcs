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
   buy(20);
   buy(50);

   return 0;
}
