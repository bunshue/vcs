#include <iostream>
using namespace std;

int main()
{
   int num;
   cout << "�п�J1��9���������@�Ʀr�C\n";
   cin >> num;

   try{
      if(num <= 0)
         throw "��J�F0�H�U";
      if(num >= 10)
         throw "��J�F10�H�W";
      cout << num << "�C\n";
   }

   catch(char* err){
      cout << "���~�G:" << err << '\n';
      return 1;
   }

   return 0;
}
