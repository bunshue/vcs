#include <iostream>
using namespace std;

int main()
{
   char str[] = "Hello";

   cout << "Hello\n";

   for(int i=0; str[i]!='\0'; i++){
      cout << str[i] << '*';
   }
   cout << '\n';

   return 0;
}
