#include <iostream>
using namespace std;

//buy¨ç¼Æªº©w¸q
int buy(int x, int y)
{
   int z;

   cout << "¶R¤F" << x << "¸U¤¸»P" << y << "¸U¤¸ªº¨®¤l¡C\n";

   z = x+y;

   return z;
}

//buyŠÖ?‚ÌŒÄ‚Ño‚µ
int main()
{
   int num1, num2, sum;

   cout << "­n¶R¦h¤Ö¿úªº¨®¤l¡H\n";
   cin >> num1;

   cout << "­n¶R¦h¤Ö¿úªº¨®¤l¡H\n";
   cin >> num2;

   sum = buy(num1, num2);

   cout << "¦X­p¬°" << sum << "¸U¤¸¡C\n";

   return 0;
}
