#include <iostream>
using namespace std;

int main()
{
   for (int i=0; i<=10; i++){
      cout.width(3);
      cout.fill('-');
      cout << i; 
   }
   cout << '\n';

   return 0;
}

