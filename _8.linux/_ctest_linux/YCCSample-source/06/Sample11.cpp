#include <iostream>
using namespace std;

int main()
{
   int res; 

   cout << "�п�J���Z�]1��5�^�G\n";

   cin >> res;

   switch(res){
      case 1:
      case 2:
         cout << "�٭n�A�[�j��I\n";
         break;
      case 3:
      case 4:
         cout << "�N�ӳo�Ӽˤl�O���U�h�C\n";
         break;
      case 5:
         cout << "�۷��u�q��I\n";
         break;
      default:
         cout << "�п�J���Z�]1��5�^�G\n";
         break;
   }
   
   return 0;
}
