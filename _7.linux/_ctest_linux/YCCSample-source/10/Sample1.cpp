#include <iostream>
using namespace std;

//func��ƪ��ŧi
void func();

int a = 0; 

//main���
int main()
{
   int b = 1;

   cout << "�i�H�bmain��Ƥ��ϥ��ܼ�a�Pb�C\n";
   cout << "�ܼ�a���Ȭ�" << a << "�C\n";
   cout << "�ܼ�b���Ȭ�" << b << "�C\n";
   //cout << "�ܼ�c���Ȭ�" << c << "�C\n";

   func();

   return 0;
}

//func��ƪ��w�q
void func()
{
   int c = 2;

   cout << "�i�H�bfunc��Ƥ��ϥ��ܼ�a�Pc�C\n";
   cout << "�ܼ�a���Ȭ�" << a << "�C\n";
   //cout << "�ܼ�b���Ȭ�" << b << "�C\n";
   cout << "�ܼ�c���Ȭ�" << c << "�C\n";
}
