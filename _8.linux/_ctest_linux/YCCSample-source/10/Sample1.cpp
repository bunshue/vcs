#include <iostream>
using namespace std;

//funcㄧ计
void func();

int a = 0; 

//mainㄧ计
int main()
{
   int b = 1;

   cout << "mainㄧ计ずㄏノ跑计a籔b\n";
   cout << "跑计a" << a << "\n";
   cout << "跑计b" << b << "\n";
   //cout << "跑计c" << c << "\n";

   func();

   return 0;
}

//funcㄧ计﹚竡
void func()
{
   int c = 2;

   cout << "funcㄧ计ずㄏノ跑计a籔c\n";
   cout << "跑计a" << a << "\n";
   //cout << "跑计b" << b << "\n";
   cout << "跑计c" << c << "\n";
}
