#include <iostream>
using namespace std;

//funcㄧ计
void func();

int a = 0; 

//mainㄧ计
int main()
{
   for(int i=0; i<5; i++)
      func();

   return 0;
}

//funcㄧ计﹚竡
void func()
{
   int b = 0;
   static int c = 0;

   cout << "跑计a" << a <<  "跑计b" << b << "跑计c" << c << "\n";
   a++;	
   b++;
   c++;
}
