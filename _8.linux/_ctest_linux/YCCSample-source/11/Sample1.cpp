#include <iostream>
using namespace std;

//�C�|���AWeek���ŧi
enum Week{SUN, MON, TUE, WED, THU, FRI, SAT};

int main()
{
   Week w;
   w = SUN;

   switch(w){
      case SUN: cout << "�P����C\n"; break;
      case MON: cout << "�P���@�C\n"; break;
      case TUE: cout << "�P���G�C\n"; break;
      case WED: cout << "�P���T�C\n"; break;
      case THU: cout << "�P���|�C\n"; break;
      case FRI: cout << "�P�����C\n"; break;
      case SAT: cout << "�P�����C\n"; break;
      default: cout << "�����D�O�P���X�H\n"; break;
   }

   return 0;
}
