#include <iostream>
using namespace std;

int main()
{
   char res; 

   cout << "�A�O�k�ͶܡH\n";
   cout << "�п�JY��N�C\n";

   cin >> res;

   if (res == 'Y' || res == 'y'){
      cout << "�A�O�k�ͳ�I\n";
     }
   else if(res == 'N' || res == 'n'){
      cout << "�A�O�k�ͳ�I\n";
   }
   else{
      cout << "�п�JY��N�C\n";
   }

   return 0;
}
