#include <iostream>
using namespace std;

int main()
{
   int ch = 0;

   for(int i=0; i<5; i++){
      for(int j=0; j<5; j++){
         if(ch == 0){
            cout << '*';
            ch = 1;
          }
         else{
            cout << '-';
            ch = 0;
         }
      }
       cout << '\n';
}

   return 0;
}