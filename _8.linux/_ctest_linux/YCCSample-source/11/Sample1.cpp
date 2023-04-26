#include <iostream>
using namespace std;

//列舉型態Week的宣告
enum Week{SUN, MON, TUE, WED, THU, FRI, SAT};

int main()
{
   Week w;
   w = SUN;

   switch(w){
      case SUN: cout << "星期日。\n"; break;
      case MON: cout << "星期一。\n"; break;
      case TUE: cout << "星期二。\n"; break;
      case WED: cout << "星期三。\n"; break;
      case THU: cout << "星期四。\n"; break;
      case FRI: cout << "星期五。\n"; break;
      case SAT: cout << "星期六。\n"; break;
      default: cout << "不知道是星期幾？\n"; break;
   }

   return 0;
}
