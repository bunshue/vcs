#include <iostream>
using namespace std;

//func��ƪ��ŧi
void func();

int a = 0; 

//main���
int main()
{
   for(int i=0; i<5; i++)
      func();

   return 0;
}

//func��ƪ��w�q
void func()
{
   int b = 0;
   static int c = 0;

   cout << "�ܼ�a��" << a <<  "�ܼ�b��" << b << "�ܼ�c��" << c << "�C\n";
   a++;	
   b++;
   c++;
}
