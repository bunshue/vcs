#include <iostream>
using namespace std;

//buyｨ郛ﾆｪｺｩwｸq
int buy(int x, int y)
{
   int z;

   cout << "ｶR､F" << x << "ｸU､ｸｻP" << y << "ｸU､ｸｪｺｨｮ､l｡C\n";

   z = x+y;

   return z;
}

//buy関?の呼び出し
int main()
{
   int num1, num2, sum;

   cout << "ｭnｶRｦh､ﾖｿ�ｪｺｨｮ､l｡H\n";
   cin >> num1;

   cout << "ｭnｶRｦh､ﾖｿ�ｪｺｨｮ､l｡H\n";
   cin >> num2;

   sum = buy(num1, num2);

   cout << "ｦXｭpｬｰ" << sum << "ｸU､ｸ｡C\n";

   return 0;
}
